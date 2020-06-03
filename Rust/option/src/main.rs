#![allow(dead_code, unused_variables)]
fn main() {
    enum Option<T> {
        Some(T),
        None,
    }
    let some_number = Some(5);
    let some_string = Some("a string");

    let absent_number: Option<i32> = None;
}
