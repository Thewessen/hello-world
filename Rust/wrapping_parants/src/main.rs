#[macro_use] extern crate tramp;

use tramp::{tramp, Rec};

fn main() {
    // max stall stack reach
    println!("{}", str_matching_parants((2 as u64).pow(18)));
}

fn str_matching_parants(count: u64) -> String {
    tramp(wrap_parants(String::from(""), count))
}

fn wrap_parants(s: String, count: u64) -> Rec<String> {
    match count {
        0 => rec_ret!(s),
        _ => rec_call!(wrap_parants("{".to_owned() + &s + "}", count - 1))
    }
}

