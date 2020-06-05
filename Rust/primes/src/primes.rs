type Prime = u64;

/// basic prime structure
pub struct Primes {
    primes: Vec<Prime>,
}

impl Primes {
    /// creates a new iterable instance of Primes
    pub fn new() -> Primes {
        Primes { primes: vec![] }
    }
}

/// makes the prime struct iterable (inc. all methods)
impl Iterator for Primes {
    type Item = Prime;

    fn next(&mut self) -> Option<Self::Item> {
        let mut prime: Prime = self.primes.last().unwrap_or(&1) + 1;
        while self.primes.iter().any(|p| prime % p == 0) {
            prime += 2;
        }
        self.primes.push(prime);
        Some(prime)
    }
}
