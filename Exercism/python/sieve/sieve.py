from itertools import count


class Primes(object):
    """Iterable primes using Sieve of Eratosthenes"""
    def __init__(self, end=None):
        if not isinstance(end, (int, None)):
            raise ValueError(f'Not a valid end ({end})')
        self.numbers = count(2)
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        p = next(self.numbers)
        if self.end is not None and p > self.end:
            raise StopIteration
        self.numbers = filter(lambda n: n % p, self.numbers)
        return p


def primes(limit: int) -> list:
    """Just to pass test"""
    return [*Primes(limit)]
