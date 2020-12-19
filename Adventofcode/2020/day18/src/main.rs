use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use itertools::{put_back, PutBack};

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
    let part_two = args.part_two;
    let data = reader
        .lines()
        .filter_map(|line| line.ok());
    // input2 (part-one): 12918250417632
    // input2 (part-two): 171259538712010
    let result = data
        .map(|line| eval(line.as_str(), part_two))
        .fold(0, |a, b| a + b);
    println!("{}", result);
    Ok(())
}

#[derive(Copy, Clone)]
enum Operation {
    Add,
    Mult,
    Noop
}

#[derive(Copy, Clone)]
struct Cache {
    calc: Operation,
    value: u64,
}

impl Default for Cache {
    fn default() -> Self {
        Cache {
            calc: Operation::Noop,
            value: 0,
        }
    }
}

impl Cache {
    fn push_val(&mut self, v: u64) {
        self.value = match self.calc {
            Operation::Add => self.value + v,
            Operation::Mult => self.value * v,
            Operation::Noop => v
        };
        self.calc = Operation::Noop;
    }

    fn calc_from(&mut self, calc: &str) {
        self.calc = match calc {
            "+" => Operation::Add,
            "*" => Operation::Mult,
            _ => self.calc
        }
    }
}

fn eval(s: &str, adv: bool) -> u64 {
    if s.is_empty() {
        return 0;
    }
    // brackets first
    let mut p = s.to_string();
    loop {
        if let Some(i) = p.chars().position(|chr| chr == '(') {
            let l = i + 1 + matching_closing_index(&p[(i + 1)..])
                .expect("closing bracket");
            p = [
                &p[..i], 
                &eval(&p[(i + 1)..l], adv).to_string(),
                &p[(l + 1)..]
            ].concat();
        } else { break; }
    }
    // calc after
    calc(&p, adv)
}

fn calc(s: &str, adv: bool) -> u64 {
    fn calc_iter<T>(iter: &mut PutBack<T>, adv: bool) -> u64
    where T: Iterator<Item = String> {
        let mut r = Cache::default();
        loop {
            match iter.next() {
                Some(s) if s.chars().all(|ch| ch.is_ascii_digit()) => {
                    let v = if let (Operation::Mult, true) = (r.calc, adv) {
                        iter.put_back(s);
                        calc_iter(iter, true)
                    } else {
                        s.parse().unwrap()
                    };
                    r.push_val(v);
                },
                Some(s) => r.calc_from(&s),
                _ => break,
            }
        };
        r.value
    }
    let mut pb = put_back(s.split(' ').map(|st| st.to_string()));
    calc_iter(&mut pb, adv)
}

fn matching_closing_index(s: &str) -> Result<usize, &str> {
    let mut count = 0;
    for (i, chr) in s.chars().enumerate() {
        match chr {
            '(' => { count += 1; }
            ')' => if count == 0 {
                return Ok(i);
            } else {
                count -= 1;
            },
            _ => (),
        }
    }
    Err("No matching parenthesis found")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_eval_calc_one() {
        let calc = "1 + (2 * 3) + (4 * (5 + 6))";
        assert_eq!(eval(calc, false), 51);
    }

    #[test]
    fn test_eval_calc_two() {
        let calc = "2 * 3 + (4 * 5)";
        assert_eq!(eval(calc, false), 26);
    }

    #[test]
    fn test_eval_calc_three() {
        let calc = "5 + (8 * 3 + 9 + 3 * 4 * 3)";
        assert_eq!(eval(calc, false), 437);
    }

    #[test]
    fn test_eval_calc_four() {
        let calc = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))";
        assert_eq!(eval(calc, false), 12_240);
    }

    #[test]
    fn test_eval_calc_five() {
        let calc = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2";
        assert_eq!(eval(calc, false), 13_632);
    }
    
    #[test]
    fn test_eval_advanced() {
        let calc = "1 + 2 * 3 + 4 * 5 + 6";
        assert_eq!(eval(calc, true), 231);
    }

    #[test]
    fn test_eval_advanced_one() {
        let calc = "1 + (2 * 3) + (4 * (5 + 6))";
        assert_eq!(eval(calc, true), 51);
    }

    #[test]
    fn test_eval_advanced_two() {
        let calc = "2 * 3 + (4 * 5)";
        assert_eq!(eval(calc, true), 46);
    }

    #[test]
    fn test_eval_advanced_three() {
        let calc = "5 + (8 * 3 + 9 + 3 * 4 * 3)";
        assert_eq!(eval(calc, true), 1_445);
    }

    #[test]
    fn test_eval_advanced_four() {
        let calc = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))";
        assert_eq!(eval(calc, true), 669_060);
    }

    #[test]
    fn test_eval_advanced_five() {
        let calc = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2";
        //         "(    (54)    *        (216)       ) + 2 + 4 * 2";
        //         "54 * 222 * 2";
        assert_eq!(eval(calc, true), 23_340);
    }

    #[test]
    fn test_eval_advanced_six() {
        let calc = "(7 * 2 + 2 + 9 + 7) * ((6 + 5) * 3) + (2 * 4 + (8 * 7 * 9 * 7) + 5 + 6 * 9) + 3 + 4 + 2";
        assert_eq!(eval(calc, true), 8_934_240);
    }

    #[test]
    fn test_eval_advanced_seven() {
        let calc = "((5 + 9) * 9) * 3 * (2 + 5 + 6)";
        assert_eq!(eval(calc, true), 4_914);
    }

    #[test]
    fn test_eval_advanced_eight() {
        let calc = "((3 * 9 + 6 * 6 + 9) + 2 * 5 + (9 + 8 + 6 * 6 + 6) * 7) * (6 + 2 + 5) + (4 * 5 + 6) * ((6 * 8 + 8 + 3) * 7 * 7 * 6 + 4) * 3 * 6";
        assert_eq!(eval(calc, true), 76_320_520_005_240);
    }

    #[test]
    fn test_eval_advanced_bug_one() {
        let calc = "(2 * 3 * 4 * 5) + 5";
        assert_eq!(eval(calc, true), 125);
    }

    #[test]
    fn test_eval_advanced_bug_two() {
        let calc = "(2 * 3) * (4 + 5) + 5";
        assert_eq!(eval(calc, true), 84);
    }

    #[test]
    fn test_eval_advanced_bug_three() {
        let calc = "((2 * 3) * (4 * 5) + 5) + 5";
        assert_eq!(eval(calc, true), 155);
    }

    #[test]
    fn test_empty() {
        let calc = "";
        assert_eq!(eval(calc, false), 0);
        assert_eq!(eval(calc, true), 0);
    }

    #[test]
    fn test_slice() {
        let calc = "((2 * 3) * (4 * 5) + 5) + 5";
        assert_eq!(eval(calc, true), 155);
    }
}
