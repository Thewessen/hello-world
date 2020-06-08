use primes::Primes;
use primes::primes_up_to;

fn main() {
    let mut primes = Primes::default();
    println!("1st = {}", primes.next().unwrap());

    println!("21th = {}", primes.nth(21).unwrap_or(2));
    for prime in Primes::default().take(10) {
        println!("{}", prime.to_string());
    }

    println!("1000 primes:");
    println!("{:?}", primes_up_to(100_000));
}
