pub fn factors(n: u64) -> Vec<u64> {
    let mut factors: Vec<u64> = Vec::new();
    let mut rem = n;
    let mut div = 2;
    while rem > 1 {
        if let 0 = rem % div {
            factors.push(div);
            rem /= div;
        } else {
            div += 1;
        }
    }
    factors
}
