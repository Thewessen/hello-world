#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Optional

class Cave:
    """A cave-system is build out of these Caves.
    Each cave can hold connections to other caves."""
    START = 'start'
    END = 'end'

    def __init__(self, name: str):
        self._name = name
        self._conns = set()

    @property
    def connections(self):
        return set(self._conns)

    @property
    def name(self):
        return self._name

    def add_conn(self, other):
        self._conns.add(other)

    def is_small(self):
        return self._name.islower()

    def __eq__(self, other):
        if isinstance(other, str):
            return self._name == other
        if isinstance(other, Cave):
            return self._name == other.name
        return False

    def __repr__(self):
        return f"Cave('{self._name}')"

    def __hash__(self):
        return hash(self._name)


class Path:
    """Reperesents a path through a cave-system."""
    def __init__(self, init = []):
        self._path: list[Cave] = init

    @classmethod
    def from_path(cls, other):
        return cls(list(other._path))

    @property
    def end(self):
        if len(self._path) > 0:
            return self._path[-1]

    def add(self, cave: Cave):
        self._path.append(cave)
        return self

    def is_valid(self, cave: Cave, strict = True):
        if not cave.is_small():
            return True

        if strict or cave == Cave.START or cave == Cave.END:
            return cave not in self._path

        return (cave not in self._path
                or unique_caves(c for c in self._path if c.is_small()))

    def is_complete(self):
        return self.end == Cave.END

    def __repr__(self):
        return '-'.join(cave.name for cave in self._path)


def unique_caves(caves: Iterator[Cave]) -> bool:
    """Validates if an iterator of caves contains unique caves.
    The iterator is consumed in the process."""
    s = set()
    for cave in caves:
        if cave in s:
            return False
        s.add(cave)
    return True


def search_cave(name: str, caves: set[Cave]) -> Optional[Cave]:
    """Returns a specific cave out of a set of caves. Returns None of the cave
    is not found."""
    for cave in caves:
        if cave.name == name:
            return cave


def valid_paths(curr: Cave, strict = True, path = Path()) -> Iterator[Path]:
    """Constructs valid paths from a starting cave. Paths may not be ending!"""
    if not path.is_valid(curr, strict):
        yield path
    elif curr == Cave.END:
        yield Path.from_path(path).add(curr)
    else:
        new_path = Path.from_path(path).add(curr)
        for cave in curr.connections:
            yield from valid_paths(cave, strict, new_path)


def parse_input(data: Iterator[str]) -> set[Cave]:
    """Constructs a cave system from cave-connections data."""
    caves = set()
    for line in data:
        start, end = line.strip().split('-')
        start_cave = search_cave(start, caves) or Cave(start)
        end_cave = search_cave(end, caves) or Cave(end)
        caves |= {start_cave, end_cave}
        start_cave.add_conn(end_cave)
        end_cave.add_conn(start_cave)
    return caves


def count_valid_paths(data: Iterator[str], part2 = False) -> int:
    """Counts the number of valid and complete paths through a cave system,
    constructed from cave-connections data."""
    caves = parse_input(data)
    start = search_cave(Cave.START, caves)
    if start is None:
        return 0
    return sum(1 for p in valid_paths(start, not part2) if p.is_complete())


def main():
    parser = ArgumentParser(description="Day 12 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        print(count_valid_paths(data, args.part2))


if __name__ == '__main__':
    main()
