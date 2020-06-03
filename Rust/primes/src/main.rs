use primes::Primes;

fn main() {
    let primes = Primes::new();

    for prime in primes {
        println!("{}", prime.to_string());
    }
}
