pub fn is_armstrong_number(num: u32) -> bool {
    let string = num.to_string();
    string.chars()
          .map(|c| c.to_digit(10).unwrap_or(0))
          .map(|n| n.pow(string.len() as u32))
          .sum::<u32>() == num
}
