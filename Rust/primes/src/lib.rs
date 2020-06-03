pub struct Primes {
    primes: Vec<u64>,
}

impl Primes {
    pub fn new() -> Primes {
        Primes { primes: vec![2] }
    }
}

impl Iterator for Primes {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let mut prime: u64 = self.primes.last().unwrap_or(&2) + 1;
        while self.primes.iter().any(|p| prime % p == 0) {
            prime += 1;
        }
        self.primes.push(prime);
        Some(prime)
    }
}
