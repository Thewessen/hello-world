use std::io::{self};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::read_to_string;
use regex::Regex;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "s", long = "strict")]
    strict: bool,
}

/// PART1:
/// The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
///```
/// byr (Birth Year)
/// iyr (Issue Year)
/// eyr (Expiration Year)
/// hgt (Height)
/// hcl (Hair Color)
/// ecl (Eye Color)
/// pid (Passport ID)
/// cid (Country ID)
///```
///
/// Passport data is validated in batch files (your puzzle input). Each passport is represented as a
/// sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank
/// lines.
/// 
/// Here is an example batch file containing four passports:
///```
///ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
///byr:1937 iyr:2017 cid:147 hgt:183cm
///
///iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
///hcl:#cfa07d byr:1929
///
///hcl:#ae17e1 iyr:2013
///eyr:2024
///ecl:brn pid:760753108 byr:1931
///hgt:179cm
///
///hcl:#cfa07d eyr:2025 pid:166559648
///iyr:2011 ecl:brn hgt:59in
///```
/// The first passport is valid - all eight fields are present. The second passport is invalid - it
/// is missing hgt (the Height field).
/// 
/// The third passport is interesting; the only missing field is cid, so it looks like data from
/// North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system
/// temporarily ignore missing cid fields. Treat this "passport" as valid.
/// 
/// The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any
/// other field is not, so this passport is invalid.
/// 
/// According to the above rules, your improved system would report 2 valid passports.
///
/// PART 2:
/// You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
/// ```
/// byr (Birth Year) - four digits; at least 1920 and at most 2002.
/// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
/// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
/// hgt (Height) - a number followed by either cm or in:
///     If cm, the number must be at least 150 and at most 193.
///     If in, the number must be at least 59 and at most 76.
/// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
/// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
/// pid (Passport ID) - a nine-digit number, including leading zeroes.
/// cid (Country ID) - ignored, missing or not.
/// ```
/// Your job is to count the passports where all required fields are both present and valid according to the above rules.
fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let strict = args.strict;
    let content = read_to_string(args.file)?;
    let result = content
        .split("\n\n")
        .filter(|passport| !passport.is_empty())
        .map(Passport::from_str)
        .filter(|p| {
            if strict {
                p.is_strict_valid()
            } else {
                p.is_valid()
            }
        })
        .count();
    println!("{}", result);
    Ok(())
}

#[derive(Debug)]
struct Passport {
    byr: Option<String>,
    iyr: Option<String>,
    eyr: Option<String>,
    hgt: Option<String>,
    hcl: Option<String>,
    ecl: Option<String>,
    pid: Option<String>,
    cid: Option<String>,
}

impl Passport {
    fn new() -> Self {
        Passport {
            byr: None,
            iyr: None,
            eyr: None,
            hgt: None,
            hcl: None,
            ecl: None,
            pid: None,
            cid: None,
        }
    }

    fn from_str(passport: &str) -> Self {
        let mut p = Self::new();
        passport
            .split(|ch| ch == ' ' || ch == '\n') 
            .filter(|field| !field.is_empty())
            .map(|field| field.split(':'))
            .for_each(|mut field| {
                match field.next().unwrap() {
                    "byr" => p.byr = Some(field.next().unwrap().to_owned()),
                    "iyr" => p.iyr = Some(field.next().unwrap().to_owned()),
                    "eyr" => p.eyr = Some(field.next().unwrap().to_owned()),
                    "hgt" => p.hgt = Some(field.next().unwrap().to_owned()),
                    "hcl" => p.hcl = Some(field.next().unwrap().to_owned()),
                    "ecl" => p.ecl = Some(field.next().unwrap().to_owned()),
                    "pid" => p.pid = Some(field.next().unwrap().to_owned()),
                    "cid" => p.cid = Some(field.next().unwrap().to_owned()),
                    _ => (),
                }
            });
        p
    }

    pub fn is_valid(&self) -> bool {
        self.byr != None &&
        self.iyr != None &&
        self.eyr != None &&
        self.hgt != None &&
        self.hcl != None &&
        self.ecl != None &&
        self.pid != None
    }

