import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from functools import partial

class Bank:
    bank: str

    def __init__(self, bank: str):
        self.bank = bank

    @classmethod
    def from_str(cls, string: str) -> 'Bank':
        return cls(string)

    def __repr__(self):
        return f"Bank({self.bank})"

    def max_joltage(self, n: int, debug: bool = False) -> int:
        """Returns the max joltage for a given bank"""
        maxs = []
        pos = -1

        for x in range(n):
            start = max(pos + 1, x)
            # zero indexing should result in None for end part
            end = (1 - n + x) or None
            bank_part = self.bank[start:end]
            if debug:
                print(f"pos: {pos}, x: {x}, start: {start}, end: {end}, bank_part: {bank_part}")
            first_max = max(int(battery) for battery in self.bank[start:end])
            maxs.append(str(first_max))
            pos = bank_part.index(str(first_max)) + start

        max_joltage = ''.join(maxs)
        if debug:
            print(f"max: {max_joltage}")
        return int(max_joltage)


def parse_input(input: Iterator[str], debug: bool = False) -> int:
    """Turns input into banks"""
    for line in input:
        bank = Bank.from_str(line.strip())
        if debug:
            print(bank)
        yield bank

def max_joltage(input: Iterator[str], debug: bool = False, batteries: int = 2) -> int:
    """Sums all max joltages from puzzle input banks"""
    return sum(bank.max_joltage(batteries, debug=debug)
               for bank in parse_input(input, debug=debug))

if __name__ == '__main__':
    create_cli(3, part1=max_joltage, part2=partial(max_joltage, batteries=12))
