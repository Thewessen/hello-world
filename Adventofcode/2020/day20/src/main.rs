use std::io::{self, BufRead, BufReader};
use std::path::PathBuf;
use structopt::StructOpt;
use std::fs::File;
use itertools::Itertools;

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
    let data = reader
        .lines()
        .filter_map(|line| line.ok());
    let result = if args.part_two {
        unimplemented!();
    } else {
        unimplemented!();
    };
    // println!("{}", result);
    Ok(())
}

struct Tile {
    id: u64,
    tile: Vec<String>,
}

impl Tile {
    fn rotate(&mut self) {
        let mut new_tile: Vec<String> = self.tile[0].chars().map(|chr| chr.to_string()).collect();
        for row in self.tile[1..].iter() {
            new_tile = new_tile.iter()
                .zip(row.chars())
                .map(|(row, chr)| [chr.to_string(), row.to_string()].concat())
                .collect();
        }
        self.tile = new_tile;
    }

    fn flip_hor(&mut self) {
        self.tile = self.tile.iter().rev().cloned().collect();
    }

    fn flip_ver(&mut self) {
        self.tile = self.tile.iter()
            .map(|row| row.chars().rev().collect())
            .collect();
    }

    fn borders(&self) -> Vec<String> {
        vec![
            self.tile[0].clone(),
            self.tile.iter().last().unwrap().clone(),
            self.tile.iter().map(|row| row.chars().next().unwrap()).collect(),
            self.tile.iter().map(|row| row.chars().last().unwrap()).collect(),
        ]
    }

    fn matches(&self, other: &Self) -> bool {
        self.borders().iter().any(|border| {
            other.borders().iter().any(|ob| {
                ob == border || ob.to_string() == border.chars().rev().collect::<String>()
            })
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rotate_tile() {
        let mut tile = Tile {
            id: 0,
            tile: vec![
                "..##.#..#.".to_string(),
                "##..#.....".to_string(),
                "#...##..#.".to_string(),
                "####.#...#".to_string(),
                "##.##.###.".to_string(),
                "##...#.###".to_string(),
                ".#.#.#..##".to_string(),
                "..#....#..".to_string(),
                "###...#.#.".to_string(),
                "..###..###".to_string(),
            ]
        };
        tile.rotate();
        assert_eq!(tile.tile, vec![
            ".#..#####.".to_string(),
            ".#.####.#.".to_string(),
            "###...#..#".to_string(),
            "#..#.##..#".to_string(),
            "#....#.##.".to_string(),
            "...##.##.#".to_string(),
            ".#...#....".to_string(),
            "#.#.##....".to_string(),
            "##.###.#.#".to_string(),
            "#..##.#...".to_string(),
        ])
    }

    #[test]
    fn test_flip_hor() {
        let mut tile = Tile {
            id: 0,
            tile: vec![
                "..##.#..#.".to_string(),
                "##..#.....".to_string(),
                "#...##..#.".to_string(),
                "####.#...#".to_string(),
                "##.##.###.".to_string(),
                "##...#.###".to_string(),
                ".#.#.#..##".to_string(),
                "..#....#..".to_string(),
                "###...#.#.".to_string(),
                "..###..###".to_string(),
            ]
        };
        tile.flip_hor();
        assert_eq!(tile.tile, vec![
            "..###..###".to_string(),
            "###...#.#.".to_string(),
            "..#....#..".to_string(),
            ".#.#.#..##".to_string(),
            "##...#.###".to_string(),
            "##.##.###.".to_string(),
            "####.#...#".to_string(),
            "#...##..#.".to_string(),
            "##..#.....".to_string(),
            "..##.#..#.".to_string(),
        ]);
    }

    #[test]
    fn test_flip_ver() {
        let mut tile = Tile {
            id: 0,
            tile: vec![
                "..###..###".to_string(),
                "###...#.#.".to_string(),
                "..#....#..".to_string(),
                ".#.#.#..##".to_string(),
                "##...#.###".to_string(),
                "##.##.###.".to_string(),
                "####.#...#".to_string(),
                "#...##..#.".to_string(),
                "##..#.....".to_string(),
                "..##.#..#.".to_string(),
            ]
        };
        tile.flip_ver();
        assert_eq!(tile.tile, vec![
            "###..###..".to_string(),
            ".#.#...###".to_string(),
            "..#....#..".to_string(),
            "##..#.#.#.".to_string(),
            "###.#...##".to_string(),
            ".###.##.##".to_string(),
            "#...#.####".to_string(),
            ".#..##...#".to_string(),
            ".....#..##".to_string(),
            ".#..#.##..".to_string(),
        ]);
    }

    #[test]
    fn test_borders_tile() {
        let tile = Tile {
            id: 0,
            tile: vec![
                "..###..###".to_string(),
                "###...#.#.".to_string(),
                "..#....#..".to_string(),
                ".#.#.#..##".to_string(),
                "##...#.###".to_string(),
                "##.##.###.".to_string(),
                "####.#...#".to_string(),
                "#...##..#.".to_string(),
                "##..#.....".to_string(),
                "..##.#..#.".to_string(),
            ]
        };
        assert_eq!(tile.borders(), vec![
            "..###..###".to_string(),
            "..##.#..#.".to_string(),
            ".#..#####.".to_string(),
            "#..##.#...".to_string(),
        ]);
    }

    #[test]
    fn test_matching_tile() {
        let tile1 = Tile {
            id: 0,
            tile: vec![
                "..##.#..#.".to_string(),
                "##..#.....".to_string(),
                "#...##..#.".to_string(),
                "####.#...#".to_string(),
                "##.##.###.".to_string(),
                "##...#.###".to_string(),
                ".#.#.#..##".to_string(),
                "..#....#..".to_string(),
                "###...#.#.".to_string(),
                "..###..###".to_string(),
            ]
        };
        let tile2 = Tile {
            id: 1,
            tile: vec![
                ".#..#####.".to_string(),
                ".#.####.#.".to_string(),
                "###...#..#".to_string(),
                "#..#.##..#".to_string(),
                "#....#.##.".to_string(),
                "...##.##.#".to_string(),
                ".#...#....".to_string(),
                "#.#.##....".to_string(),
                "##.###.#.#".to_string(),
                "#..##.#...".to_string(),
            ]
        };
        assert!(tile1.matches(&tile2))
    }

}
