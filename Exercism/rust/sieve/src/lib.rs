type Prime = u64;

/// basic iterable primes structure
#[derive(Default)]
struct Primes {
    cache: Vec<Prime>,
    last: Prime,
}

impl Primes {
    /// creates a default iterable instance of Primes
    pub fn default() -> Self {
        Primes {
            cache: vec![],
            last: 1
        }
    }
    fn is_prime(&self, n: &u64) -> bool {
        self.cache.iter().all(|p| n % p != 0)
    }
}

/// makes the prime struct iterable
impl Iterator for Primes {
    type Item = Prime;

    fn next(&mut self) -> Option<Self::Item> {
        self.last = if self.last < 3 {
            self.last + 1
        } else {
            (self.last + 2..)
                .step_by(2)
                .find(|n| self.is_prime(n))
                .unwrap()
        };
        self.cache.push(self.last);
        Some(self.last)
    }
}

pub fn primes_up_to(upper_bound: u64) -> Vec<Prime> {
    Primes::default()
        .take_while(|p| p <= &upper_bound)
        .collect()
}