    pub fn is_strict_valid(&self) -> bool {
        // println!("{:#?}", self);
        // println!("byr: {:?}", matches_number(&self.byr.as_ref().unwrap(), 1920, 2002));
        // println!("iyr: {:?}", matches_number(&self.iyr.as_ref().unwrap(), 2010, 2020));
        self.is_valid() &&
        matches_number(&self.byr.as_ref().unwrap(), 1920, 2002) &&
        matches_number(&self.iyr.as_ref().unwrap(), 2010, 2020) &&
        matches_number(&self.eyr.as_ref().unwrap(), 2020, 2030) &&
        {
            let height = self.hgt.as_ref().unwrap();
            let ln = height.len() - 2;
            let result = {
                if height.ends_with("cm") {
                    matches_number(&height[..ln], 150, 193)
                } else if height.ends_with("in") {
                    matches_number(&height[..ln], 59, 76)
                } else {
                    false
                }
            };
            // println!("hgt: {:?}", result);
            result
        } && {
            let re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
            let result = re.is_match(&self.hcl.as_ref().unwrap());
            // println!("hcl: {:?}", result);
            result
        } && {
            let ecl = self.ecl.as_ref().unwrap();
            let result = ecl == "amb" ||
                ecl == "blu" ||
                ecl == "brn" ||
                ecl == "gry" ||
                ecl == "grn" ||
                ecl == "hzl" ||
                ecl == "oth";
            // println!("ecl: {:?}", result);
            result
        } && {
            let re = Regex::new(r"^[0-9]{9}$").unwrap();
            let result = re.is_match(&self.pid.as_ref().unwrap());
            // println!("pid: {:?}", result);
            result
        }
    }
}

impl PartialEq for Passport {
    fn eq(&self, other: &Self) -> bool {
        self.byr == other.byr &&
        self.iyr == other.iyr &&
        self.eyr == other.eyr &&
        self.hgt == other.hgt &&
        self.hcl == other.hcl &&
        self.ecl == other.ecl &&
        self.pid == other.pid
    }
}
impl Eq for Passport {}

fn matches_number(s: &str, least: u16, most: u16) -> bool {
    let digit = s.parse::<u16>().unwrap();
    least <= digit && digit <= most
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_from_str() {
        let p = Passport {
            byr: Some(String::from("1966")),
            iyr: Some(String::from("2012")),
            eyr: Some(String::from("2020")),
            hgt: Some(String::from("151cm")),
            hcl: Some(String::from("#ceb3a1")),
            ecl: Some(String::from("grn")),
            pid: Some(String::from("947726115")),
            cid: Some(String::from("105")),
        };
        let r = Passport::from_str("eyr:2020 cid:105 iyr:2012 pid:947726115\nhcl:#ceb3a1 ecl:grn byr:1966 hgt:151cm");
        assert_eq!(p, r);
    }

    #[test]
    fn is_valid() {
        let p = Passport {
            byr: Some(String::new()),
            iyr: Some(String::new()),
            eyr: Some(String::new()),
            hgt: Some(String::new()),
            hcl: Some(String::new()),
            ecl: Some(String::new()),
            pid: Some(String::new()),
            cid: None,
        };
        assert!(p.is_valid());
    }

    #[test]
    fn match_number() {
        assert!(matches_number("206", 200, 208));
    }

    #[test]
    fn is_strict_valid() {
        let p = Passport {
            byr: Some(String::from("1966")),
            iyr: Some(String::from("2012")),
            eyr: Some(String::from("2020")),
            hgt: Some(String::from("151cm")),
            hcl: Some(String::from("#ceb3a1")),
            ecl: Some(String::from("grn")),
            pid: Some(String::from("947726115")),
            cid: Some(String::from("105")),
        };
        assert!(p.is_strict_valid());
    }

    #[test]
    fn invalid_passpords() {
        let p = Passport::from_str("eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from_str("iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from_str("hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from_str("hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007");
        assert_eq!(p.is_strict_valid(), false);
    }
}
