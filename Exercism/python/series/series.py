def slices(series: str, length: int) -> list:
    """Given a string of digits, output all the contiguous substrings
    of length 'n' in that string in the order that they appear."""
    if length > len(series) or length <= 0:
        raise ValueError('Incorrect slice length')
    return [series[i:i+length] for i in range(len(series) - length + 1)]
