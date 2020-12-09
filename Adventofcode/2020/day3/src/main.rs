use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;

#[derive(StructOpt, Debug)]
struct Cli {
    // Input file
    #[structopt(parse(from_os_str))]
    file: PathBuf,
    #[structopt(short = "p", long="part-two")]
    part_two: bool,
}

/// PART 1:
/// From your starting position at the top-left, check the position that is right 3 and down 1.
/// Then, check the position that is right 3 and down 1 from there, and so on until you go past the
/// bottom of the map.
///
/// The locations you'd check in the above example are marked here with O where there was an open
/// square and X where there was a tree:
///
///```
///..##.........##.........##.........##.........##.........##.......  --->
///#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
///.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
///..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
///.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
///..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
///.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
///.#........#.#........X.#........#.#........#.#........#.#........#
///#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
///#...##....##...##....##...#X....##...##....##...##....##...##....#
///.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
///```
/// In this example, traversing the map using this slope would cause you to encounter 7 trees.
fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .collect();

    let result = match args.part_two {
        false => count_from_input(&lines, &(1, 3)),
        true => [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
            .iter()
            .map(|slope| count_from_input(&lines, slope))
            .fold(1, |a, b| a * b)
    };
    println!("{}", result);
    Ok(())
}

fn count_from_input(lines: &Vec<String>, slope: &(u32, u32)) -> u64 {
    let mut x_coord: u32 = 0;
    lines
        .iter()
        .step_by(slope.0 as usize)
        .map(|line| {
            let result = line.chars().nth(x_coord as usize).unwrap() == '#';
            x_coord = (x_coord + slope.1) % (line.len() as u32); 
            result
        })
        .fold(0, |r, c| r + (c as u64))
}
