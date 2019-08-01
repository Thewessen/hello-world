from string import ascii_uppercase
from string import digits

from random import randint
from itertools import product


class Robot(object):
    """Creates a Robot with a random name, e.g. XE137"""

    def __init__(self):
        self.NAMES = [''.join(char + dig) for char, dig in product(
                    product(ascii_uppercase, repeat=2),
                    product(digits, repeat=3)
                )]
        self.name = self.pick_name()

    def pick_name(self) -> str:
        r = randint(0, len(self.NAMES))
        n = self.NAMES[r]
        self.NAMES = self.NAMES[:r] + self.NAMES[r+1:]
        return n

    def reset(self):
        self.name = self.pick_name()
