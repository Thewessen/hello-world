use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use std::cmp::Ordering;

#[derive(StructOpt, Debug)]
struct Cli {
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);

    let mut seats = reader
        .lines()
        .filter_map(|line| line.ok())
        .filter(|line| !line.is_empty())
        .map(|seat| Seat::from(seat.as_str()));

    let result = match args.part_two {
        true => owned_seat(&mut seats),
        false => seats.fold(Seat::default(), |a, b| {
            if a >= b { a } else { b }
        })
    };

    println!("{}", result.id);
    Ok(())
}

fn id_from_space(s: &str) -> u32 {
    s.chars()
     .map(|ch| match ch {
         'B' => '1',
         'F' => '0',
         'R' => '1',
         'L' => '0',
         _ => '0',
     })
     .filter_map(|b| b.to_digit(2))
     .fold(0, |n, b| n * 2 + b)
}

fn owned_seat<I>(seats: &mut I) -> Seat
where I: Iterator<Item = Seat>
{
    let mut plain = (0..(1 << 11))
        .map(|i| Seat::from(i))
        .collect::<Vec<Seat>>();

    // sort seats
    seats.for_each(|seat| {
        let id = seat.id as usize;
        plain[id] = seat.to_owned();
    });

    let mut iter = plain.iter().skip_while(|seat| seat.free).peekable();
    loop {
        let seat = iter.next().expect("available seat");
        if seat.free && !iter.peek().expect("occupied seat").free {
            break seat.to_owned();
        }
    }
}

#[derive(Eq, Debug)]
struct Seat {
    id: u32,
    free: bool,
}

impl Default for Seat {
    fn default() -> Seat {
        Seat { id: 0, free: true }
    }
}

impl From<u32> for Seat {
    fn from(id: u32) -> Self {
        Seat { id, ..Seat::default() }
    }
}

impl From<&str> for Seat {
    fn from(s: &str) -> Self {
        let id = id_from_space(s);
        Seat { id, ..Seat::default() }
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
        assert_eq!(id_from_space("FBF"), 2);
        assert_eq!(id_from_space("BFB"), 5);

        assert_eq!(id_from_space("LRR"), 3);
        assert_eq!(id_from_space("RRL"), 6);
    }
}
