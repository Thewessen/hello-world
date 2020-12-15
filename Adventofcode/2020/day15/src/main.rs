use structopt::StructOpt;
use std::collections::HashMap;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(default_value = "0")]
    till: u64,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
}

fn main() {
    let args = Cli::from_args();
    let puzzle = vec![8, 13, 1, 0, 18, 9];
    let result = if args.till != 0 {
        solve_puzzle(puzzle, args.till as usize)
    } else if args.part_two {
        solve_puzzle(puzzle, 30_000_000)
    } else {
        solve_puzzle(puzzle, 2020)
    };
    println!("{}", result);
}

fn solve_puzzle(numbers: Vec<u64>, till: usize) -> u64 {
    if numbers.is_empty() {
        panic!("no puzzle input");
    }
    let mut spoken: u64 = *numbers.iter().last().unwrap();
    let mut mem: HashMap<u64, usize> = numbers
        .iter()
        .enumerate()
        .map(|(i, n)| (*n, i))
        .take(numbers.len() - 1)
        .collect();
    for i in numbers.len()..till {
        let n = match mem.get(&spoken) {
            Some(j) => i - j - 1, 
            None => 0,
        };
        mem.insert(spoken, i - 1);
        spoken = n as u64;
    }
    spoken
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_puzzle() {
        let p = vec![0, 3, 6];
        assert_eq!(solve_puzzle(p, 2020), 436);
    }

    #[test]
    fn test_second_puzzle() {
        let p = vec![1, 3, 2];
        assert_eq!(solve_puzzle(p, 2020), 1);
    }

    #[test]
    fn test_third_puzzle() {
        let p = vec![2, 1, 3];
        assert_eq!(solve_puzzle(p, 2020), 10);
    }

    #[test]
    fn test_fourth_puzzle() {
        let p = vec![1, 2, 3];
        assert_eq!(solve_puzzle(p, 2020), 27);
    }

    #[test]
    fn test_fifth_puzzle() {
        let p = vec![2, 3, 1];
        assert_eq!(solve_puzzle(p, 2020), 78);
    }

    #[test]
    fn test_sixth_puzzle() {
        let p = vec![3, 2, 1];
        assert_eq!(solve_puzzle(p, 2020), 438);
    }

    #[test]
    fn test_seventh_puzzle() {
        let p = vec![3, 1, 2];
        assert_eq!(solve_puzzle(p, 2020), 1_836);
    }

    #[test] #[ignore]
    fn test_part_two_first_puzzle() {
        let p = vec![0, 3, 6];
        assert_eq!(solve_puzzle(p, 30_000_000), 175_594);
    }

    #[test] #[ignore]
    fn test_part_two_second_puzzle() {
        let p = vec![1, 3, 2];
        assert_eq!(solve_puzzle(p, 30_000_000), 2_578);
    }

    #[test] #[ignore]
    fn test_part_two_third_puzzle() {
        let p = vec![2, 1, 3];
        assert_eq!(solve_puzzle(p, 30_000_000), 3_544_142);
    }

    #[test] #[ignore]
    fn test_part_two_fourth_puzzle() {
        let p = vec![1, 2, 3];
        assert_eq!(solve_puzzle(p, 30_000_000), 261_214);
    }

    #[test] #[ignore]
    fn test_part_two_fifth_puzzle() {
        let p = vec![2, 3, 1];
        assert_eq!(solve_puzzle(p, 30_000_000), 6_895_259);
    }

    #[test] #[ignore]
    fn test_part_two_sixth_puzzle() {
        let p = vec![3, 2, 1];
        assert_eq!(solve_puzzle(p, 30_000_000), 18);
    }

    #[test] #[ignore]
    fn test_part_two_seventh_puzzle() {
        let p = vec![3, 1, 2];
        assert_eq!(solve_puzzle(p, 30_000_000), 362);
    }
}
