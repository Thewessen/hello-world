type Prime = u64;

pub struct Primes {
    primes: Vec<Prime>,
}


impl Primes {
    pub fn new() -> Primes {
        Primes { primes: vec![] }
    }
}

impl Iterator for Primes {
    type Item = Prime;

    fn next(&mut self) -> Option<Self::Item> {
        let mut prime: Prime = self.primes.last().unwrap_or(&1) + 1;
        while self.primes.iter().any(|p| prime % p == 0) {
            prime += 1;
        }
        self.primes.push(prime);
        Some(prime)
    }
}
