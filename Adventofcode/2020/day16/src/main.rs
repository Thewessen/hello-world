use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use std::convert::TryFrom;
use std::ops::RangeInclusive;
use std::num::ParseIntError;
use itertools::Itertools;

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
    let data = reader
        .lines()
        .filter_map(|line| line.ok());
    let ticket_data = TicketData::from(data);
    let result = if args.part_two {
        // input2: 3765150732757
        ticket_data
            .your_fields()
            .iter()
            .filter(|f| f.name.starts_with("departure"))
            .map(|f| f.value)
            .fold(1, |a, b| a * b)
    } else {
        // input2: 23044
        ticket_data.sum_invalid_nearby()
    };
    println!("{}", result);
    Ok(())
}

#[derive(Debug, Clone)]
struct FieldRange(RangeInclusive<u64>, RangeInclusive<u64>);

impl FieldRange {
    fn contains(&self, i: &u64) -> bool {
        self.0.contains(i) || self.1.contains(i)
    }
}

#[derive(Debug, Clone)]
struct Field {
    name: String,
    range: FieldRange,
    value: u64,
}

impl TryFrom<&str> for Field {
    type Error = ParseIntError;
    fn try_from(field: &str) -> Result<Self, Self::Error> {
        let mut name_range = field.split(": ");
        let name: String = name_range.next()
            .expect("should contain name")
            .to_string();
        let mut range1_2 = name_range.next()
            .expect("should have ranges")
            .split(" or ");
        let mut range1_bounds = range1_2.next()
            .expect("range 1 bounds")
            .split('-');
        let rang1_lb = range1_bounds.next()
            .expect("range 1 lower bound")
            .parse::<u64>()?;
        let rang1_ub = range1_bounds.next()
            .expect("range 1 upper bound")
            .parse::<u64>()?;
        let mut range2_bounds = range1_2.next()
            .expect("range 2 bounds")
            .split('-');
        let rang2_lb = range2_bounds.next()
            .expect("range 2 lower bound")
            .parse::<u64>()?;
        let rang2_ub = range2_bounds.next()
            .expect("range 2 upper bound")
            .parse::<u64>()?;
        let field = Field {
            name,
            range: FieldRange(
                rang1_lb..=rang1_ub,
                rang2_lb..=rang2_ub,
            ),
            value: 0,
        };
        Ok(field)
    }
}

struct TicketData {
    rules: Vec<Field>,
    yours: Vec<u64>,
    nearby: Vec<Vec<u64>>,
}

impl<I> From<I> for TicketData
where I: Iterator<Item = String> {
    fn from(lines: I) -> TicketData {
        let mut groups = lines
            .batching(|lines| {
                let group: Vec<String> = lines
                    .take_while(|line| !line.is_empty())
                    .collect();
                match group.is_empty() {
                    true => None,
                    false => Some(group),
                }
            });
        let rules: Vec<Field> = groups.next()
            .expect("field group")
            .iter()
            .filter_map(|field| Field::try_from(field.as_str()).ok())
            .collect();
        let yours: Vec<u64> = groups.next()
            .expect("your ticket")
            .iter()
            .skip(1)
            .next()
            .unwrap()
            .split(',')
            .filter_map(|n| n.parse::<u64>().ok())
            .collect();
        let nearby: Vec<Vec<u64>> = groups.next()
            .expect("nearby tickets")
            .iter()
            .skip(1)
            .map(|line| line
                .split(',')
                .filter_map(|n| n.parse::<u64>().ok())
                .collect::<Vec<u64>>()
            )
            .collect();
        TicketData { rules, yours, nearby }
    }
}

impl TicketData {
    fn sum_invalid_nearby(&self) -> u64 {
        self.nearby
            .iter()
            .map(|ticket| ticket.iter()
                .filter(|n| self.rules.iter().all(|rule| !rule.range.contains(n)))
                .fold(0, |a, b| a + b)
            )
            .fold(0, |a, b| a + b)
    }

    fn field_positions(&self) -> Vec<usize> {
        let mut possible: Vec<Vec<usize>> = self.rules.iter()
            .map(|_| (0..self.rules.len()).collect::<Vec<usize>>())
            .collect();
        self.nearby
            .iter()
            // filter invalid
            .filter(|numbers| numbers.iter()
                .all(|n| self.rules.iter().any(|f| f.range.contains(n)))
            )
            // reduce possibilities
            .for_each(|numbers| numbers
                .iter()
                .enumerate()
                .for_each(|(i, n)| {
                    possible[i] = possible[i]
                        .iter()
                        .filter(|j| self.rules[**j].range.contains(n))
                        .copied()
                        .collect();
                })
            );
        while !possible.iter().all(|p| p.len() == 1) {
            let taken: Vec<usize> = possible
                .iter()
                .filter(|p| p.len() == 1)
                .map(|p| p[0])
                .collect();
            possible = possible
                .iter()
                .map(|poss| {
                    if poss.len() == 1 { poss.clone() }
                    else {
                        poss.iter()
                            .filter(|p| !taken.contains(p))
                            .copied()
                            .collect()
                    }
                })
                .collect()
            ;
        }
        possible
            .iter()
            .flatten()
            .copied()
            .collect()
    }

    fn your_fields(&self) -> Vec<Field> {
        let positions = self.field_positions();
        let mut fields = Vec::with_capacity(self.rules.len());
        for i in 0..self.rules.len() {
            let mut field = self.rules[positions[i]].clone();
            field.value = self.yours[i];
            fields.push(field);
        }
        fields
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_range_inclusive() {
        let r = FieldRange(1..=3, 5..=7);
        assert!(r.contains(&3));
        assert!(r.contains(&5));
        assert!(!r.contains(&4));
    }

    #[test]
    fn test_sum_invalid_fields() {
        let data = r#"class: 1-3 or 5-7
                      row: 6-11 or 33-44
                      seat: 13-40 or 45-50

                      your ticket:
                      7,1,14

                      nearby tickets:
                      7,3,47
                      40,4,50
                      55,2,20
                      38,6,12"#
                      .split('\n')
                      .map(|line| line.trim().to_string());
        let ticket_data = TicketData::from(data);
        assert_eq!(ticket_data.sum_invalid_nearby(), 71);
    }

    #[test]
    fn test_valid_possitions() {
        let data = r#"class: 0-1 or 4-19
                      row: 0-5 or 8-19
                      seat: 0-13 or 16-19
                      
                      your ticket:
                      11,12,13
                      
                      nearby tickets:
                      3,9,18
                      15,1,5
                      5,14,9"#
                      .split('\n')
                      .map(|line| line.trim().to_string());
        let your_ticket: Vec<u64> = TicketData::from(data)
            .your_fields()
            .iter()
            .map(|f| f.value)
            .collect();
        assert_eq!(your_ticket, vec![11, 12, 13]);
    }
}

