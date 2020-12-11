use std::io::{Result};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::read_to_string;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
}

fn main() -> Result<()> {
    let args = Cli::from_args();
    let content = read_to_string(args.file)?;
    if args.part_two {
        println!("{:?}", count_all_answered(&content));
    } else {
        println!("{:?}", count_answered(&content));
    }
    Ok(())
}

fn count_answered(total: &str) -> u32 {
    total
        .split("\n\n")
        .map(|group| group
            .chars()
            .filter(|ch| ch != &'\n')
            .fold(&mut vec![], |acc, curr| {
                if !acc.contains(&curr) {
                    acc.push(curr);
                }
                acc
            })
            .len() as u32
        )
        .fold(0, |a, b| a + b)
}

fn count_all_answered(total: &str) -> u32 {
    total
        .split("\n\n")
        .map(|group| {
            let mut persons = group.split('\n').filter(|person| !person.is_empty());
            let first = persons.next().unwrap_or("");
            let rest = persons.collect::<Vec<&str>>();
            let count = first.chars().fold(0, |count, ans| {
                count + rest.iter().all(|answers| answers.contains(ans)) as u32
            });
            count
        })
        .fold(0, |a, b| a + b)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn count_empty_lines() {
        let s = "\n\n\n\n\n\n\n\n";
        assert_eq!(count_answered(s), 0);
    }

    #[test]
    fn count_one_group() {
        let s = "abcx\nabcy\nabcz";
        assert_eq!(count_answered(s), 6);
    }

    #[test]
    fn count_answered_true() {
        let s = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb";
        assert_eq!(count_answered(s), 11);
    }

    #[test]
    fn count_all_empty_lines() {
        let s = "\n\n\n\n\n\n\n\n";
        assert_eq!(count_all_answered(s), 0);
    }

    #[test]
    fn count_all_one_group() {
        let s = "abcx\nabcy\nabcz";
        assert_eq!(count_all_answered(s), 3);
    }

    #[test]
    fn count_all_answered_true() {
        let s = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb";
        assert_eq!(count_all_answered(s), 6);
    }
}
