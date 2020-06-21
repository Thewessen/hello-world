pub fn collatz(n: u64) -> Option<u64> {
    match Collatz::from(n).count() {
        0 if n == 1 => Some(0),
        0 => None,
        i => Some(i as u64),
    }
}

pub struct Collatz { n: u64 }

impl From<u64> for Collatz {
    fn from(n: u64) -> Self {
        Collatz { n }
    }
}

impl Iterator for Collatz {
    type Item = u64;
    
    fn next(&mut self) -> Option<Self::Item> {
        if self.n <= 1 {
            None
        } else {
            match self.n % 2 == 0 {
                true => {
                    self.n /= 2;
                    Some(self.n)
                },
                false => {
                    self.n *= 3;
                    self.n += 1;
                    Some(self.n)
                },
            }
        }
    }
}
