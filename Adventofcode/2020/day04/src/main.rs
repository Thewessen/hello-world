use std::io::{self};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::read_to_string;
use std::convert::TryFrom;
use std::mem::discriminant;

#[derive(StructOpt, Debug)]
struct Cli {
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "s", long = "strict")]
    strict: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let strict = args.strict;
    let content = read_to_string(args.file)?;
    let result = content
        .split("\n\n")
        .map(Passport::from)
        .filter(|p| match strict {
            true => p.is_strict_valid(),
            false => p.is_valid()
        })
        .count();

    println!("{}", result);
    Ok(())
}

#[derive(Debug, PartialEq, Eq)]
enum PasswordField {
    BirthYear(u16),
    IssueYear(u16),
    ExpirationYear(u16),
    Height(String),
    HairColor(String),
    EyeColor(String),
    PassportID(String),
    CountryID(String),
}

impl PasswordField {
    fn is_valid(&self) -> bool {
        match self {
            Self::BirthYear(value) => &1920 <= value && value <= &2002,
            Self::IssueYear(value) => &2010 <= value && value <= &2020,
            Self::ExpirationYear(value) => &2020 <= value && value <= &2030,
            Self::Height(value) => {
                let height = value.chars()
                        .take_while(|ch| ch.is_numeric())
                        .collect::<String>()
                        .parse::<u8>();
                if value.ends_with("cm") {
                    match height {
                        Ok(n) => 150 <= n && n <= 193,
                        Err(_) => false,
                    }
                } else if value.ends_with("in") {
                    match height {
                        Ok(n) => 59 <= n && n <= 76,
                        Err(_) => false,
                    }
                } else { false }
            },
            Self::HairColor(value) => value.starts_with("#") &&
                value.chars().skip(1).all(|ch| match ch {
                    'a'..='f' | '0'..='9' => true,
                    _ => false,
                }),
            Self::EyeColor(value) => ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                .iter().any(|color| color == value),
            Self::PassportID(value) => value.chars().all(|ch| ch.is_numeric()),
            Self::CountryID(_) => true,
        }
    }
}

impl TryFrom<&str> for PasswordField {
    type Error = &'static str;

    fn try_from(field: &str) -> Result<Self, Self::Error> {
        let mut iter = field.split(':');
        match iter.next() {
            Some("byr") => match iter.next().and_then(|n| n.parse::<u16>().ok()) {
                Some(n) => Ok(Self::BirthYear(n)),
                None => Err("invalid value for byr field")
            },
            Some("iyr") => match iter.next().and_then(|n| n.parse::<u16>().ok()) {
                Some(n) => Ok(Self::IssueYear(n)),
                None => Err("invalid value for iyr field")
            },
            Some("eyr") => match iter.next().and_then(|n| n.parse::<u16>().ok()) {
                Some(n) => Ok(Self::ExpirationYear(n)),
                None => Err("invalid value for eyr field")
            },
            Some("hgt") => match iter.next() {
                Some(v) => Ok(Self::Height(v.to_string())),
                None => Err("invalid value for hgt field")
            },
            Some("hcl") => match iter.next() {
                Some(v) => Ok(Self::HairColor(v.to_string())),
                None => Err("invalid value for hcl field")
            },
            Some("ecl") => match iter.next() {
                Some(v) => Ok(Self::EyeColor(v.to_string())),
                None => Err("invalid value for ecl field")
            },
            Some("pid") => match iter.next() {
                Some(v) => Ok(Self::PassportID(v.to_string())),
                None => Err("invalid value for pid field")
            },
            Some("cid") => match iter.next() {
                Some(v) => Ok(Self::CountryID(v.to_string())),
                None => Err("invalid value for cid field")
            },
            Some(_) => Err("no field for type found"),
            None => Err("field looks empty")
        }
    }
}

#[derive(Debug, PartialEq, Eq)]
struct Passport {
    fields: Vec<PasswordField>
}

impl Default for Passport {
    fn default() -> Self {
        Passport { fields: vec![] }
    }
}

impl From<&str> for Passport {
    fn from(passport: &str) -> Self {
        let fields: Vec<PasswordField> = passport
            .split(|ch| ch == ' ' || ch == '\n') 
            .filter(|field| !field.is_empty())
            .filter_map(|field| PasswordField::try_from(field).ok())
            .collect();
        Passport { fields }
    }
}

impl Passport {
    fn is_valid(&self) -> bool {
        use PasswordField::*;
        [ BirthYear(0), IssueYear(0), ExpirationYear(0),
          Height(String::default()),
          HairColor(String::default()),
          EyeColor(String::default()),
          PassportID(String::default())
        ].iter().all(|t| self.fields.iter().any(|f| discriminant(f) == discriminant(t)))
    }

    fn is_strict_valid(&self) -> bool {
        self.is_valid() && self.fields.iter()
            .all(|field| field.is_valid())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use PasswordField::*;

    #[test]
    fn test_match_equal_variants() {
        let n = IssueYear(100);
        let m = IssueYear(200);
        assert_eq!(discriminant(&n), discriminant(&m));
    }

    #[test]
    fn test_not_equal_variants() {
        let n = IssueYear(100);
        let m = ExpirationYear(200);
        assert_ne!(discriminant(&n), discriminant(&m));
    }

    #[test]
    fn parse_from_str() {
        let p = Passport {
            fields: vec![
                ExpirationYear(2020),
                CountryID(String::from("105")),
                IssueYear(2012),
                PassportID(String::from("947726115")),
                HairColor(String::from("#ceb3a1")),
                EyeColor(String::from("grn")),
                BirthYear(1966),
                Height(String::from("151cm")),
            ]
        };
        let r = Passport::from("eyr:2020 cid:105 iyr:2012 pid:947726115\nhcl:#ceb3a1 ecl:grn byr:1966 hgt:151cm");
        assert_eq!(p, r);
    }

    #[test]
    fn is_valid() {
        let p = Passport {
            fields: vec![
                ExpirationYear(2020),
                CountryID(String::from("105")),
                IssueYear(2012),
                PassportID(String::from("947726115")),
                HairColor(String::from("#ceb3a1")),
                EyeColor(String::from("grn")),
                BirthYear(1966),
                Height(String::from("151cm")),
            ]
        };
        assert!(p.is_valid());
    }

    #[test]
    fn is_strict_valid() {
        let p = Passport {
            fields: vec![
                ExpirationYear(2020),
                CountryID(String::from("105")),
                IssueYear(2012),
                PassportID(String::from("947726115")),
                HairColor(String::from("#ceb3a1")),
                EyeColor(String::from("grn")),
                BirthYear(1966),
                Height(String::from("151cm")),
            ]
        };
        assert!(p.is_strict_valid());
    }

    #[test]
    fn invalid_passpords() {
        let p = Passport::from("eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from("iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from("hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277");
        assert_eq!(p.is_strict_valid(), false);
        let p = Passport::from("hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007");
        assert_eq!(p.is_strict_valid(), false);
    }
}
