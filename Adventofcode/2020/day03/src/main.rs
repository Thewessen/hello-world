use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;

#[derive(StructOpt, Debug)]
struct Cli {
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long="part-two")]
    part_two: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines()
        .filter_map(|line| line.ok())
        .collect();

    let result = match args.part_two {
        false => count_trees(&lines, &(1, 3)),
        true => [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
            .iter()
            .map(|slope| count_trees(&lines, slope))
            .fold(1, |a, b| a * b)
    };
    println!("{}", result);
    Ok(())
}

fn count_trees(lines: &Vec<String>, slope: &(usize, usize)) -> u64 {
    let mut x_coord: usize = 0;
    let (dy, dx) = slope;
    lines
        .iter()
        .step_by(*dy)
        .filter_map(|line| {
            let result = line.chars().nth(x_coord);
            x_coord = (x_coord + dx) % line.len(); 
            match result {
                Some('#') => Some('#'),
                _ => None,
            }
        })
        .count() as u64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_trees_default_slope_two() {
        let lines = vec![
            String::from("..##......."),
            String::from("#...#...#.."),
            String::from(".#....#..#."),
            String::from("..#.#...#.#"),
            String::from(".#...##..#."),
            String::from("..#.##....."),
            String::from(".#.#.#....#"),
            String::from(".#........#"),
            String::from("#.##...#..."),
            String::from("#...##....#"),
            String::from(".#..#...#.#")
        ];
        assert_eq!(count_trees(&lines, &(1, 3)), 7);
    }

    #[test]
    fn test_count_trees_slope_one() {
        let lines = vec![
            String::from("..##......."),
            String::from("#...#...#.."),
            String::from(".#....#..#."),
            String::from("..#.#...#.#"),
            String::from(".#...##..#."),
            String::from("..#.##....."),
            String::from(".#.#.#....#"),
            String::from(".#........#"),
            String::from("#.##...#..."),
            String::from("#...##....#"),
            String::from(".#..#...#.#")
        ];
        assert_eq!(count_trees(&lines, &(1, 1)), 2);
    }

    #[test]
    fn test_count_trees_slope_three() {
        let lines = vec![
            String::from("..##......."),
            String::from("#...#...#.."),
            String::from(".#....#..#."),
            String::from("..#.#...#.#"),
            String::from(".#...##..#."),
            String::from("..#.##....."),
            String::from(".#.#.#....#"),
            String::from(".#........#"),
            String::from("#.##...#..."),
            String::from("#...##....#"),
            String::from(".#..#...#.#")
        ];
        assert_eq!(count_trees(&lines, &(1, 5)), 3);
    }

    #[test]
    fn test_count_trees_slope_four() {
        let lines = vec![
            String::from("..##......."),
            String::from("#...#...#.."),
            String::from(".#....#..#."),
            String::from("..#.#...#.#"),
            String::from(".#...##..#."),
            String::from("..#.##....."),
            String::from(".#.#.#....#"),
            String::from(".#........#"),
            String::from("#.##...#..."),
            String::from("#...##....#"),
            String::from(".#..#...#.#")
        ];
        assert_eq!(count_trees(&lines, &(1, 7)), 4);
    }

    #[test]
    fn test_count_trees_slope_five() {
        let lines = vec![
            String::from("..##......."),
            String::from("#...#...#.."),
            String::from(".#....#..#."),
            String::from("..#.#...#.#"),
            String::from(".#...##..#."),
            String::from("..#.##....."),
            String::from(".#.#.#....#"),
            String::from(".#........#"),
            String::from("#.##...#..."),
            String::from("#...##....#"),
            String::from(".#..#...#.#")
        ];
        assert_eq!(count_trees(&lines, &(2, 1)), 2);
    }
}
