use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use num::{One, Zero};
use num::integer::{lcm, Integer, ExtendedGcd};
use num::bigint::{BigInt, ToBigInt};

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
    let mut reader = BufReader::new(file);
    let mut ids = String::new();
    let mut depart = String::new();
    reader.read_line(&mut depart)
        .expect("first line should be the departure");
    reader.read_line(&mut ids)
        .expect("second line should be bus id's");

    let schema: Vec<&str> = ids
        .trim()
        .split(',')
        .collect();

    if args.part_two {
        // input: 560214575859998
        // input2: 230903629977901
        println!("{}", first_special_timestamp(schema));
    } else {
        // input: 2238
        // input2: 4938
        let depart = depart
            .trim()
            .parse::<u32>()
            .expect("departure should be a number");

        let (id, waiting_minutes) = earliest_bus(schema, &depart);
        println!("{}", id * waiting_minutes);
    }
    Ok(())
}

fn earliest_bus(busses: Vec<&str>, depart: &u32) -> (u32, u32) {
    busses
        .iter()
        .filter_map(|id| id.parse::<u32>().ok())
        .map(|bus| (bus, bus - (depart % bus)))
        .fold((0, u32::MAX), |(a, b), (c, d)| {
            if d < b { (c, d) } else { (a, b) }
        })
}

fn first_special_timestamp(schema: Vec<&str>) -> BigInt {
    let busses: Vec<(BigInt, BigInt)> = schema
        .iter()
        .enumerate()
        .filter_map(|(idx, line)| line.parse::<u128>().ok()
            .and_then(|line| Some((idx.into(), line.into())))
        )
        .collect();
    
    let lcmultiple: BigInt = busses.iter()
        .fold(BigInt::one(), |acc, (_, line)| lcm(acc, line.to_bigint().unwrap()));

    busses
        .iter()
        .fold(BigInt::zero(), |acc, (idx, line)| {
            let p = &lcmultiple / line;
            let diff = (2 * line - idx) % line;
            let inv = modular_multiplicative_inverse(p.to_bigint().unwrap(), line);
            acc + inv * p * diff
        }) % lcmultiple
}

fn modular_multiplicative_inverse(a: BigInt, m: &BigInt) -> BigInt {
    let p = a % m;
    let e: ExtendedGcd<BigInt> = BigInt::extended_gcd(&p, &m);
    let solution = BigInt::one() * e.x / e.gcd;
    ((solution % m) + m) % m
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_earliest_bus() {
        let busses = vec!["7", "13", "59", "31", "19"];
        assert_eq!(earliest_bus(busses, &939), (59, 5));
    }

    #[test]
    fn test_simple_special_timestamp() {
        let schema: Vec<&str> = vec!["2","3","5"];
        assert_eq!(first_special_timestamp(schema), 8.into());
    }

    #[test]
    fn test_another_simple_special_timestamp() {
        let schema: Vec<&str> = vec!["2","5", "x", "7"];
        assert_eq!(first_special_timestamp(schema), 4.into());
    }

    #[test]
    fn test_first_special_timestamp() {
        let schema: Vec<&str> = vec!["7","13","x","x","59","x","31","19"];
        assert_eq!(first_special_timestamp(schema), 1_068_781.into());
    }

    #[test]
    fn test_second_special_timestamp() {
        let schema: Vec<&str> = vec!["67", "7", "59", "61"];
        assert_eq!(first_special_timestamp(schema), 754_018.into());
    }

    #[test]
    fn test_third_special_timestamp() {
        let schema: Vec<&str> = vec!["67", "x", "7", "59", "61"];
        assert_eq!(first_special_timestamp(schema), 779_210.into());
    }

    #[test]
    fn test_fourth_special_timestamp() {
        let schema: Vec<&str> = vec!["67", "7", "x", "59", "61"];
        assert_eq!(first_special_timestamp(schema), 1_261_476.into());
    }

    #[test]
    fn test_fifth_special_timestamp() {
        let schema: Vec<&str> = vec!["1789", "37", "47", "1889"];
        assert_eq!(first_special_timestamp(schema), 1_202_161_486.into());
    }

    #[test]
    fn test_extended_gcd() {
        let e: ExtendedGcd<i128> = i128::extended_gcd(&6, &7);
        assert_eq!(e.x, -1);
    }

    #[test]
    fn test_modular_multiplicative_inverse() {
        assert_eq!(modular_multiplicative_inverse(77.into(), &5.to_bigint().unwrap()), 3.into());
    }
}
