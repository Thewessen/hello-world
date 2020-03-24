pub fn raindrops(n: u32) -> String {
    let mut sound = String::with_capacity(15);

    if n % 3 == 0 { sound += "Pling" };
    if n % 5 == 0 { sound += "Plang" };
    if n % 7 == 0 { sound += "Plong" };
    if sound.is_empty() { sound = n.to_string() }

    sound
}
