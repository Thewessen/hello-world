use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use itertools::Itertools;
use std::fs::File;

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
    let numbers = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .map(|numb| numb.parse::<u64>().unwrap_or(0))
        .collect::<Vec<u64>>();

    let (n, i) = first_xmas_flaw(&numbers, 25);
    if args.part_two {
        let (a, b) = sum_sequence(&numbers[..i], n)
            .expect("no solution");
        println!("{}", a + b);
    } else {
        println!("{}", n);
    }
    Ok(())
}

fn check_make_sum(numbers: &[u64], n: u64) -> bool {
    numbers
        .iter()
        .combinations(2)
        .any(|comb| comb[0] + comb[1] == n)
}

fn first_xmas_flaw(numbers: &Vec<u64>, preamble: usize) -> (u64, usize) {
    let mut next: usize = 0;
    while check_make_sum(&numbers[next..(preamble + next)], numbers[preamble + next]) {
        next += 1;
    }
    let i = preamble + next;
    (numbers[i], i)
}

fn sum_sequence(numbers: &[u64], n: u64) -> Result<(u64, u64), &str> {
    let mut from = 0;
    let result = loop {
        let mut adds = vec![];
        for p in numbers[from..].iter() {
            adds.push(*p);
            if adds.iter().fold(0, |a, b| a + b) >= n {
                break;
            }
        }
        if adds.iter().fold(0, |a, b| a + b) == n {
            break adds;
        } else {
            from += 1;
        }
    };
    let a = result.iter().fold(u64::MAX, |a, b| {
        if &a <= b { a } else { *b }
    });
    let b = result.iter().fold(u64::MIN, |a, b| {
        if &a >= b { a } else { *b }
    });
    Ok((a, b))
}

mod tests {
    use super::*;

    #[test]
    fn test_check_sum() {
        assert!(check_make_sum(&[1, 2, 3], 5));
        assert!(check_make_sum(&[3, 10, 1], 4));
        assert_eq!(check_make_sum(&[4, 10, 1], 4), false);
    }

    #[test]
    fn test_first_xmas_flaw() {
        assert_eq!(first_xmas_flaw(vec![4, 10, 1, 11, 12, 14], 3).0, 14);
    }

    #[test]
    fn test_next_xmas_flaw() {
        assert_eq!(first_xmas_flaw(vec![4, 10, 1, 11, 12, 14], 2).0, 1);
    }

    #[test]
    fn test_real_xmas_flaw() {
        let numbers = vec![35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576];
        assert_eq!(first_xmas_flaw(numbers, 5).0, 127);
    }

    #[test]
    fn test_sum_sequence() {
        assert_eq!(sum_sequence(&[1, 2, 3, 4], 9), Ok((2, 4)));
    }

    #[test]
    fn test_real_sum_sequence() {
        let numbers = [35,20,15,25,47,40,62,55,65,95,102,117,150,182];
        assert_eq!(sum_sequence(&numbers, 127), Ok((15, 47)));
    }
}
