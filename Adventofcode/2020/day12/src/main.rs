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
    waypoint: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let instructs = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .collect::<Vec<String>>();
    let mut ferry = Ferry::new();
    process_instructs(&instructs, &mut ferry, args.waypoint);
    println!("{}", ferry.calculate_distance());
    Ok(())
}

#[derive(Debug, PartialEq)]
enum Move {
    North(u32),
    South(u32),
    East(u32),
    West(u32),
    Left(u32),
    Right(u32),
    Forward(u32),
}

#[derive(Debug, PartialEq)]
enum Direction {
    North,
    South,
    East,
    West,
}
#[derive(Debug, PartialEq)]
struct Waypoint {
    x: i32,
    y: i32,
}

impl Waypoint {
    fn new() -> Self {
        Waypoint { x: 10, y: 1 }
    }

    fn move_north(&mut self, value: i32) -> () {
        self.y += value;
    }
    
    fn move_south(&mut self, value: i32) -> () {
        self.y -= value;
    }

    fn move_east(&mut self, value: i32) -> () {
        self.x += value;
    }

    fn move_west(&mut self, value: i32) -> () {
        self.x -= value;
    }
    
    fn turn(&mut self, value: i32) -> () {
        if value <= -90 {
            let mem = self.x;
            self.x = -self.y;
            self.y = mem;
            self.turn(value + 90);
        } else if value >= 90 {
            let mem = self.x;
            self.x = self.y;
            self.y = -mem;
            self.turn(value - 90);
        }
    }
}

#[derive(Debug, PartialEq)]
struct Ferry {
    facing: Direction,
    x: i32,
    y: i32,
    waypoint: Waypoint,
}


impl Ferry {
    fn new () -> Self {
        Ferry {
            x: 0, y: 0,
            facing: Direction::East,
            waypoint: Waypoint::new(),
        }
    }

    pub fn process_move(&mut self, m: Move) -> () {
        match m {
            Move::North(value) => self.move_north(value as i32),
            Move::South(value) => self.move_south(value as i32),
            Move::East(value) => self.move_east(value as i32),
            Move::West(value) => self.move_west(value as i32),
            Move::Left(value) =>  self.turn(0 - value as i32),
            Move::Right(value) => self.turn(value as i32),
            Move::Forward(value) => match self.facing {
                Direction::North => self.move_north(value as i32),
                Direction::East => self.move_east(value as i32),
                Direction::South => self.move_south(value as i32),
                Direction::West => self.move_west(value as i32),
            }
        }
    }

    pub fn process_move_waypoint(&mut self, m: Move) -> () {
        match m {
            Move::North(value) => self.waypoint.move_north(value as i32),
            Move::South(value) => self.waypoint.move_south(value as i32),
            Move::East(value) => self.waypoint.move_east(value as i32),
            Move::West(value) => self.waypoint.move_west(value as i32),
            Move::Left(value) =>  self.waypoint.turn(0 - value as i32),
            Move::Right(value) => self.waypoint.turn(value as i32),
            Move::Forward(value) => self.move_to_waypoint(value as i32)
        }
    }
    
    fn move_north(&mut self, value: i32) -> () {
        self.y += value;
    }
    
    fn move_south(&mut self, value: i32) -> () {
        self.y -= value;
    }

    fn move_east(&mut self, value: i32) -> () {
        self.x += value;
    }

    fn move_west(&mut self, value: i32) -> () {
        self.x -= value;
    }

    fn turn(&mut self, value: i32) -> () {
        if value <= -90 || 90 <= value {
            match self.facing {
                Direction::North if value < 0 => self.face(Direction::West),
                Direction::South if value > 0 => self.face(Direction::West),
                Direction::East if value < 0 => self.face(Direction::North),
                Direction::West if value > 0 => self.face(Direction::North),
                Direction::South if value < 0 => self.face(Direction::East),
                Direction::North if value > 0 => self.face(Direction::East),
                Direction::West if value < 0 => self.face(Direction::South),
                Direction::East if value > 0 => self.face(Direction::South),
                _ => (),
            };
            if value < 0 {
                self.turn(value + 90);
            } else {
                self.turn(value - 90);
            }
        }
    }
    
    fn face(&mut self, d: Direction) -> () {
        self.facing = d;
    }

    fn move_to_waypoint(&mut self, value: i32) -> () {
        self.x += self.waypoint.x * value;
        self.y += self.waypoint.y * value;
    }

    fn calculate_distance(&self) -> i32 {
        self.x.abs() + self.y.abs()
    }
}

