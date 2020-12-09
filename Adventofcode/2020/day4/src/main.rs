use std::io::{self};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::read_to_string;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
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
fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let content = read_to_string(args.file)?;
    let result = content
        .split("\n\n")
        .filter(|passport| !passport.is_empty())
        .map(Passport::from_str)
        .filter(|p| p.is_valid())
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
        self.is_valid() &&
        matches_number(self.byr, )
    }
}

#[cfg(test)]
mod tests {
}
