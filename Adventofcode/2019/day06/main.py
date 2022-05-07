#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator

def parse_input(data: Iterator[str]) -> dict[str, list[str]]:
    orbits = dict()
    for orbit in data:
        [root, planet] = orbit.strip().split(')')
        if root in orbits:
            orbits[root].append(planet)
        else:
            orbits[root] = [planet]
    return orbits


def count_orbits(data: dict[str, list[str]], planet = 'COM') -> tuple[int, int]:
    """Counts the number of orbits and planets. Returns a tuple
    (#orbits, #planets)"""
    if planet not in data:
        return 0, 1
    planet_count = 0
    orbit_count = 0
    for p in data[planet]: 
        oc, pc = count_orbits(data, p)
        planet_count += pc
        orbit_count += oc
    return orbit_count + planet_count, planet_count + 1

def orbit_route(data: dict[str, list[str]], planet = 'COM') -> tuple[int, bool]:
    if planet not in data:
        return 0, False
    if 'YOU' in data[planet] or 'SAN' in data[planet]:
        return 1, False
    dist = 0
    matched = 0
    for p in data[planet]: 
        c, m = orbit_route(data, p)
        if c > 0:
            dist += c + int(not m)
            matched = 2 if m else matched + 1
    return dist, matched >= 2


def santa_distance(data: dict[str, list[str]]) -> int:
    """Calculates the distance between you and santa. (see README part 2)"""
    dist, matched = orbit_route(data)
    if not matched:
        raise ValueError('No valid route found')
    return dist - 2 # YOU and SAN don't count as planets


def part_1(data: Iterator[str]) -> int:
    """Solution part 1 (see Readme)"""
    orbits, _ = count_orbits(parse_input(data))
    return orbits

def part_2(data: Iterator[str]) -> int:
    """Solution part 2 (see Readme)"""
    return santa_distance(parse_input(data))

if __name__ == '__main__':
    create_cli(6, part1=part_1, part2=part_2)
