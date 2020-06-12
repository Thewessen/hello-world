use std::convert::TryFrom;

#[derive(Debug, PartialEq)]
pub enum Nucleo { A, C, G, T, U }

impl TryFrom<&char> for Nucleo {
    type Error = ();
    fn try_from(ch: &char) -> Result<Self, Self::Error> {
        match ch {
            'A' => Ok(Nucleo::A),
            'C' => Ok(Nucleo::C),
            'G' => Ok(Nucleo::G),
            'T' => Ok(Nucleo::T),
            'U' => Ok(Nucleo::U),
            _   => Err(()),
        }
    }
}

#[derive(Debug, PartialEq)]
pub struct DNA {
    nucleotides: Vec<Nucleo>
}

#[derive(Debug, PartialEq)]
pub struct RNA {
    nucleotides: Vec<Nucleo>
}

impl DNA {
    pub fn new(dna: &str) -> Result<DNA, usize> {
        dna.char_indices()
           .map(|(i, ch)| match Nucleo::try_from(&ch) {
               Ok(Nucleo::U)|Err(_) => Err(i),
               Ok(nucleo)           => Ok(nucleo),
           })
           .collect::<Result<Vec<Nucleo>, usize>>()
           .and_then(|nucleotides| Ok(DNA { nucleotides }))
    }

    pub fn into_rna(self) -> RNA {
        let nucleotides = self.nucleotides.iter().map(
            |n| match n {
                Nucleo::G => Nucleo::C,
                Nucleo::C => Nucleo::G,
                Nucleo::T => Nucleo::A,
                Nucleo::A => Nucleo::U,
                _ => unreachable!("DNA should not contain nucleotide {:?}", n),
           }).collect();
        RNA { nucleotides }
    }
}

impl RNA {
    pub fn new(rna: &str) -> Result<RNA, usize> {
        rna.char_indices()
           .map(|(i, ch)| match Nucleo::try_from(&ch) {
               Ok(Nucleo::T)|Err(_) => Err(i),
               Ok(nucleo)           => Ok(nucleo),
           })
           .collect::<Result<Vec<Nucleo>, usize>>()
           .and_then(|nucleotides| Ok(RNA { nucleotides }))
    }
}
