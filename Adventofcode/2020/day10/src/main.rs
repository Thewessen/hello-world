use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
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
    let mut numbers = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .map(|numb| numb.parse::<u64>().unwrap_or(0))
        .collect::<Vec<u64>>();
    numbers.sort();
    if args.part_two {
        let result = possible_routes(numbers);
        println!("{}", result);
    } else {
        let diffs = joltage_differences(numbers);
        let (a, b) = count_diffs(diffs);
        println!("{}", a * b);
    }
    Ok(())
}

fn joltage_differences(numbers: Vec<u64>) -> Vec<u8> {
    let mut iter = numbers.iter().peekable();
    let mut diff = vec![];
    let mut a = 0;
    loop {
        let b = match iter.peek() {
            Some(number) => **number,
            None => a + 3,
        };
        diff.push((b - a) as u8);
        a = match iter.next() {
            Some(number) => *number,
            None => break diff,
        };
    }
}

fn count_diffs(diffs: Vec<u8>) -> (u32, u32) {
    let a = diffs.iter().filter(|n| n == &&1).count() as u32;
    let b = diffs.iter().filter(|n| n == &&3).count() as u32;
    (a, b)
}

fn possible_routes(numbers: Vec<u64>) -> u64 {
    numbers
        .iter()
        .rev()
        .fold(Vec::<(u64, u64)>::with_capacity(3), |mut mem, curr| {
            if mem.is_empty() { mem.push((1, *curr)); }
            else {
                mem = mem
                    .iter()
                    .filter(|(_, n)| n - curr <= 3)
                    .cloned()
                    .collect::<Vec<(u64, u64)>>();
                let routes = mem.iter().fold(0, |c, (routes, _)| c + routes);
                mem.push((routes, *curr));
            }
            mem
        })
        .iter()
        .filter(|(_, n)| n - 0 <= 3)
        .fold(0, |curr, (routes, _)| curr + routes)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sorted_joltage_difference() {
        let a = vec![1, 2, 3, 4, 5];
        assert_eq!(joltage_differences(a), vec![1, 1, 1, 1, 1, 3]);
    }

    #[test]
    fn test_small_joltage_difference() {
        let mut a = vec![16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4];
        a.sort();
        assert_eq!(joltage_differences(a), vec![1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]);
    }

    #[test]
    fn test_large_joltage_difference() {
        let mut a = vec![28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                     38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3];
        a.sort();
        let mut answ = joltage_differences(a);
        answ.sort();
        let mut s = vec![1; 22];
        s.append(vec![3; 10].as_mut());
        assert_eq!(answ, s);
    }

    #[test]
    fn test_count_diffs() {
        let mut s = vec![1; 22];
        s.append(vec![3; 10].as_mut());
        assert_eq!(count_diffs(s), (22, 10));
    }

    #[test]
    fn test_simple_possible_routes() {
        assert_eq!(possible_routes(vec![1, 2, 3, 4, 5]), 13);
    }

    #[test]
    fn test_real_possible_routes() {
        let mut a = vec![16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4];
        a.sort();
        assert_eq!(possible_routes(a), 8);
    }

    #[test]
    fn test_real_large_possible_routes() {
        let mut a = vec![28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                     38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3];
        a.sort();
        assert_eq!(possible_routes(a), 19_208);
    }
}
