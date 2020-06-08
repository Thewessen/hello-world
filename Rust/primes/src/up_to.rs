use crate::Prime;

pub fn primes_up_to(upper_bound: Prime) -> Vec<Prime> {
    match upper_bound {
        2 => vec![2],
        _ if upper_bound < 2 => Vec::new(),
        _ => (3..=upper_bound).step_by(2).fold(vec![2], |mut primes, n| {
            if primes.iter().all(|p| n % p != 0) { primes.push(n) }
            primes
        })
    }
}
