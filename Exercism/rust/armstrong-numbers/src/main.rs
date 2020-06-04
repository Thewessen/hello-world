fn main() {
    let string = String::from("123");
    let iter = string
       .chars()
       .enumerate()
       .map(|(i, c)| c.to_digit(10).unwrap_or(0).pow(i as u32 + 1));
    for c in iter {
        println!("{}", c);
    }
}
