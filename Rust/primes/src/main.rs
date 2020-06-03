use primes::Primes;

fn main() {
    let mut primes = Primes::new();

    println!("21th = {}", primes.nth(21).unwrap_or(2));
    for prime in Primes::new().take(10) {
        println!("{}", prime.to_string());
    }
}
