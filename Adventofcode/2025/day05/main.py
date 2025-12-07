import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import takewhile

class Range:
    def __init__(self, start: int, end: int):
        if start > end:
            raise ValueError(f'Invalid range: {start}-{end}')
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Range({self.start}, {self.end})'

    def includes(self, n: int) -> bool:
        return self.start <= n <= self.end

    def __len__(self):
        return self.end - self.start + 1
    
    def isdisjoint(self, other: 'Range') -> bool:
        return self.end < other.start or self.start > other.end

    def union(self, other: 'Range') -> 'Range':
        return Range(min(self.start, other.start), max(self.end, other.end))


def parse_input(data: Iterator[str], debug: bool = False) -> Iterator[Range]:
    for line in takewhile(lambda l: l.strip() != '', data):
        # yield all ranges
        start, end = line.strip().split('-')
        r = Range(int(start), int(end))
        yield r

    # seperate ranges from ids with None
    yield None

    for line in data:
        # yield all ids
        if line.strip() == '':
            continue
        yield line.strip()

def pick_fresh_ids(data: Iterator[str], debug: bool = False) -> int:
    input = parse_input(data, debug=debug)
    ranges = list(takewhile(lambda r: isinstance(r, Range), input))
    if debug:
        print(f'ranges: {ranges}')
    for id in input:
        included = any(r.includes(int(id)) for r in ranges)
        if debug:
            print(f'  checking {id} -> {included}')
        if included:
            yield id

def join_ranges(ranges: Iterator[Range], debug: bool = False) -> Iterator[Range]:
    ranges = sorted(ranges, key=lambda r: r.start)
    if len(ranges) == 0:
        return

    current_range = ranges[0]
    for r in ranges[1:]:
        if current_range.isdisjoint(r):
            if debug:
                print(f'new range: {current_range}')
            yield current_range
            current_range = r
            continue
        current_range = r.union(current_range)

    if debug:
        print(f'new range: {current_range}')
    yield current_range

def count_fresh_ids(data: Iterator[str], debug: bool = False) -> int:
    """Count the number of fresh ids"""
    return sum(1 for _ in pick_fresh_ids(data, debug=debug))

def count_all_possible_fresh_ids(data: Iterator[str], debug: bool = False) -> int:
    """Count the number of possible fresh ids"""
    input = parse_input(data, debug=debug)
    ranges = takewhile(lambda r: isinstance(r, Range), input)
    # For this part we ignore the ids in the input
    return sum(len(r) for r in join_ranges(ranges, debug=debug))

if __name__ == '__main__':
    create_cli(5, part1=count_fresh_ids, part2=count_all_possible_fresh_ids)
