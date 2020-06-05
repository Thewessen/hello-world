use primes::Primes;

pub fn factors(n: u64) -> Vec<u64> {
    let mut factors: Vec<u64> = Vec::new();
    let primes = Primes::new();
    let mut number = n;
    for prime in primes.take_while(|p| p <= &n) {
        while number % prime == 0 {
            number /= prime;
            factors.push(prime);
        }
        if number == 1 {
            break;
        }
    }
    factors
}
