import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from collections import Counter
from functools import partial

def parse_input(input: Iterator[str], debug: bool = False, part2: bool = False) -> Counter:
    beam_positions = set()
    counter = Counter()
    for line in input:
        if len(beam_positions) == 0:
            start_pos = line.strip().find('S')
            if debug:
                print(f"Found start position at {start_pos}")
            if part2:
                counter[start_pos] += 1
            beam_positions.add(start_pos)
            continue
        new_positions = set()
        for pos in beam_positions:
            new_positions.add(pos)
            if line[pos] == '^':
                if part2:
                    counter[pos - 1] += counter[pos]
                    counter[pos + 1] += counter[pos]
                    del counter[pos]
                else:
                    # for part 1 we only count the splits itself
                    counter[0] += 1
                if debug:
                    print(f"Counter: {counter}")
                new_positions.remove(pos)
                new_positions.add(pos - 1)
                new_positions.add(pos + 1)
        beam_positions = new_positions
        if debug:
            print(f"Beam positions: {beam_positions}")
    return counter

def count_splitters(input: Iterator[str], debug: bool = False, part2: bool = False) -> int:
    """Count the number of splitters in the input"""
    counter = parse_input(input, debug=debug, part2=part2)
    return counter.total()

if __name__ == '__main__':
    create_cli(7, part1=count_splitters, part2=partial(count_splitters, part2=True))
