from itertools import groupby


def palindromes(
        min_factor: int,
        max_factor: int,
        reverse: bool = False
        ) -> iter:
    """All palindromes and its factors"""
    return map(lambda x: (x[0], list(x[1])),
               groupby(sorted(([a, b]
                       for a in range(min_factor, max_factor + 1)
                       for b in range(a, max_factor + 1)
                       if str(a * b) == str(a * b)[::-1]),
                       key=lambda n: n[0] * n[1], reverse=reverse),
                       key=lambda n: n[0] * n[1]))


def palindrome_factors(
        min_factor: int,
        max_factor: int,
        reverse: bool = False
        ) -> iter:
    """Largest or smallest palindrome factor with assertion"""
    if min_factor > max_factor:
        raise ValueError("min_factor should be smaller then max_factor")
    try:
        return next(palindromes(min_factor, max_factor, reverse=reverse))
    except StopIteration:
        return None, []


def largest(min_factor: int, max_factor: int) -> list:
    """Largest palindrome between min- and max-factor"""
    return palindrome_factors(min_factor, max_factor, True)


def smallest(min_factor: int, max_factor: int) -> list:
    """Smallest palindrome between min- and max-factor"""
    return palindrome_factors(min_factor, max_factor)
