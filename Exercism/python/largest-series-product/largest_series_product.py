def prod(serie: str) -> int:
    """Returns the product of a serie of digits"""
    p = 1
    for digit in serie:
        p *= int(digit)
    return p


def largest_product(series: str, size: int) -> int:
    """Calculates the largest product of serie of digits"""
    if type(size) is not int or size < 0:
        raise ValueError('Invalid size')
    grouped = (series[i:i+size] for i in range(len(series) - size + 1))
    return max(prod(serie) for serie in grouped)
