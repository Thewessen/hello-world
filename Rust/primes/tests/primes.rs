#[macro_use]
extern crate time_test;

use primes::Prime;
use primes::iter::Primes;
use primes::up_to::primes_up_to;

#[test]
#[ignore]
fn first_prime() {
    assert_eq!(Primes::default().next().unwrap(), 2);
}

#[test]
#[ignore]
fn first_three_primes() {
    let first_three_primes: Vec<Prime> = Primes::default().take(3).collect();
    assert_eq!(first_three_primes, [2, 3, 5]);
}

#[test]
#[ignore]
fn hunderest_prime() {
    let prime: Prime = Primes::default().nth(100).unwrap();
    assert_eq!(prime, 547);
}

#[test]
#[ignore]
// Takes 5.5-6 sec to run
fn ten_thousendths_prime_using_iter() {
    time_test!();
    let prime: Prime = Primes::default().nth(10_000).unwrap();
    assert_eq!(prime, 104743);
}

#[test]
#[ignore]
// Takes 2.5-3 sec to run
fn ten_thousendths_prime_using_up_to() {
    time_test!();
    let primes: Vec<Prime> = primes_up_to(104_744);
    assert_eq!(*primes.last().unwrap(), 104_743);
}

#[test]
// Takes about 75 secs to run
fn fifty_thousendths_prime_using_iter() {
    time_test!();
    let prime: Prime = Primes::default().nth(50_000).unwrap();
    assert_eq!(prime, 611_957);
}
