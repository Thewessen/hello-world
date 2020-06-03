fn main() {
    println!("{}", str_matching_parants(5));
}

fn str_matching_parants(count: i32) -> String {
    wrap_parants(String::from(""), count)
}

fn wrap_parants(s: String, count: i32) -> String {
    match count {
        0 => s,
        _ => wrap_parants("{".to_owned() + &s + "}", count - 1)
    }
}

