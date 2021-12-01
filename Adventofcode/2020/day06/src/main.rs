use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
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
    let mut groups = reader.lines()
        .filter_map(|line| line.ok())
        .batching(|total| {
            let group: Vec<String> = total
                .take_while(|line| !line.is_empty())
                .collect();
            match group.is_empty() {
                true => None,
                false => Some(group),
            }
        });
    if args.part_two {
        // input2: 3356
        println!("{:?}", count_all_answered(&mut groups));
    } else {
        // input2: 6775
        println!("{:?}", count_answered(&mut groups));
    }
    Ok(())
}

fn count_answered<I>(groups: &mut I) -> u32
where I: Iterator<Item = Vec<String>> {
    groups.fold(0, |count, group| {
        count + group
            .iter()
            .join("")
            .chars()
            .unique()
            .count() as u32
    })
}

fn count_all_answered<I>(groups: &mut I) -> u32
where I: Iterator<Item = Vec<String>> {
    groups.fold(0, |count, group| {
        if group.is_empty() { count }
        else {
            let mut persons = group.iter();
            let first = persons.next().unwrap();
            count + first.chars().fold(0, |c, ans| {
                c + persons.clone()
                    .all(|answers| answers.contains(ans)) as u32
            })
        }
    })
}

trait IteratorExt: Iterator {
    fn into_groups(&mut self) -> Self;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn count_empty_lines() {
        let s = vec![vec![]];
        assert_eq!(count_answered(&mut s.iter().cloned()), 0);
    }

    #[test]
    fn count_one_group() {
        let s = vec![vec![
            "abcx".to_string(),
            "abcy".to_string(),
            "abcz".to_string()
        ]];
        assert_eq!(count_answered(&mut s.iter().cloned()), 6);
    }

    #[test]
    fn count_answered_true() {
        let s = vec![
            vec!["abc".to_string()],
            vec!["a".to_string(), "b".to_string(), "c".to_string()],
            vec!["ab".to_string(), "ac".to_string()],
            vec!["a".to_string(), "a".to_string(), "a".to_string(), "a".to_string()],
            vec!["b".to_string()]
        ];
        assert_eq!(count_answered(&mut s.iter().cloned()), 11);
    }

    #[test]
    fn count_all_one_group() {
        let s = vec![vec![
            "abcx".to_string(),
            "abcy".to_string(),
            "abcz".to_string()
        ]];
        assert_eq!(count_all_answered(&mut s.iter().cloned()), 3);
    }

    #[test]
    fn count_all_answered_true() {
        let s = vec![
            vec!["abc".to_string()],
            vec!["a".to_string(), "b".to_string(), "c".to_string()],
            vec!["ab".to_string(), "ac".to_string()],
            vec!["a".to_string(), "a".to_string(), "a".to_string(), "a".to_string()],
            vec!["b".to_string()]
        ];
        assert_eq!(count_all_answered(&mut s.iter().cloned()), 6);
    }
}
