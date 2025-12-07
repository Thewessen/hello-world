import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import takewhile
from math import ceil

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Range({self.start}, {self.end})'

    def includes(self, n: int) -> bool:
        return self.start <= n <= self.end

    @property
    def str_start(self):
        return str(self.start)

    @property
    def str_end(self):
        return str(self.end)


def split_ranges(chars: Iterator[str]) -> Iterator[str]:
    """Example input 123-124,125-126"""
    for c in chars:
        yield c +''.join(takewhile(lambda x: x != ',', chars))

def parse_input(chars: Iterator[str]) -> Iterator[Range]:
    """Example input 123-124"""
    for id in split_ranges(chars):
        start, end = id.split('-')
        yield Range(int(start), int(end))

def invalid_ids(chars: Iterator[str], debug: bool = False) -> int:
    for ranges in parse_input(chars):
        if debug:
            print(f'Checking {ranges}')

        if (len(ranges.str_start) == len(ranges.str_end)
            and len(ranges.str_start) % 2 == 1):
            if debug:
                print('Not possible to construct an invalid id in this uneven range')
            continue

        even_start_len = ceil(len(ranges.str_start) / 2) * 2
        mid_start_len = even_start_len // 2
        start_str = ranges.str_start.zfill(even_start_len)
        even_end_len = ceil(len(ranges.str_end) / 2) * 2
        mid_end_len = even_end_len // 2
        end_str = ranges.str_end
        start_part = int(start_str[:mid_start_len])
        end_part = int(ranges.str_end[:mid_end_len])
        if debug:
            print(f'from {start_part} to {max(end_part, start_part + 1)}')
        for n in range(start_part, max(end_part, start_part + 1) + 1):
            invalid_id = int(str(n) + str(n))
            if debug:
                print(f'Checking {invalid_id} in {ranges} -> {ranges.includes(invalid_id)}')
            if ranges.includes(invalid_id):
                yield invalid_id

def is_invalid_id(id: int) -> bool:
    if id == 0:
        return False

    length = len(str(id))
    if length == 1:
        return False

    for n in range(1, length):
        if length % n != 0:
            continue
        part = int(str(id)[:n])
        if part == 0:
            continue
        if int(str(id)) == int(str(part) * (length // n)):
            return True

    return False

def invalid_ids_part_2(chars: Iterator[str], debug: bool = False) -> int:
    for ranges in parse_input(chars):
        if debug:
            print(f'=== Checking {ranges} ===')

        for id in range(ranges.start, ranges.end + 1):
            if is_invalid_id(id):
                yield id


def generate_invalid_ids(ranges: Range, debug: bool = False) -> str:
    """Generates invalid ids close to a given range"""
    for l in range(len(ranges.str_start), len(ranges.str_end) + 1):
        ### check for primes
        if l % 2 == 0:
            # is even so the ranges start and end can be split in two
            start_part = ranges.str_start.zfill(l)[:l // 2]
            # end_part = ranges.str_end.zfill(l)[:l // 2]
            end_part = ranges.str_end[:l // 2 + len(ranges.str_end) - len(ranges.str_start)]
            start = max(10 ** ((l // 2) - 1), int(start_part))
            end = min(10 ** (l // 2), int(end_part) + 1)
        else:
            # is uneven so only one number can be repeated
            start_part = ranges.str_start.zfill(l)[:1]
            end_part = ranges.str_end[:1 + len(ranges.str_end) - len(ranges.str_start)]
            start = max(1, int(start_part))
            end = int(end_part) + 1


        if debug:
            print(f"Constructing parts from {start} to {end} with length {l}")
        for part in range(start, end):
            if l % len(str(part)) != 0 or l == len(str(part)):
                # unable to construct id from part for length l
                if debug:
                    print(f"unable to construct id from {part} for length {l}")
                continue

            invalid_id = int(str(part) * (l // len(str(part))))
            if invalid_id > ranges.end:
                break

            if ranges.includes(invalid_id):
                if debug:
                    print(f"found invalid id: {invalid_id}")
                yield invalid_id


def count_invalid_ids(chars: Iterator[str], debug: bool = False) -> int:
    """Sums all part 1 constructed invalid ids"""
    return sum(invalid_ids(chars, debug))

def count_more_invalid_ids(chars: Iterator[str], debug: bool = False) -> int:
    """Sums all part 2 constructed invalid ids"""
    return sum(invalid_ids_part_2(chars, debug))

if __name__ == '__main__':
    create_cli(2, part1=count_invalid_ids, part2=count_more_invalid_ids, charbychar=True)
