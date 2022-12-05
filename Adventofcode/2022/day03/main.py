#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from more_itertools import chunked


def parse_input(data: Iterator[str]) -> Iterator[str]:
    """Parses rucksacks from given input"""
    return (line.strip() for line in data)


def split_compartment(rucksack: str) -> tuple[set[str], set[str]]:
    """Return the two compartment with their respective items from rucksack"""
    mid = int(len(rucksack) / 2)
    return set(rucksack[:mid]), set(rucksack[mid:])


def duplicate_item(rucksack: str) -> str:
    """Returns the item which is in both compartments of the given rucksack"""
    compart1, compart2 = split_compartment(rucksack)
    intersect = compart1.intersection(compart2)

    if len(intersect) != 1:
        raise ValueError(f"""More than one duplicate item found:
            rucksack: {rucksack}
            compart1: {''.join(compart1)}
            compart2: {''.join(compart2)}
            items: {','.join(intersect)}""")

    return intersect.pop()


def duplicate_item_in_rucksacks(*rucksacks: str) -> str:
    """Returns the duplicate item in multiple rucksacks"""
    if len(rucksacks) < 2:
        raise ValueError(f"Two or more rucksacks should be provided")

    rucksacks_iter = iter(rucksacks)
    intersect = set(next(rucksacks_iter)).intersection(set(next(rucksacks_iter)))
    for rucksack in rucksacks_iter:
        intersect = intersect.intersection(set(rucksack))

    if len(intersect) != 1:
        raise ValueError(f"""More than one duplicate item found:
            rucksacks: {', '.join(rucksacks)}
            items: {', '.join(intersect)}""")

    return intersect.pop()


def item_priority(item: str) -> int:
    """Returns the value (priority) of a given item"""
    if item.islower():
        return ord(item) - 96
    if item.isupper():
        return ord(item) - 38
    raise ValueError(f"Score not calculatable for item: {item}")


def total_score_errors(data: Iterator[str]) -> int:
    """Score the sum of all errors in given input (part 1)"""
    return sum(item_priority(duplicate_item(rucksack))
               for rucksack in parse_input(data))


def total_score_badges(data: Iterator[str]) -> int:
    """Score the sum of all badge priorities in given input (part 2)"""
    return sum(item_priority(duplicate_item_in_rucksacks(*rucksacks))
               for rucksacks in chunked(parse_input(data), 3))


if __name__ == '__main__':
    create_cli(3, part1=total_score_errors, part2=total_score_badges)
