import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from functools import partial
from enum import StrEnum


class Direction(StrEnum):
    LEFT = 'L'
    RIGHT = 'R'


class Rotation:
    def __init__(self, direction: Direction, steps: int):
        self.direction = direction
        self.steps = steps

    @classmethod
    def from_str(cls, s: str) -> 'Rotation':
        return cls(Direction(s[0]), int(s[1:]))

    def relative(self) -> int:
        """Relative rotation in steps"""
        return (self.steps if self.direction == Direction.RIGHT else -self.steps)

    def full_spins(self) -> int:
        """Number of full spins in rotation"""
        return self.steps // 100

    def rest(self) -> 'Rotation':
        """Left over rotation after full spins"""
        return Rotation(self.direction, self.steps % 100)


class Lock:
    n = 50
    ns = 100

    def rotate(self, r: Rotation) -> None:
        self.n += r.relative()
        self.n %= self.ns

    def passes_zero(self, r: Rotation) -> bool:
        if self.n == 0:
            return False

        if r.direction == Direction.LEFT:
            return self.n - r.steps < 0
        else:
            return self.n + r.steps > 100


def parse_input(data: Iterator[str]) -> Iterator[Rotation]:
    """Parses rotations from puzzle input"""
    for line in data:
        yield Rotation.from_str(line.strip())

def handle_lock(data: Iterator[str], part2: bool = False) -> Iterator[int]:
    """Rotates the direction by the given number of steps"""
    lock = Lock()
    for rotation in parse_input(data):
        if part2:
            # count rotations
            yield rotation.full_spins()
            # count passes
            yield int(lock.passes_zero(rotation.rest()))

        # mutates the lock
        lock.rotate(rotation)

        # count hits
        yield int(lock.n == 0)

def count_hits(data: Iterator[str], debug: bool = False) -> int:
    """Counts the number of times the dial lands on zero"""
    return sum(handle_lock(data))

def count_passes(data: Iterator[str], debug: bool = False) -> int:
    """Counts the number of times the dial passes zero"""
    return sum(handle_lock(data, True))

if __name__ == '__main__':
    create_cli(1, part1=count_hits, part2=count_passes)
