from itertools import cycle, chain


# chain/cycle found on many solution on exercism.io
# nice way to create indices for rail pattern
def pattern(values: iter, rails: int) -> iter:
    """Gives characters in the order they appear on each rail"""
    indices = cycle(chain(range(rails), range(rails - 2, 0, -1)))
    return (v for v, __ in sorted(zip(values, indices), key=lambda t: t[1]))


def encode(message: str, rails: int) -> str:
    """Encoding for the rail fence cipher."""
    return ''.join(pattern(message, rails))


def decode(message: str, rails: int) -> str:
    """Decoding for the rail fence cipher."""
    look_up = list(pattern(range(len(message)), rails))
    return ''.join(message[look_up.index(i)] for i in range(len(message)))
