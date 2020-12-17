use std::io::{self};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::read_to_string;
use itertools::Itertools;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long = "part-two")]
    part_two: bool,
    #[structopt(short = "N", long = "dimension", default_value = "0")]
    n: usize,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let space = read_to_string(args.file)?;
    let result = if args.n != 0 {
        Space::from(space.as_str(), args.n)
            .nth(5)
            .expect("6th cycle")
            .active()
    } else if args.part_two {
        // input2: 1980
        Space::from(space.as_str(), 4)
            .nth(5)
            .expect("6th cycle")
            .active()
    } else {
        // input2: 362
        Space::from(space.as_str(), 3)
            .nth(5)
            .expect("6th cycle")
            .active()
    };
    println!("{}", result);
    Ok(())
}

type Coords = Vec<Vec<isize>>;

struct Space(Coords);

impl Iterator for Space {
    type Item = Self;

    fn next(&mut self) -> Option<Self> {
        let d = self.dimension();
        let new_space = self.0.iter()
            .fold(vec![-1..=1; d], |acc, coords| {
                acc.iter()
                    .enumerate()
                    .map(|(i, r)| {
                        let lb = if &coords[i] <= r.start() { coords[i] - 1 } else { *r.start() };
                        let ub = if &coords[i] >= r.end() { coords[i] + 1 } else { *r.end() };
                        lb..=ub
                    })
                    .collect()
            });

        let deltas: Coords = (0..d)
            .map(|_| -1..=1)
            .multi_cartesian_product()
            .filter(|p| p != &vec![0; d])
            .collect();

        self.0 = new_space
            .into_iter()
            .multi_cartesian_product()
            .fold(vec![], |mut acc, coords| {
                let count = deltas.iter()
                    .fold(0, |c, delta| {
                        let neighbor: Vec<isize> = coords.iter()
                            .zip(delta.iter())
                            .map(|(a, b)| a + b)
                            .collect();
                        c + self.0.contains(&neighbor) as isize
                    });
                match count {
                    3 => acc.push(coords.clone()),
                    2 if self.0.contains(&coords) => acc.push(coords.clone()),
                    _ => (),
                };
                acc
            });
    
        Some(Space(self.0.clone()))
    }
}

impl Space {
    fn active(&self) -> usize {
        self.0.len()
    }
     
    fn dimension(&self) -> usize {
        match self.0.iter().next() {
            Some(coords) => coords.len(),
            None => 0
        }
    }

    fn from(space: &str, dimension: usize) -> Self {
        let mut coords: Coords = vec![];
        for (y, line) in space.split('\n').enumerate() {
            for (x, ch) in line.chars().enumerate() {
                match ch {
                    '#' => {
                        let mut coord = vec![x as isize, y as isize];
                        coord.append(&mut vec![0; dimension - 2]);
                        coords.push(coord);
                    }
                    _ => ()
                }
            }
        }
        Space(coords)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_into_coords() {
        let space = Space::from(".#.\n..#\n###", 3);
        assert_eq!(space.0, vec![
            vec![1, 0, 0],
            vec![2, 1, 0],
            vec![0, 2, 0],
            vec![1, 2, 0],
            vec![2, 2, 0],
        ]);
    }

    #[test]
    fn test_cycle_one() {
        let mut space = Space::from(".#.\n..#\n###", 3);
        assert_eq!(space.next().unwrap().0, vec![
            vec![0, 1, -1],
            vec![0, 1, 0],
            vec![0, 1, 1],
            vec![1, 2, 0],
            vec![1, 3, -1],
            vec![1, 3, 0],
            vec![1, 3, 1],
            vec![2, 1, 0],
            vec![2, 2, -1],
            vec![2, 2, 0],
            vec![2, 2, 1],
        ])
    }

    #[test]
    fn test_active_coords() {
        let mut space = Space::from(".#.\n..#\n###", 3);
        assert_eq!(space.next().unwrap().active(), 11);
    }

    #[test]
    fn test_full_cycle() {
        let mut space = Space::from(".#.\n..#\n###", 3);
        assert_eq!(space.nth(5).unwrap().active(), 112);
    }

    #[test]
    fn test_full_cycle_part_two() {
        let mut space = Space::from(".#.\n..#\n###", 4);
        assert_eq!(space.nth(5).unwrap().active(), 848);
    }
}
