#![allow(dead_code)]

#[derive(Debug)]
enum Country {
    Germany,
    Netherlands,
    US,
}

#[derive(Debug)]
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(Country),
}

fn main() {
    let coin: Coin = Coin::Quarter(Country::Germany);
    let value = value_in_cents(&coin);
    println!("The value of the coin {:?} is {}", coin, value);
}

/// Matching using enums, blocks and inner state of enum
fn value_in_cents(coin: &Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter is {:?}", state);
            25
        }
    }
}

fn option_divide(a: i32, b: i32) -> Option<i32> {
    match b {
        0 => None,
        _ => Some(a / b)
    }
}

fn add_one_to_option(n: Option<i32>) -> Option<i32> {
    match n {
        None => None,
        Some(i) => Some(i + 1)
    }
}

#[test]
fn quarter_is_recognized() {
    let coin: Coin = Coin::Quarter(Country::Germany);
    let value = value_in_cents(&coin);
    assert_eq!(value, 25);
}

#[test]
fn divide_by_other_then_zero_gives_some_value() {
    let result = option_divide(6, 3);
    assert_eq!(result, Some(2));
}

#[test]
fn divide_by_zero_gives_none() {
    let result = option_divide(10, 0);
    assert_eq!(result, None);
}

#[test]
fn add_one_to_some() {
    let result = add_one_to_option(Some(3));
    assert_eq!(result, Some(4));
}

#[test]
fn add_one_to_none() {
    let result = add_one_to_option(None);
    assert_eq!(result, None);
}
