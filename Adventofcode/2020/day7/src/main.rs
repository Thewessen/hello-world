use std::io::{Result, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
}

/// PART 1:
/// You land at the regional airport in time for your next flight. In fact, it looks like you'll
/// even have time to grab some food: all flights are currently delayed due to issues in luggage
/// processing.
///
/// Due to recent aviation regulations, many rules (your puzzle input) are being enforced about
/// bags and their contents; bags must be color-coded and must contain specific quantities of other
/// color-coded bags. Apparently, nobody responsible for these regulations considered how long they
/// would take to enforce!
fn main() -> Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let rules = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|rule| !rule.is_empty())
        .collect::<Vec<String>>();
    let possible = possible_colors(vec![], &rules);
    possible.iter().for_each(|color| println!("{}", color));
    println!("{:?}", possible_colors(vec![], &rules).len());
    Ok(())
}

fn possible_colors(mut colors: Vec<String>, rules: &Vec<String>) -> Vec<String> {
    let new_colors = rules.iter()
        .filter(|rule| {
            if colors.is_empty() {
                !rule.starts_with("shiny gold") && rule.contains("shiny gold")
            } else {
                colors.iter().any(|color| {
                    !rule.starts_with(color) && rule.contains(color)
                })
            }
        })
        .map(rule_to_bag)
        .fold(vec![], |mut new, color| {
            if !colors.contains(&color) {
                new.push(color);
            }
            new
        });
    if !new_colors.is_empty() {
        colors.append(&mut possible_colors(new_colors, rules));
    }
    colors
}

fn rule_to_bag(rule: &String) -> String {
    rule.split(' ')
        .take(2)
        .fold(String::new(), |a, b| a + " " + &b)
        .trim()
        .to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rule_to_bag() {
        let s = String::from("light red bags contain 1 bright white bag, 2 muted yellow bags.");
        assert_eq!(rule_to_bag(&s), "light red");
    }

    #[test]
    fn test_possible_colors() {
        let rules = vec![
            String::from("light red bags contain 1 bright white bag, 2 muted yellow bags."),
            String::from("dark orange bags contain 3 bright white bags, 4 muted yellow bags."),
            String::from("bright white bags contain 1 shiny gold bag."),
            String::from("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."),
            String::from("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags."),
            String::from("dark olive bags contain 3 faded blue bags, 4 dotted black bags."),
            String::from("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."),
            String::from("faded blue bags contain no other bags."),
            String::from("dotted black bags contain no other bags.")
        ];
        assert_eq!(possible_colors(vec![], &rules).len(), 4);
    }
}
