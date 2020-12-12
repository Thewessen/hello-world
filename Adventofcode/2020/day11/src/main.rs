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
    new_rules: bool,
}

fn main() -> io::Result<()> {
    let args = Cli::from_args();
    let file = File::open(args.file)?;
    let reader = BufReader::new(file);
    let seats = reader
        .lines()
        .map(|line| line.unwrap_or(String::new()))
        .filter(|line| !line.is_empty())
        .collect::<Vec<String>>();

    let result = stable_free(&seats, &args.new_rules);
    println!("{}", result);

    Ok(())
}

fn evolve(seats: &Vec<String>, new_rules: &bool) -> Vec<String> {
    let mut new_seats = vec![String::with_capacity(seats[0].len()); seats.len()];
    let limit = if *new_rules { 5 } else { 4 };
    for (y, row) in seats.iter().enumerate() {
        for (x, seat) in row.chars().enumerate() {
            match seat {
                'L' if count_surrounding(&seats, (x, y), new_rules) == 0 => {
                    new_seats[y] += "#"
                },
                '#' if count_surrounding(&seats, (x, y), new_rules) >= limit => {
                    new_seats[y] += "L"
                },
                seat => new_seats[y] += &seat.to_string(),
            }
        }
    }
    new_seats
}

fn count_surrounding(seats: &Vec<String>, position: (usize,usize), new_rules: &bool) -> u8 {
    let deltas: Vec::<(i32, i32)> = vec![
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
    ];

    let (x, y) = position;
    let mut count: u8 = 0;
    for (dx, dy) in deltas.iter() {
        let (mut di, mut dj) = (dx.to_owned(), dy.to_owned());
        count += loop {
            if x as i32 + di < 0 || y as i32 + dj < 0 { break 0; }
            match seats.get((y as i32 + dj) as usize) {
                None => break 0,
                Some(row) => match row.chars().nth((x as i32 + di) as usize) {
                    Some('#') => break 1,
                    Some('.') if *new_rules => {
                        di += dx;
                        dj += dy;
                    }
                    _ => break 0,
                }
            }
        }
    }
    count
}

fn count_free(seats: &Vec<String>) -> u32 {
    seats.iter()
         .fold(0, |count, row| {
             count + row.chars()
                .fold(0, |c, seat| {
                    match seat {
                        '#' => c + 1,
                        _   => c
                    }
                })
         })
}

