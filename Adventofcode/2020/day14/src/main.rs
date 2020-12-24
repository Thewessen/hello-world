use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use num_traits::pow;
use std::collections::HashMap;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    v2: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let instructs: Vec<String> = reader
        .lines()
        .filter_map(|line| line.ok())
        .filter(|line| !line.is_empty())
        .collect();

    // --part1--
    // input: 11327140210986
    // input2: 5875750429995
    //
    // --part2--
    // input: 2308180581795
    // input2: 5272149590143
     let result = Mem::from_instructs(instructs, args.v2).calc_value();
     println!("{}", result);
    Ok(())
}

#[derive(Debug, PartialEq, Eq)]
struct Mem {
    mem: HashMap<u64, u64>,
    mask: String,
    floating: bool,
}

impl Default for Mem {
    fn default() -> Self {
        Mem {
            mem: HashMap::new(),
            mask: ['X'; 36].iter().collect(),
            floating: false,
        }
    }
}

impl From<bool> for Mem {
    fn from(floating: bool) -> Self {
        Mem { floating, ..Mem::default() }
    }
}

impl Mem {
    fn read(&mut self, line: &str) -> () {
        if line.starts_with("mask") {
            self.mask = Reader::read_mask(line);
        } else if line.starts_with("mem") {
            let (address, value) = Reader::read_mem(line);
            if self.floating {
                self.floating_address(address, value, 0, 0);
            } else {
                self.masked_value(address, value);
            }
        }
    }

    fn masked_value(&mut self, address: u64, value: u64) -> () {
        let value = self.mask
            .chars()
            .rev()
            .enumerate()
            .map(|(i, m)| match m {
                '0' | '1' => (i, m.to_digit(2).unwrap() as u64),
                _ => (i, value as u64 / pow(2, i) % 2)
            })
            .fold(0, |acc, (i, b)| {
                acc + b * pow(2, i)
            });
        self.mem.insert(address, value);
    }

    fn floating_address(&mut self, address: u64, value: u64, new_address: u64, i: usize) -> () {
        let adds = match self.mask.chars().rev().nth(i) {
            Some('1') => vec![Some(true), None],
            Some('0') if address / pow(2, i) % 2 == 1 =>
                vec![Some(true), None],
            Some('0') => vec![Some(false), None],
            Some('X') => vec![Some(false), Some(true)],
            None => {
                self.mem.insert(new_address, value);
                vec![None, None]
            },
            _ => unreachable!("mask should only contain 1, 0 or X"),
        };
        for a in adds.iter() {
            match a {
                Some(true) => self.floating_address(address, value, new_address + pow(2, i), i + 1),
                Some(false) => self.floating_address(address, value, new_address, i + 1),
                None => (),
            };
        }
    }

    fn from_instructs(instructs: Vec<String>, floating: bool) -> Self {
        let mut mem = Mem::from(floating);
        instructs.iter().for_each(|line| mem.read(line));
        mem
    }

    fn calc_value(&self) -> u64 {
        self.mem.values().fold(0, |acc, curr| acc + curr)
    }
}

struct Reader {}

impl Reader {
    fn read_mask(line: &str) -> String {
        line
            .split(" = ")
            .nth(1)
            .expect("mask")
            .to_string()
    }
    
    fn read_mem(line: &str) -> (u64, u64) {
        let mut fields = line
            .split(" = ");
        let address: u64 = fields.next()
            .expect("address field")
            .chars()
            .filter(|ch| ch.is_numeric())
            .collect::<String>()
            .parse()
            .unwrap();
        let value: u64 = fields.next()
            .expect("value field")
            .parse()
            .unwrap();
        (address, value)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_floor_div() {
        assert_eq!(5 / 2, 2);
    }

    #[test]
    fn test_value_one_with_mask() {
        let mut mem = Mem {
            mask: String::from("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
            ..Mem::default()
        };
        mem.masked_value(10, 11);
        assert_eq!(mem.mem.get(&10), Some(&73));
    }

    #[test]
    fn test_value_second_with_mask() {
        let mut mem = Mem {
            mask: String::from("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
            ..Mem::default()
        };
        mem.masked_value(10, 101);
        assert_eq!(mem.mem.get(&10), Some(&101));
    }

    #[test]
    fn test_value_third_with_mask() {
        let mut mem = Mem {
            mask: String::from("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
            ..Mem::default()
        };
        mem.masked_value(10, 0);
        assert_eq!(mem.mem.get(&10), Some(&64));
    }

    #[test]
    fn test_create_mem() {
        let mem = Mem {
            floating: true,
            ..Mem::default()
        };
        assert_eq!(Mem::from(true), mem);
    }

    #[test]
    fn test_follow_instructions() {
        let instructs = vec![
            String::from("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
            String::from("mem[8] = 11"),
            String::from("mem[7] = 101"),
            String::from("mem[8] = 0"),
        ];
        assert_eq!(Mem::from_instructs(instructs, false).calc_value(), 165);
    }

    #[test]
    fn test_follow_instructions_v2() {
        let instructs = vec![
          String::from("mask = 000000000000000000000000000000X1001X"),
          String::from("mem[42] = 100"),
          String::from("mask = 00000000000000000000000000000000X0XX"),
          String::from("mem[26] = 1"),
        ];
        let mem = Mem::from_instructs(instructs, true);
        assert_eq!(mem.mem.get(&58), Some(&100));
        assert_eq!(mem.mem.get(&58), Some(&100));
        assert_eq!(mem.mem.get(&16), Some(&1));
        assert_eq!(mem.mem.get(&26), Some(&1));
        assert_eq!(mem.mem.get(&27), Some(&1));
        assert_eq!(mem.calc_value(), 208);
    }
}
