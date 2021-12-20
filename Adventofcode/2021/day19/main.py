#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from itertools import combinations
from functools import reduce


class Scanner:
    def __init__(self, id: int, coords: set[tuple[int, int, int]]):
        self.id = id
        self.coords = coords
        self._dist_map = None
        self.coord = None

    def __repr__(self):
        return f'Scanner({self.id})'

    def __eq__(self, other):
        return self.id == other.id

    @property
    def distance_map(self):
        if self._dist_map is None:
            self._dist_map = dict()
            for a in self.coords:
                self._dist_map[a] = list(sorted(calc_distance(a, b)
                                                for b in self.coords
                                                if b != a))
        return self._dist_map

    def set_coord(self, coord: tuple[int, int, int]):
        self.coord = coord


def calc_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    xa, ya, za = a
    xb, yb, zb = b
    return abs(xa - xb) + abs(ya - yb) + abs(za - zb)


def parse_input(data: Iterator[str]) -> Iterator[Scanner]:
    coords = set()
    id = None
    for line in data:
        line = line.strip()
        if line.startswith('---') and id is not None:
            yield Scanner(int(id), coords)
            coords = set()
            id = None
        if line.startswith('---'):
            id = line.split(' ')[2]
        elif line != '':
            x, y, z = line.split(',')
            coords.add((int(x), int(y), int(z)))
    if id is not None:
        yield Scanner(int(id), coords)


def possible_match(dist_map: list[int], other_map: list[int], count = 11) -> bool:
    for dist in dist_map:
        if dist in other_map:
            count -= 1
        if count == 0:
            return True
    return False


def create_coord_map(dist_map_a: dict, dist_map_b: dict):
    # there is only one mapping which can be constructed
    # see `main_test.py` for testing this assumption
    matched_mapping = dict()
    for coord_a, dist_a in dist_map_a.items():
        for coord_b, dist_b in dist_map_b.items():
            if possible_match(dist_a, dist_b):
                matched_mapping[coord_a] = coord_b
                break
    crds = matched_mapping.values()
    if len(set(crds)) != len(crds) or len(crds) < 12:
        return None
    return matched_mapping


def create_transform_func(coord_map: dict):
    swap_func = [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (x, z, y),
        lambda x, y, z: (y, x, z),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (z, x, y),
        lambda x, y, z: (z, y, x),
    ]
    neg_func = [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (-x, y, z),
        lambda x, y, z: (x, -y, z),
        lambda x, y, z: (x, y, -z),
        lambda x, y, z: (-x, -y, z),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (-x, -y, -z),
    ]
    for f in swap_func:
        for g in neg_func:
            first_a, first_b = next(iter(coord_map.items()))
            x, y, z = first_a
            xp, yp, zp = f(*g(*first_b))
            dx, dy, dz = (x - xp, y - yp, z - zp)
            h = lambda x, y, z: (x + dx, y + dy, z + dz)
            fn = lambda coord: h(*f(*g(*coord)))
            if all(fn(b) == a for a, b in coord_map.items()):
                return fn


def create_beacon_coords(curr_scanner: Scanner, scanners: list[Scanner], scanner_ids: set[int]):
    beacons = set()
    for s in scanners:
        if s.id in scanner_ids:
            continue
        coord_map = create_coord_map(curr_scanner.distance_map, s.distance_map)
        if coord_map is None:
            continue
        fn = create_transform_func(coord_map)
        if fn is None:
            continue
        new_coords = create_beacon_coords(s, scanners, scanner_ids | {s.id})
        beacons |= {fn(coord) for coord in s.coords | new_coords}
    return beacons


def count_unique_beacons(data: Iterator[str]) -> int:
    scanners = list(parse_input(data))
    curr_scanner = scanners[0]
    beacons = curr_scanner.coords
    beacons |= create_beacon_coords(curr_scanner, scanners, {0})
    return len(beacons)


def scanner_coords(curr_scanner: Scanner, scanners: list[Scanner], scanner_ids: set[int], fns = []):
    for s in scanners:
        if s.id in scanner_ids:
            continue
        coord_map = create_coord_map(curr_scanner.distance_map, s.distance_map)
        if coord_map is None:
            continue
        fn = create_transform_func(coord_map)
        if fn is None:
            continue
        yield reduce(lambda coord, f: f(coord), reversed(fns), fn((0, 0, 0)))
        yield from scanner_coords(s, scanners, scanner_ids | {s.id}, fns + [fn])


def largest_manhattan_distance(data: Iterator[str]) -> int:
    scanners = list(parse_input(data))
    curr_scanner = scanners[0]
    curr_scanner.set_coord((0, 0, 0))
    coords = scanner_coords(curr_scanner, scanners, {0})
    return max(calc_distance(a, b) for a, b in combinations(coords, 2))


def main():
    parser = ArgumentParser(description="Day 19 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open('./input', 'r') as data:
        if args.part2:
            r = largest_manhattan_distance(data)
        else:
            r = count_unique_beacons(data)
        print(r)


if __name__ == '__main__':
    main()
