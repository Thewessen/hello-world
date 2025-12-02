use scraper::{Html, Selector};

fn get_input() -> String {
    let input = std::fs::read_to_string("input.txt")
        .expect("Failed to read input file");
    input
}

fn main() {
    // let api_key = std::env::var("API_KEY")
    //     .expect("API_KEY not set");

    // TODO: user interaction
    let year = "2023";
    let day = "1";

    let exp_url = format!("https://adventofcode.com/{year}/day/{day}",
                          year=year, day=day);
    // let input_url = format!("https://adventofcode.com/{year}/day/{day}/input",
    //                   year=year, day=day);
    let explanation = reqwest::blocking::get(&exp_url)
        .expect("Failed to get explanation")
        .text()
        .expect("Failed to get explanation text");

    let document = Html::parse_document(&explanation);
    let selector = Selector::parse("main").unwrap();
    let puzzle = document.select(&selector).next().unwrap();
    // let input = thread::spawn(|| reqwest::get(&input_url));
    // let resp = explanation.join().unwrap().await?;
    println!("{:#?}", html2md::parse_html(&puzzle.inner_html()));
    // let resp = reqwest::get("https://www.rust-lang.org").await?;
    // println!(resp.json());
}
