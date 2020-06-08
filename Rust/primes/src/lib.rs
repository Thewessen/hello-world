//! # Iterable primes
//! 
//! This crate `primes` contains the structure for creating
//! an endless iterable stream of primes
//! 
//! ### Example
//!
//! ```
//! let primes_iter = iter::Primes::default();
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
//! let primes_iter = iter::Primes::default();
//! let first_two_primes: Vec<u64> = primes_iter.take(2).collect();
//!
//! assert_eq!(first_two_primes, [2, 3]);
//! ```

pub type Prime = u64;

pub use self::up_to::primes_up_to;
pub use self::iter::Primes;

pub mod iter;
pub mod up_to;
