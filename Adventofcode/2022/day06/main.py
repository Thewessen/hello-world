#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from more_itertools import sliding_window


def parse_input(data: Iterator[str]) -> Iterator[str]:
    """Return the datastream found in puzzle input"""
    return iter(next(data).strip())


def first_marker(data: str, unique: int) -> int:
    """Find the first marker position (part 1)"""
    for i, chars in enumerate(sliding_window(data, unique)):
        if len(set(chars)) == unique:
            return i + unique
    raise ValueError(f"No marker found in data: {data}")


def find_first_packet_marker_in_data_stream(data: Iterator[str]) -> int:
    """Parse data stream and find the first packet marker (part 1)"""
    d = parse_input(data)
    return first_marker(d, 4)


def find_first_message_marker_in_data_stream(data: Iterator[str]) -> int:
    """Parse data stream and find the first message marker (part 2)"""
    d = parse_input(data)
    return first_marker(d, 14)


if __name__ == '__main__':
    create_cli(6, part1=find_first_packet_marker_in_data_stream, part2=find_first_message_marker_in_data_stream)
