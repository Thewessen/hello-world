use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use std::cmp::Ordering;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let mut result = Seat::new(0);
    let seats = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .map(|seat| Seat::from_binary_space(&seat));

    if args.part_two {
        let mut plain = (0..(1 << 11))
            .map(|i| Seat::new(i))
            .collect::<Vec<Seat>>();

        // sort seats
        seats.for_each(|seat| {
            let id = seat.id as usize;
            plain[id] = seat.to_owned();
        });

        let mut iter = plain.iter().skip_while(|seat| seat.free).peekable();
        result = loop {
            let seat = iter.next().unwrap();
            if seat.free && !iter.peek().unwrap().free {
                break seat.to_owned();
            }
        }
    } else {
        result = seats.fold(result, |a, b| {
            if a >= b { a } else { b }
        });
    }
    println!("{:?}", result.id);
    Ok(())
}

fn bin_from_space(s: &str) -> u32 {
    let bin = s.chars()
        .map(|ch| match ch {
            'B' => '1',
            'F' => '0',
            'R' => '1',
            'L' => '0',
            _ => '0',
        })
        .collect::<String>();
    u32::from_str_radix(&bin, 2).unwrap_or(0)
}

#[derive(Eq, Debug)]
struct Seat {
    id: u32,
    free: bool,
}

impl Seat {
    fn new(id: u32) -> Self {
        Seat { id, free: true }
    }

    fn from_binary_space(s: &str) -> Self {
        Seat {
            id: bin_from_space(&s),
            free: false
        }
    }
}

impl Ord for Seat {
    fn cmp(&self, other: &Self) -> Ordering {
        self.id.cmp(&other.id)
    }
}

impl PartialOrd for Seat {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.id.cmp(&other.id))
    }
}

impl PartialEq for Seat {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}

impl Copy for Seat { }
impl Clone for Seat {
    fn clone(&self) -> Seat {
        *self
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from_string() {
        assert_eq!(bin_from_space("FBF"), 2);
        assert_eq!(bin_from_space("BFB"), 5);

        assert_eq!(bin_from_space("LRR"), 3);
        assert_eq!(bin_from_space("RRL"), 6);
    }
}
