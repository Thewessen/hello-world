// takes about 2.2 seconds for test_big_prime
pub fn nth(n: u32) -> u32 {
    if n == 0 { return 2; }

    let mut primes: Vec<u32> = vec![2];
    let mut prime: u32 = 3;

    'exit: loop {
        if !primes.iter().any(|p| prime % p == 0) {
            primes.push(prime);
        }
        if primes.len() == n as usize + 1 {
            break 'exit prime;
        }
        prime += 2;
    }
}

// takes about 6.8 second for test_big_prime
// pub fn nth(n: u32) -> u32 {
//     if n == 0 { return 2; }
//     (3..).step_by(2)
//          .filter(|p| !(3..p / 2 + 1).step_by(2).any(|i| p % i == 0))
//          .nth(n as usize - 1)
//          .unwrap()
// }
