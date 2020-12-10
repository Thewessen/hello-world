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

/// PART 1:
/// You write a quick program to use your phone's camera to scan all of the nearby boarding passes
/// (your puzzle input); perhaps you can find your seat through process of elimination.
/// 
/// Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat
/// might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and
/// R means "right".
/// 
/// The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the
/// plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is
/// in. Start with the whole list of rows; the first letter indicates whether the seat is in the
/// front (0 through 63) or the back (64 through 127). The next letter indicates which half of that
/// region the seat is in, and so on until you're left with exactly one row.
///
/// PART 2:
/// It's a completely full flight, so your seat should be the only missing boarding pass in your
/// list. However, there's a catch: some of the seats at the very front and back of the plane don't
/// exist on this aircraft, so they'll be missing from your list as well.
/// 
/// Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours
/// will be in your list.
/// 
/// What is the ID of your seat?
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
