pub fn is_armstrong_number(num: u32) -> bool {
    armstrong_sum(&num) == num
}

fn armstrong_sum(num: &u32) -> u32 {
    let digits = digits(num);
    digits
       .iter()
       .map(|n| n.pow(digits.len() as u32))
       .sum()
}

fn digits(num: &u32) -> Vec<u32> {
    num.to_string()
       .chars()
       .map(|c| c.to_digit(10).unwrap_or(0))
       .collect()
}
