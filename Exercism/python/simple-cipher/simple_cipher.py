import random
from string import ascii_lowercase
from string import ascii_uppercase
from itertools import cycle


def random_str(size: int) -> str:
    """Creates a random string of size 'size'"""
    return ''.join(random.choice(ascii_lowercase) for __ in range(size))


def shift(char: str, key: int) -> str:
    """Rotates a 'char' by a given index 'key'"""
    if not char.isalpha():
        return char
    abc = ascii_uppercase if char.isupper() else ascii_lowercase
    return abc[(abc.index(char) + key) % len(abc)]


class Cipher(object):
    """Substitution cipher"""

    def __init__(self, key=None):
        self.key = key or random_str(101)

    def encode(self, text: str) -> str:
        """Substitution cipher encoding"""
        return ''.join(shift(char, ascii_lowercase.index(key))
                       for char, key in zip(text, cycle(self.key)))

    def decode(self, text: str) -> str:
        """Substitution cipher decoding"""
        return ''.join(shift(char, -1 * ascii_lowercase.index(key))
                       for char, key in zip(text, cycle(self.key)))
