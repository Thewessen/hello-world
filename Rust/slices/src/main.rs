fn main() {
    let mut s = String::from("Hello, world!");
    let hello = string_slices(&mut s);
    println!("slices = {}", hello);

    s.clear();

    // The compiler makes sure this reference stays valid
    // println!("slices = {}", hello); // ERROR!
}

fn string_slices(s: &String) -> &str {
    // You get a pointer to the underlaying data
    let hello = &s[0..5];

    // some more slices...
    println!("{}", s == &s[0..s.len()]); // true
    println!("{}", s == &s[..]); // true
    println!("{}", &s[..5] == &s[0..5]); // true
    println!("{}", &s[7..] == &s[7..s.len()]); // true

    hello
}
