fn main() {
    // String class is stored on the heap (variable size)
    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);
}