fn move_from_str(s: &str) -> Move {
    let mut chrs = s.chars();
    match chrs.next() {
        Some('N') => Move::North(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('E') => Move::East(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('S') => Move::South(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('W') => Move::West(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('L') => Move::Left(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('R') => Move::Right(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some('F') => Move::Forward(chrs.as_str().parse::<u32>().unwrap_or(0)),
        Some(ch) => panic!("unrecognized direction {}", ch),
        None => panic!("no direction found in {}", s)
    }
}

fn process_instructs(instructs: &Vec<String>, ferry: &mut Ferry, with_waypoint: bool) -> () {
   instructs
       .iter()
       .map(|instruct| move_from_str(instruct))
       .for_each(|m| {
           if with_waypoint {
               ferry.process_move_waypoint(m);
            } else {
               ferry.process_move(m);
            }
       });
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_move_south_from_string() {
        assert_eq!(move_from_str("S4"), Move::South(4));
    }

    #[test]
    fn test_move_forward_from_string() {
        assert_eq!(move_from_str("F10"), Move::Forward(10));
    }

    #[test]
    fn test_move_ship_south() {
        let m = Move::South(10);
        let mut f = Ferry::new();
        f.process_move(m);
        assert_eq!(f, Ferry { facing: Direction::East, x: 0, y: -10, waypoint: Waypoint::new() });
    }

    #[test]
    fn test_turn_ship_right() {
        let m = Move::Right(90);
        let mut f = Ferry::new();
        f.process_move(m);
        assert_eq!(f, Ferry { facing: Direction::South, x: 0, y: 0, waypoint: Waypoint::new() });
    }

    #[test]
    fn test_turn_ship_left() {
        let m = Move::Left(360);
        let mut f = Ferry::new();
        f.process_move(m);
        assert_eq!(f, Ferry { facing: Direction::East, x: 0, y: 0, waypoint: Waypoint::new() });
    }

    #[test]
    fn test_move_ship_forward() {
        let m = Move::Forward(10);
        let mut f = Ferry::new();
        f.process_move(m);
        assert_eq!(f, Ferry { facing: Direction::East, x: 10, y: 0, waypoint: Waypoint::new() });
    }

    #[test]
    fn test_process_instructions() {
        let mut f = Ferry::new();
        let instructs = vec![
            String::from("F10"),
            String::from("N3"),
            String::from("F7"),
            String::from("R90"),
            String::from("F11")
        ];
        process_instructs(&instructs, &mut f, false);
        assert_eq!(f, Ferry { facing: Direction::South, x: 17, y: -8, waypoint: Waypoint::new() });
    }

    #[test]
    fn test_calculate_distance() {
        let f = Ferry { facing: Direction::South, x: 17, y: -8, waypoint: Waypoint::new() };
        assert_eq!(f.calculate_distance(), 25);
    }

    #[test]
    fn test_turn_hor_waypoint_right() {
        let mut w = Waypoint { x: 10, y: 0 };
        w.turn(90);
        assert_eq!(w, Waypoint { x: 0, y: -10 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: -10, y: 0 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: 0, y: 10 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: 10, y: 0 });
    }

    #[test]
    fn test_turn_dia_waypoint_right() {
        let mut w = Waypoint { x: 10, y: 1 };
        w.turn(90);
        assert_eq!(w, Waypoint { x: 1, y: -10 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: -10, y: -1 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: -1, y: 10 });
        w.turn(90);
        assert_eq!(w, Waypoint { x: 10, y: 1 });
    }

    #[test]
    fn test_turn_hor_waypoint_left() {
        let mut w = Waypoint { x: 10, y: 0 };
        w.turn(-90);
        assert_eq!(w, Waypoint { x: 0, y: 10 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: -10, y: 0 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: 0, y: -10 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: 10, y: 0 });
    }

    #[test]
    fn test_turn_dia_waypoint_left() {
        let mut w = Waypoint { x: 10, y: 10 };
        w.turn(-90);
        assert_eq!(w, Waypoint { x: -10, y: 10 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: -10, y: -10 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: 10, y: -10 });
        w.turn(-90);
        assert_eq!(w, Waypoint { x: 10, y: 10 });
    }

    #[test]
    fn test_process_instructions_with_waypoint() {
        let mut f = Ferry::new();
        let instructs = vec![
            String::from("F10"),
            String::from("N3"),
            String::from("F7"),
            String::from("R90"),
            String::from("F11")
        ];
        process_instructs(&instructs, &mut f, true);
        assert_eq!(f, Ferry { facing: Direction::East, x: 214, y: -72, waypoint: Waypoint { x: 4, y: -10 }});
    }
}
