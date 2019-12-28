from itertools import count, islice


def gen_primes() -> iter:
    """Generates primes in order"""
    primes = set()
    for n in count(2):
        if all(n % p != 0 for p in primes):
            yield n
            primes.add(n)


def prime(nth: int) -> int:
    """Returns the nth prime"""
    return next(islice(gen_primes(), nth - 1, None))


def prime_range(n: int) -> int:
    """Returns a list of the first n primes"""
    return list(islice(gen_primes(), n))
