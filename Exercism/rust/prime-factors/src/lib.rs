mod primes;

use crate::primes::Primes;

pub fn factors(n: u64) -> Vec<u64> {
    let mut factors: Vec<u64> = Vec::new();
    let primes = Primes::new();
    // let boundry = n / 2;
    let mut number = n;
    for prime in primes {
        while number % prime == 0 {
            number /= prime;
            factors.push(prime);
        }
        if prime > number {
            break;
        }
    }
    factors
}
