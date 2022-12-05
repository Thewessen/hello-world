#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import islice
from enum import Enum


def parse_input(data: Iterator[str]) -> Iterator[list[int]]:
    """Parses Elve inventory from puzzle input"""
    inventory = []
    for line in data:
        if line.strip() == '':
            yield inventory
            inventory = []
        else:
            inventory.append(int(line.strip()))
    if len(inventory) > 0:
        yield inventory


def inventory_sizes(data: Iterator[str]) -> Iterator[int]:
    """Map elves inventory data to inventory sizes"""
    return (sum(inventory) for inventory in parse_input(data))


def largest_inventory(data: Iterator[str]) -> int:
    """Largest elve inventory (part 1)"""
    return max(inventory_sizes(data))


def top_three(sizes: Iterator[int]) -> Iterator[int]:
    """Top three elve inventory sizes (part 1)"""
    return islice(sorted(sizes, reverse=True), 3)


def top_three_total_inventory_size(data: Iterator[str]) -> int:
    """Total inventory size top three elve inventories (part 2)"""
    return sum(top_three(inventory_sizes(data)))


if __name__ == '__main__':
    create_cli(1, part1=largest_inventory, part2=top_three_total_inventory_size)
