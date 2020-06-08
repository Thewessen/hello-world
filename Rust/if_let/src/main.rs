#![allow(dead_code)]
fn main() {
    println!("Hello, world!");
}

fn impl_with_match(o: Option<i32>) -> i32 {
    match o {
        Some(3) => 3,
        _ => 0
    }
}

fn impl_with_if_let(o: Option<i32>) -> i32 {
    let mut r = 0;
    if let Some(3) = o {
        r = 3;
    }
    r
}

#[test]
fn both_impl_are_the_same() {
    let input = Some(3);
    assert_eq!(impl_with_match(input), impl_with_if_let(input));
}
