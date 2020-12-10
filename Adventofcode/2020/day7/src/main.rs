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

/// PART 1:
fn main() -> Result<()> {
    let args = Cli::from_args();
    let content = read_to_string(args.file)?;
    Ok(())
}

fn count_colors(rules: &str, colors: Vec<&str>, depth: u32) -> u32 {
    if depth == 0 {
        colors
    } else {
        colors.append(rules.split('\n')
        .filter(|rule| !rule.is_empty())
        .filter(|rule| {
            if colors.is_empty() {
                !rule.starts_with("shiny gold") && rule.contains("shiny gold")
            } else {
                colors.iter().some(|color| {
                    !rule.starts_with(color) && rule.contains(color)
                })
            }
        })
        .collect::<Vec<&str>>();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn number_of_colors() {
        let rules = r#"
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
        "#;
        assert_eq!(count_colors(rules, vec![], 2), 4);
    }
}