fn stable_free(seats: &Vec<String>, new_rules: &bool) -> u32 {
    let mut s = seats.clone();
    loop {
        let new_seats = evolve(&s, new_rules);
        if new_seats == s {
            break count_free(&new_seats);
        }
        s = new_seats;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_surrounding() {
        let seats = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.#.L..#.."),
            String::from("#L##.##.L#"),
            String::from("#.#L.LL.LL"),
            String::from("#.#L#L#.##"),
            String::from("..L.L....."),
            String::from("#L#L##L#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        assert_eq!(count_surrounding(&seats, (0, 0), &false), 1);
        assert_eq!(count_surrounding(&seats, (9, 9), &false), 1);
        assert_eq!(count_surrounding(&seats, (3, 3), &false), 3);

        assert_eq!(count_surrounding(&seats, (0, 0), &true), 2);
        assert_eq!(count_surrounding(&seats, (9, 9), &true), 2);
        assert_eq!(count_surrounding(&seats, (3, 3), &true), 4);
    }

    #[test]
    fn test_first_generation_seats() {
        let init = vec![
            String::from("L.LL.LL.LL"),
            String::from("LLLLLLL.LL"),
            String::from("L.L.L..L.."),
            String::from("LLLL.LL.LL"),
            String::from("L.LL.LL.LL"),
            String::from("L.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLLL"),
            String::from("L.LLLLLL.L"),
            String::from("L.LLLLL.LL"),
        ];

        let next = vec![
            String::from("#.##.##.##"),
            String::from("#######.##"),
            String::from("#.#.#..#.."),
            String::from("####.##.##"),
            String::from("#.##.##.##"),
            String::from("#.#####.##"),
            String::from("..#.#....."),
            String::from("##########"),
            String::from("#.######.#"),
            String::from("#.#####.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
        assert_eq!(evolve(&init, &true), next);
    }

    #[test]
    fn test_second_generation_seats() {
        let init = vec![
            String::from("#.##.##.##"),
            String::from("#######.##"),
            String::from("#.#.#..#.."),
            String::from("####.##.##"),
            String::from("#.##.##.##"),
            String::from("#.#####.##"),
            String::from("..#.#....."),
            String::from("##########"),
            String::from("#.######.#"),
            String::from("#.#####.##"),
        ];

        let next = vec![
            String::from("#.LL.L#.##"),
            String::from("#LLLLLL.L#"),
            String::from("L.L.L..L.."),
            String::from("#LLL.LL.L#"),
            String::from("#.LL.LL.LL"),
            String::from("#.LLLL#.##"),
            String::from("..L.L....."),
            String::from("#LLLLLLLL#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#LLLL.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
    }

    #[test]
    fn test_third_generation_seats() {
        let init = vec![
            String::from("#.LL.L#.##"),
            String::from("#LLLLLL.L#"),
            String::from("L.L.L..L.."),
            String::from("#LLL.LL.L#"),
            String::from("#.LL.LL.LL"),
            String::from("#.LLLL#.##"),
            String::from("..L.L....."),
            String::from("#LLLLLLLL#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#LLLL.##"),
        ];
        
        let next = vec![
            String::from("#.##.L#.##"),
            String::from("#L###LL.L#"),
            String::from("L.#.#..#.."),
            String::from("#L##.##.L#"),
            String::from("#.##.LL.LL"),
            String::from("#.###L#.##"),
            String::from("..#.#....."),
            String::from("#L######L#"),
            String::from("#.LL###L.L"),
            String::from("#.#L###.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
    }

    #[test]
    fn test_fourth_generation_seats() {
        let init = vec![
            String::from("#.##.L#.##"),
            String::from("#L###LL.L#"),
            String::from("L.#.#..#.."),
            String::from("#L##.##.L#"),
            String::from("#.##.LL.LL"),
            String::from("#.###L#.##"),
            String::from("..#.#....."),
            String::from("#L######L#"),
            String::from("#.LL###L.L"),
            String::from("#.#L###.##"),
        ];

        let next = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.L.L..#.."),
            String::from("#LLL.##.L#"),
            String::from("#.LL.LL.LL"),
            String::from("#.LL#L#.##"),
            String::from("..L.L....."),
            String::from("#L#LLLL#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
    }

    #[test]
    fn test_fifth_generation_seats() {
        let init = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.L.L..#.."),
            String::from("#LLL.##.L#"),
            String::from("#.LL.LL.LL"),
            String::from("#.LL#L#.##"),
            String::from("..L.L....."),
            String::from("#L#LLLL#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        let next = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.#.L..#.."),
            String::from("#L##.##.L#"),
            String::from("#.#L.LL.LL"),
            String::from("#.#L#L#.##"),
            String::from("..L.L....."),
            String::from("#L#L##L#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
    }

    #[test]
    fn test_sixth_generation_seats() {
        let init = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.#.L..#.."),
            String::from("#L##.##.L#"),
            String::from("#.#L.LL.LL"),
            String::from("#.#L#L#.##"),
            String::from("..L.L....."),
            String::from("#L#L##L#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        let next = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.#.L..#.."),
            String::from("#L##.##.L#"),
            String::from("#.#L.LL.LL"),
            String::from("#.#L#L#.##"),
            String::from("..L.L....."),
            String::from("#L#L##L#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        assert_eq!(evolve(&init, &false), next);
    }

    #[test]
    fn test_count_free_seats() {
        let seats = vec![
            String::from("#.#L.L#.##"),
            String::from("#LLL#LL.L#"),
            String::from("L.#.L..#.."),
            String::from("#L##.##.L#"),
            String::from("#.#L.LL.LL"),
            String::from("#.#L#L#.##"),
            String::from("..L.L....."),
            String::from("#L#L##L#L#"),
            String::from("#.LLLLLL.L"),
            String::from("#.#L#L#.##"),
        ];

        assert_eq!(count_free(&seats), 37);
    }

    #[test]
    fn test_stable_free_seats() {
        let seats = vec![
            String::from("L.LL.LL.LL"),
            String::from("LLLLLLL.LL"),
            String::from("L.L.L..L.."),
            String::from("LLLL.LL.LL"),
            String::from("L.LL.LL.LL"),
            String::from("L.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLLL"),
            String::from("L.LLLLLL.L"),
            String::from("L.LLLLL.LL"),
        ];
      assert_eq!(stable_free(&seats, &false), 37);
      assert_eq!(stable_free(&seats, &true), 26);
    }

    #[test]
    fn test_second_generation_new_rules() {
        let init = vec![
            String::from("#.##.##.##"),
            String::from("#######.##"),
            String::from("#.#.#..#.."),
            String::from("####.##.##"),
            String::from("#.##.##.##"),
            String::from("#.#####.##"),
            String::from("..#.#....."),
            String::from("##########"),
            String::from("#.######.#"),
            String::from("#.#####.##"),
        ];

        let next = vec![
            String::from("#.LL.LL.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..L.."),
            String::from("LLLL.LL.LL"),
            String::from("L.LL.LL.LL"),
            String::from("L.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLL#"),
            String::from("#.LLLLLL.L"),
            String::from("#.LLLLL.L#"),
        ];

        assert_eq!(evolve(&init, &true), next);
    }

    #[test]
    fn test_third_generation_new_rules() {
        let init = vec![
            String::from("#.LL.LL.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..L.."),
            String::from("LLLL.LL.LL"),
            String::from("L.LL.LL.LL"),
            String::from("L.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLL#"),
            String::from("#.LLLLLL.L"),
            String::from("#.LLLLL.L#"),
        ];

        let next = vec![
            String::from("#.L#.##.L#"),
            String::from("#L#####.LL"),
            String::from("L.#.#..#.."),
            String::from("##L#.##.##"),
            String::from("#.##.#L.##"),
            String::from("#.#####.#L"),
            String::from("..#.#....."),
            String::from("LLL####LL#"),
            String::from("#.L#####.L"),
            String::from("#.L####.L#"),
        ];

        assert_eq!(evolve(&init, &true), next);
    }

    #[test]
    fn test_fourth_generation_new_rules() {
        let init = vec![
            String::from("#.L#.##.L#"),
            String::from("#L#####.LL"),
            String::from("L.#.#..#.."),
            String::from("##L#.##.##"),
            String::from("#.##.#L.##"),
            String::from("#.#####.#L"),
            String::from("..#.#....."),
            String::from("LLL####LL#"),
            String::from("#.L#####.L"),
            String::from("#.L####.L#"),
        ];

        let next = vec![
            String::from("#.L#.L#.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..#.."),
            String::from("##LL.LL.L#"),
            String::from("L.LL.LL.L#"),
            String::from("#.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLL#"),
            String::from("#.LLLLL#.L"),
            String::from("#.L#LL#.L#"),
        ];

        assert_eq!(evolve(&init, &true), next);
    }

    #[test]
    fn test_fifth_generation_new_rules() {
        let init = vec![
            String::from("#.L#.L#.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..#.."),
            String::from("##LL.LL.L#"),
            String::from("L.LL.LL.L#"),
            String::from("#.LLLLL.LL"),
            String::from("..L.L....."),
            String::from("LLLLLLLLL#"),
            String::from("#.LLLLL#.L"),
            String::from("#.L#LL#.L#"),
        ];

        let next = vec![
            String::from("#.L#.L#.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..#.."),
            String::from("##L#.#L.L#"),
            String::from("L.L#.#L.L#"),
            String::from("#.L####.LL"),
            String::from("..#.#....."),
            String::from("LLL###LLL#"),
            String::from("#.LLLLL#.L"),
            String::from("#.L#LL#.L#"),
        ];

        assert_eq!(evolve(&init, &true), next);
    }

    #[test]
    fn test_sixth_generation_new_rules() {
        let init = vec![
            String::from("#.L#.L#.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..#.."),
            String::from("##L#.#L.L#"),
            String::from("L.L#.#L.L#"),
            String::from("#.L####.LL"),
            String::from("..#.#....."),
            String::from("LLL###LLL#"),
            String::from("#.LLLLL#.L"),
            String::from("#.L#LL#.L#"),
        ];

        let next = vec![
            String::from("#.L#.L#.L#"),
            String::from("#LLLLLL.LL"),
            String::from("L.L.L..#.."),
            String::from("##L#.#L.L#"),
            String::from("L.L#.LL.L#"),
            String::from("#.LLLL#.LL"),
            String::from("..#.L....."),
            String::from("LLL###LLL#"),
            String::from("#.LLLLL#.L"),
            String::from("#.L#LL#.L#"),
        ];

        assert_eq!(evolve(&init, &true), next);
    }
}
