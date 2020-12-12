use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use std::convert::TryFrom;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "t", long="toboggan")]
    toboggan: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let toboggan = args.toboggan;
    let result = reader
        .lines()
        .filter_map(|line| line.ok())
        .filter_map(|line| Password::try_from(line.as_ref()).ok())
        .fold(0, |r, p| {
            if toboggan {
                r + (p.is_valid_toboggan() as u16)
            } else {
                r + (p.is_valid() as u16)
            }
        });

    println!("{}", result);

    Ok(())
}

#[derive(Debug, PartialEq, Eq)]
struct Policy {
    letter: char,
    lower_bound: usize,
    upper_bound: usize
}

#[derive(Debug, PartialEq, Eq)]
struct Password {
    value: String,
    policy: Policy,
}

impl TryFrom<&str> for Password {
    type Error = &'static str;

    fn try_from(s: &str) -> Result<Self, Self::Error> {
        let mut parts = s.split(' ');
        let mut bounds = parts.next()
            .expect("string should not be empty")
            .split('-')
            .filter_map(|n| n.parse::<usize>().ok());
        let letter = parts.next()
            .and_then(|part| part.chars().next())
            .expect("policy should contain a letter");
        let value = parts.next()
            .unwrap_or("")
            .to_string();
        let password = Password { value, policy: Policy {
            letter,
            lower_bound: bounds.next().unwrap_or(0),
            upper_bound: bounds.next().unwrap_or(0),
        }};
        Ok(password)
    }
}

impl Password {
    fn is_valid(&self) -> bool {
        let count = self.value.chars()
            .filter(|ch| ch == &self.policy.letter)
            .count();
         self.policy.lower_bound <= count && count <= self.policy.upper_bound
    }

    fn is_valid_toboggan(&self) -> bool {
        let mut chars = self.value.chars();
        let first = match chars.nth((self.policy.lower_bound - 1) as usize) {
            Some(chr) => chr,
            None => return false,
        };
        let second = match chars.nth(
            (self.policy.upper_bound - self.policy.lower_bound - 1) as usize
        ) {
            Some(chr) => chr,
            None => return false,
        };
        (first == self.policy.letter) ^ (second == self.policy.letter)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn correct_password_from_str() {
        let p = Password {
            value: String::from("asoeut"),
            policy: Policy {
                letter: 'a',
                lower_bound: 1,
                upper_bound: 3,
            }};
        assert_eq!(Password::try_from("1-3 a: asoeut"), Ok(p));
    }

    #[test]
    fn is_valid_password() {
        let p = Password {
            value: String::from("asoeut"),
            policy: Policy {
                letter: 'a',
                lower_bound: 1,
                upper_bound: 3,
            }};
        assert!(p.is_valid());
    }

    #[test]
    fn is_not_valid_password() {
        let p = Password {
            value: String::from("asoeut"),
            policy: Policy {
                letter: 'b',
                lower_bound: 1,
                upper_bound: 3,
            }};
        assert_eq!(p.is_valid(), false);
    }

    #[test]
    fn is_first_valid_toboggan() {
        let p = Password {
            value: String::from("asoeut"),
            policy: Policy {
                letter: 's',
                lower_bound: 2,
                upper_bound: 4,
            }};
        assert!(p.is_valid_toboggan());
    }

    #[test]
    fn is_second_valid_toboggan() {
        let p = Password {
            value: String::from("asoeut"),
            policy: Policy {
                letter: 'e',
                lower_bound: 2,
                upper_bound: 4,
            }};
        assert!(p.is_valid_toboggan());
    }

    #[test]
    fn is_first_not_valid_toboggan() {
        let p = Password {
            value: String::from("osoeut"),
            policy: Policy {
                letter: 'x',
                lower_bound: 2,
                upper_bound: 5,
            }};
        assert_eq!(p.is_valid_toboggan(), false);
    }

    #[test]
    fn is_second_not_valid_toboggan() {
        let p = Password {
            value: String::from("osoeut"),
            policy: Policy {
                letter: 'o',
                lower_bound: 1,
                upper_bound: 3,
            }};
        assert_eq!(p.is_valid_toboggan(), false);
    }
}
