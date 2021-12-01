use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use std::collections::{HashMap, HashSet};

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
    let data: Vec<String> = reader
        .lines()
        .filter_map(|line| line.ok())
        .collect();
    let input: Vec<String> = data
        .iter()
        .skip_while(|line| !line.is_empty())
        .skip(1)
        .cloned()
        .collect();
    let result = if args.part_two {
        let mut rules = data
            .iter()
            .take_while(|line| !line.is_empty())
            .map(|line| {
                if line.starts_with("8:") {
                    // "8: 42 | 42 8".to_string()
                    "8: 42 | 42 42 | 42 42 42".to_string()
                } else if line.starts_with("11:") {
                    "11: 42 31 | 42 42 31 31 | 42 42 42 31 31 31".to_string()
                    // "11: 42 31 | 42 11 31".to_string()
                } else {
                    line.to_string()
                }
            });
        // input2:
        Data::from(&mut rules, input)
            .calc_valid()
    } else {
        let mut rules = data
            .iter()
            .take_while(|line| !line.is_empty())
            .cloned();
        // input2: 184
        Data::from(&mut rules, input)
            .calc_valid()
    };
    println!("{}", result);
    Ok(())
}

type Rules = HashMap<usize, String>;
type Cache = HashMap<usize, HashSet<String>>;

struct Data {
    rules: Rules,
    input: Vec<String>,
}

impl Data {
    fn from<T>(rules: &mut T, input: Vec<String>) -> Self
    where T: Iterator<Item = String> {
        Data {
            rules: create_rules(rules),
            input,
        }
    }

    fn calc_valid(&self) -> usize {
        let (valid, _) = self.sep_valid();
        valid.len()
    }

    fn sep_valid(&self) -> (Vec<String>, Vec<String>) {
        let poss = strings_from_rules(0, &self.rules, &mut HashMap::new());
        self.input
            .iter()
            .cloned()
            .partition(|line| poss.contains(line))
    }
}

fn create_rules<T>(lines: &mut T) -> Rules
where T: Iterator<Item = String> {
    lines
        .map(|line| {
            let mut iter = line.split(": ");
            let n: usize = iter.next().unwrap().parse()
                .expect("rule number");
            let rule = iter.next()
                .expect("rule");
            if rule.starts_with("\"") && rule.ends_with("\"") {
                (n, rule[1..(rule.len() - 1)].to_string())
            } else {
                (n, rule.to_string())
            }
        })
        .collect()
}

fn strings_from_rules(n: usize, rules: &Rules, cache: &mut Cache) -> HashSet<String> {
    if cache.contains_key(&n) {
        return cache[&n].clone();
    }
    let mut poss = HashSet::new();
    let rule = rules.get(&n).expect("rule");
    for or in rule.split(" | ") {
        let mut p = HashSet::new();
        for and in or.split(' ') {
            if and.chars().all(|chr| chr.is_ascii_alphabetic()) {
                p.insert(and.to_string());
            } else {
                let nr = and.parse::<usize>().expect("rule number");
                if p.is_empty() {
                    p = strings_from_rules(nr, rules, cache);
                } else {
                    p = p.iter()
                        .flat_map(|pref|
                            strings_from_rules(nr, rules, cache)
                                .iter()
                                .map(|s| [pref.clone(), s.to_string()].concat())
                                .collect::<HashSet<String>>()
                        )
                        .collect();
                }
            }
        }
        poss.extend(p);
    }
    cache.insert(n, poss.clone());
    poss
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_create_rules() {
        let input = vec![
            "0: 4 1 5",
            "1: 2 3 | 3 2",
            "2: 4 4 | 5 5",
            "3: 4 5 | 5 4",
            "4: \"a\"",
            "5: \"b\""
        ];
        let mut lines = input.iter().map(|line| line.to_string());
        let rules = create_rules(&mut lines);
        assert_eq!(rules.len(), 6);
        assert_eq!(rules.get(&0), Some(&"4 1 5".to_string()));
        assert_eq!(rules.get(&1), Some(&"2 3 | 3 2".to_string()));
        assert_eq!(rules.get(&2), Some(&"4 4 | 5 5".to_string()));
        assert_eq!(rules.get(&3), Some(&"4 5 | 5 4".to_string()));
        assert_eq!(rules.get(&4), Some(&"a".to_string()));
        assert_eq!(rules.get(&5), Some(&"b".to_string()));
    }

    #[test]
    fn test_strings_from_rules_one() {
        let input = vec![
            "0: 1 2",
            "1: \"a\"",
            "2: 1 3 | 3 1",
            "3: \"b\"",
        ];
        let mut lines = input.iter().map(|line| line.to_string());
        let rules = create_rules(&mut lines);
        assert_eq!(strings_from_rules(0, &rules, &mut HashMap::new()), [
            "aab".to_string(),
            "aba".to_string(),
        ].iter().cloned().collect());
    }

    #[test]
    fn test_strings_from_rules_two() {
        let input = vec![
            "0: 4 1 5",
            "1: 2 3 | 3 2",
            "2: 4 4 | 5 5",
            "3: 4 5 | 5 4",
            "4: \"a\"",
            "5: \"b\""
        ];
        let mut lines = input.iter().map(|line| line.to_string());
        let rules = create_rules(&mut lines);
        assert_eq!(strings_from_rules(0, &rules, &mut HashMap::new()), [
            "aaaabb".to_string(),
            "aaabab".to_string(),
            "abbabb".to_string(),
            "abbbab".to_string(),
            "aabaab".to_string(),
            "aabbbb".to_string(),
            "abaaab".to_string(),
            "ababbb".to_string()
        ].iter().cloned().collect());
    }
}
