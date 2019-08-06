def factors(value: int) -> list:
    """Calculates list of all prime factors for given value"""
    return [*gen_factors(value)]


def gen_factors(value: int) -> iter:
    """Generates prime factor for given value"""
    for n in range(2, value + 1):
        if value == 1:
            break
        while value % n == 0:
            yield n
            value //= n
