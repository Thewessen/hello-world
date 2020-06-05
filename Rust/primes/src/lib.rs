//! # Iterable primes
//! 
//! This crate `primes` contains the structure for creating
//! an endless iterable stream of primes
//! 
//! ### Example
//!
//! ```
//! let primes_iter = primes::Primes::new();
//! for prime in primes_iter {
//!     assert_eq!(prime, 2);
//!
//! /** <-- do stuff here --> */
//!     # break;
//! }
//! ```
//!
//! All methods from the Iterable trait are included
//!
//! ### Example
//!
//! ```
//! let primes_iter = primes::Primes::new();
//! let first_two_primes: Vec<u64> = primes_iter.take(2).collect();
//!
//! assert_eq!(first_two_primes, [2, 3]);
//! ```

pub use self::primes::Primes;

pub mod primes;
