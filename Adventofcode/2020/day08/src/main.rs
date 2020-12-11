use std::io::{self, BufRead, BufReader};
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

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let instructs = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .map(|line| Instruction::from_str(&line))
        .collect::<Vec<Instruction>>();

    if args.part_two {
        match follow_instructions_with_fix(instructs) {
            Ok(result) => println!("{}", result),
            Err(_) => panic!("no solution"),
        };
    } else {
        match follow_instructions(instructs) {
            Ok(result) | Err(result) => println!("{}", result),
        }
    }
    Ok(())
}

#[derive(Debug, PartialEq, Eq, Clone)]
struct Instruction {
    operation: String,
    value: i64,
    visited: bool,
}

// impl Copy for Instruction { }
// impl Clone for Instruction {
//     fn clone(&self) -> Instruction {
//         *self
//     }
// }

impl Instruction {
    fn new(operation: &str, value: i64) -> Self {
        Instruction { operation: operation.to_owned(), value, visited: false }
    }

    fn from_str(s: &str) -> Self {
        let mut iter = s.split(' ');
        let operation = iter.next().unwrap_or("nop");
        let value = match iter.next().unwrap_or("0").parse::<f64>() {
            Ok(n) => n as i64,
            Err(e) => panic!(e)
        };
        Instruction::new(operation, value)
    }

    pub fn done(&mut self) -> () {
        self.visited = true;
    }

    pub fn swap_operation(&mut self) -> () {
        match self.get_operation() {
            "nop" => self.operation = "jmp".to_owned(),
            "jmp" => self.operation = "nop".to_owned(),
            _ => (),
        };
    }

    pub fn get_operation(&self) -> &str {
        self.operation.as_ref()
    }
}

fn follow_instructions(mut instructs: Vec<Instruction>) -> Result<i64, i64> {
    let mut current_index: usize = 0;
    let mut result: i64 = 0;
    loop {
        match instructs.get_mut(current_index) {
            None => break Ok(result),
            Some(instruct) => {
                if instruct.visited {
                    break Err(result);
                } else {
                    match instruct.get_operation() {
                        "nop" => current_index += 1,
                        "acc" => {
                            result += instruct.value;
                            current_index += 1;
                        },
                        "jmp" => current_index = (current_index as i64 + instruct.value) as usize,
                        i => unimplemented!("{}", i),
                    }
                    instruct.done();
                }
            }
        };
    }
}
fn follow_instructions_with_fix(instructs: Vec<Instruction>) -> Result<i64, i64> {
    let mut fix = 0;
    loop {
        let poss_instructs = instructs
            .iter()
            .cloned()
            .enumerate()
            .map(|(i, mut instruct)| {
                if i == fix { instruct.swap_operation(); }
                instruct
            })
            .collect::<Vec<Instruction>>();

        match follow_instructions(poss_instructs) {
            Ok(result) => break Ok(result),
            Err(_) => match instructs
                .iter()
                .enumerate()
                .skip_while(|(i, instruct)| {
                    i <= &fix || (
                        instruct.get_operation() != "jmp" &&
                        instruct.get_operation() != "nop"
                    )
                })
                .next() {
                    Some((i, _)) => fix = i,
                    None => break Err(0),
                },
        };
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_instruction_from_str_acc_poss() {
        let i = Instruction {
            operation: String::from("acc"),
            value: 3,
            visited: false
        };
        assert_eq!(Instruction::from_str("acc +3"), i);
    }

    #[test]
    fn test_instruction_from_str_acc_neg() {
        let i = Instruction {
            operation: String::from("acc"),
            value: -5,
            visited: false
        };
        assert_eq!(Instruction::from_str("acc -5"), i);
    }

    #[test]
    fn test_follow_one_instruction() {
        let instruct = Instruction::new("acc", 3);
        assert_eq!(follow_instructions(vec![instruct]), Ok(3));
    }

    #[test]
    fn test_follow_instructions_with_jump() {
        assert_eq!(follow_instructions(vec![
            Instruction::new("nop", 0),
            Instruction::new("acc", 3),
            Instruction::new("jmp", -2)
        ]), Err(3));
    }

    #[test]
    fn test_follow_real_instructions() {
        assert_eq!(follow_instructions(vec![
            Instruction::new("nop", 0),
            Instruction::new("acc", 1),
            Instruction::new("jmp", 4),
            Instruction::new("acc", 3),
            Instruction::new("jmp", -3),
            Instruction::new("acc", -99),
            Instruction::new("acc", 1),
            Instruction::new("jmp", -4),
            Instruction::new("acc", 6)
        ]), Err(5));
    }

    #[test]
    fn test_follow_instruction_should_fix() {
        assert_eq!(follow_instructions_with_fix(vec![
            Instruction::new("jmp", 0),
            Instruction::new("acc", 1)
        ]), Ok(1));
    }

    #[test]
    fn test_follow_real_instructions_should_fix() {
        assert_eq!(follow_instructions_with_fix(vec![
            Instruction::new("nop", 0),
            Instruction::new("acc", 1),
            Instruction::new("jmp", 4),
            Instruction::new("acc", 3),
            Instruction::new("jmp", -3),
            Instruction::new("acc", -99),
            Instruction::new("acc", 1),
            Instruction::new("jmp", -4),
            Instruction::new("acc", 6)
        ]), Ok(8));
    }
}
