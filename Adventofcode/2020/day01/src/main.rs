use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use std::fs::File;
use structopt::StructOpt;
use itertools::Itertools;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "n", long = "number", default_value = "2")]
    number: usize,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let result = reader
        .lines()
        .map(|line| line.unwrap_or(String::from("0")))
        .map(|number| number.parse::<u32>().unwrap_or(0))
        .combinations(args.number)
        .fold(0, |result, comb| calc(comb).unwrap_or(result));
    println!("{}", result);
    Ok(())
}

/// Returns the product if sum matches 2020
/// ```
/// # 2 numbers
/// assert_eq!(calc(vec![7, 8]), Err(0))
/// assert_eq!(calc(vec![1000, 1020]), Ok(1_020_000))
/// # 3 numbers
/// assert_eq!(calc(vec![7, 8, 9]), Err(0))
/// assert_eq!(calc(vec![1000, 1000, 20]), Ok(20_000_000))
/// ```
fn calc(numbers: Vec<u32>) -> Result<u32, u32> {
    match numbers.iter().fold(0, |a, b| a + b) {
        2020 => Ok(numbers.iter().fold(1, |a, b| a * b)),
        _ => Err(0)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ok_two_numbers() {
        assert_eq!(calc(vec![1000, 1020]), Ok(1020000))
    }

    #[test]
    fn test_err_two_numbers() {
        assert_eq!(calc(vec![7, 8]), Err(0))
    }

    #[test]
    fn test_ok_three_numbers() {
        assert_eq!(calc(vec![1000, 1000, 20]), Ok(20_000_000))
    }

    #[test]
    fn test_err_three_numbers() {
        assert_eq!(calc(vec![7, 8, 9]), Err(0))
    }
}
