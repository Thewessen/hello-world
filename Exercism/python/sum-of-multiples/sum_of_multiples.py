def sum_of_multiples(limit: int, multiples: list) -> int:
    """Given a number, finds the sum of all the unique multiples
    of particular numbers up to but not including that number."""
    return sum(set(n for m in multiples if m > 0 for n in range(m, limit, m)))
