use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use regex::Regex;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "t", long="toboggan")]
    toboggan: bool,
}

/// PART 1:
/// How many passwords are valid?
/// For example, suppose you have the following list:
/// ```
/// 1-3 a: abcde
/// 1-3 b: cdefg
/// 2-9 c: ccccccccc
/// ```
/// Each line gives the password policy and then the password.
/// The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
/// For example, `1-3` a means that the password must contain a at least `1` time and at most `3` times.
/// 
/// In the above example, `2` passwords are valid.
/// The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`.
/// The first and third passwords are valid: they contain one `a` or nine `c`,
/// both within the limits of their respective policies.
/// 
/// PART 2:
/// Each policy actually describes two positions in the password,
/// where `1` means the first character,
/// `2` means the second character, and so on.
/// (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
/// Exactly one of these positions must contain the given letter.
/// Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
///
/// Given the same example list from above:
/// ```
/// 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
/// 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
/// 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
/// ```
fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let toboggan = args.toboggan;
    let result = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .map(|line| (Policy::from_str(&line), get_password(&line)))
        .fold(0, |r, (p, s)| {
            if toboggan {
                r + (p.is_valid_toboggan(&s) as u16)
            } else {
                r + (p.is_valid(&s) as u16)
            }
        });

    println!("{}", result);

    Ok(())
}

#[derive(Debug)]
struct Policy {
    letter: char,
    lower_bound: u16,
    upper_bound: u16
}

impl Policy {
    pub fn from_str(s: &str) -> Self {
        let re = Regex::new(r"^(\d+)-(\d+) (\w)").unwrap();
        let caps = re.captures(s).unwrap();
        Policy {
            letter: caps.get(3).unwrap().as_str().chars().next().unwrap(),
            lower_bound: caps.get(1).unwrap().as_str().parse::<u16>().unwrap(),
            upper_bound: caps.get(2).unwrap().as_str().parse::<u16>().unwrap(),
        }
    }

    fn is_valid(&self, p: &str) -> bool {
        let count = p.chars()
            .filter(|ch| ch.to_owned() == self.letter)
            .count() as u16;
         self.lower_bound <= count && count <= self.upper_bound
    }

    fn is_valid_toboggan(&self, p: &str) -> bool {
        let mut chars = p.chars();
        let first = chars.nth((self.lower_bound - 1) as usize).unwrap_or(' ');
        let second = chars.nth((self.upper_bound - self.lower_bound - 1) as usize).unwrap_or(' ');
        (first == self.letter) ^ (second == self.letter)
    }
}

impl PartialEq for Policy {
    fn eq(&self, other: &Self) -> bool {
        self.letter == other.letter &&
        self.lower_bound == other.lower_bound &&
        self.upper_bound == other.upper_bound
    }
}
impl Eq for Policy {}

fn get_password(s: &str) -> String {
    s.split(':').nth(1).unwrap().trim().to_owned()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn correct_policy_from_str() {
        let p = Policy {
            letter: 'a',
            lower_bound: 1,
            upper_bound: 3,
        };
        assert_eq!(Policy::from_str("1-3 a: asoeut"), p);
    }

    #[test]
    fn correct_password_from_str() {
        assert_eq!(get_password("1-3 a: asoeut"), "asoeut");
    }

    #[test]
    fn is_valid_password() {
        let p = Policy {
            letter: 'a',
            lower_bound: 1,
            upper_bound: 3,
        };
        assert_eq!(p.is_valid("asoeut"), true);
    }

    #[test]
    fn is_not_valid_password() {
        let p = Policy {
            letter: 'b',
            lower_bound: 1,
            upper_bound: 3,
        };
        assert_eq!(p.is_valid("asoeut"), false);
    }

    #[test]
    fn is_first_valid_toboggan() {
        let p = Policy {
            letter: 's',
            lower_bound: 2,
            upper_bound: 4,
        };
        assert_eq!(p.is_valid_toboggan("asoeut"), true);
    }

    #[test]
    fn is_second_valid_toboggan() {
        let p = Policy {
            letter: 'e',
            lower_bound: 2,
            upper_bound: 4,
        };
        assert_eq!(p.is_valid_toboggan("asoeut"), true);
    }

    #[test]
    fn is_first_not_valid_toboggan() {
        let p = Policy {
            letter: 'x',
            lower_bound: 2,
            upper_bound: 5,
        };
        assert_eq!(p.is_valid_toboggan("osoeut"), false);
    }

    #[test]
    fn is_second_not_valid_toboggan() {
        let p = Policy {
            letter: 'o',
            lower_bound: 1,
            upper_bound: 3,
        };
        assert_eq!(p.is_valid_toboggan("osoeut"), false);
    }
}
