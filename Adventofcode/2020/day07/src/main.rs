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

fn main() -> Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let rules = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|rule| !rule.is_empty())
        .collect::<Vec<String>>();
    if args.part_two {
        println!("{:?}", count_bags("shiny gold", &rules));
    } else {
        println!("{:?}", unique(possible_colors(vec![], &rules)).len());
    }
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

fn unique(s: Vec<String>) -> Vec<String> {
    s.iter()
     .cloned()
     .fold(vec![], |mut acc, curr| {
         if !acc.contains(&curr) { acc.push(curr); }
         acc
     })
}

fn count_bags(color: &str, rules: &Vec<String>) -> u64 {
    if color.is_empty() {
        0
    } else {
        let rule = rules
            .iter()
            .find(|rule| rule.starts_with(color)).unwrap();

        parse_rule(rule)
            .iter()
            .fold(0, |count, (quant, color)| {
                count + quant + quant * count_bags(color, rules)
            })
    }
}

fn parse_rule(rule: &str) -> Vec<(u64, String)> {
    rule.split(' ')
        .skip_while(|word| word != &"contain")
        .skip(1)
        .fold(vec![], |mut quant, word| {
            if word != "bag," && word != "bags," && word != "bag." && word != "bags." {
                match word.parse::<f64>() {
                    Ok(n) => quant.push((n as u64, String::new())),
                    Err(_) => {
                        if word == "no" {
                            quant.push((0, String::new()));
                        } else if word != "other" {
                            let l = quant.len() - 1;
                            let last = &quant[l];
                            quant[l] = (last.0, (last.1.to_string() + " " + word).trim().to_string());
                        }
                    }
                }
            }
            quant
        })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_unique() {
        let v = vec![String::from("a"), String::from("b"), String::from("c")];
        assert_eq!(unique(v.clone()), v);
        let o = vec![String::from("a"); 5];
        assert_eq!(unique(o.clone()), vec![String::from("a")]);
    }

    #[test]
    fn test_rule_to_bag() {
        let s = String::from("light red bags contain 1 bright white bag, 2 muted yellow bags.");
        assert_eq!(rule_to_bag(&s), "light red");
    }

    #[test]
    fn test_parse_rule() {
        let s = String::from("bright white bags contain 1 shiny gold bag.");
        assert_eq!(parse_rule(&s), vec![(1, String::from("shiny gold"))]);
        let s = String::from("light red bags contain 1 bright white bag, 2 muted yellow bags.");
        assert_eq!(parse_rule(&s), vec![(1, String::from("bright white")), (2, String::from("muted yellow"))]);
        let s = String::from("wavy olive bags contain 5 mirrored tan bags, 5 vibrant lime bags, 3 dull lime bags, 5 dim lime bags.");
        assert_eq!(parse_rule(&s), vec![
            (5, String::from("mirrored tan")),
            (5, String::from("vibrant lime")),
            (3, String::from("dull lime")),
            (5, String::from("dim lime"))
        ]);
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

    #[test]
    fn test_other_bags_count_simple() {
        let rules = vec![
            String::from("shiny gold bags contain 2 dark red bags."),
            String::from("dark red bags contain no other bags.")
        ];
        assert_eq!(count_bags("shiny gold", &rules), 2);
    }

    #[test]
    fn test_other_bags_count() {
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
        assert_eq!(count_bags("shiny gold", &rules), 32);
    }

    #[test]
    fn test_more_bags_count() {
        let rules = vec![
            String::from("shiny gold bags contain 2 dark red bags."),
            String::from("dark red bags contain 2 dark orange bags."),
            String::from("dark orange bags contain 2 dark yellow bags."),
            String::from("dark yellow bags contain 2 dark green bags."),
            String::from("dark green bags contain 2 dark blue bags."),
            String::from("dark blue bags contain 2 dark violet bags."),
            String::from("dark violet bags contain no other bags.")
        ];

        assert_eq!(count_bags("shiny gold", &rules), 126);
    }
}
