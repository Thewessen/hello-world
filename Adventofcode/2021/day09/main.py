#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from functools import reduce


def parse_input(data: Iterator[str]) -> list[list[int]]:
    return [[int(i) for i in line.strip()]
            for line in data]

def lowest_points(cloud: list[list[int]]) -> Iterator[tuple[int, int]]:
    for i, row in enumerate(cloud):
        for j, _ in enumerate(row):
            if is_lowest_point(cloud, (i, j), [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]):
                yield (i, j)

def is_lowest_point(cloud: list[list[int]], coord: tuple[int, int], surr: list[tuple[int, int]], strict = True) -> bool:
    x, y = coord
    curr = cloud[x][y]
    return all((i < 0 or i == len(cloud) or j < 0 or j == len(cloud[i])
               or (strict and cloud[i][j] > curr)
               or (not strict and cloud[i][j] >= curr) for i, j in surr))

def get_basin(cloud: list[list[int]], coord: tuple[int, int]):
    basin: list[tuple[int, int]] = [coord]
    while True:
        ext = []
        for point in basin:
            i, j = point
            s = list(filter(lambda p: p not in basin and p not in ext,
                       [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]))
            # print(s)
            for p in s:
                k, l = p
                s_p = list(filter(lambda o: o not in basin and o not in ext,
                    [(k + 1, l), (k - 1, l), (k, l + 1), (k, l - 1)]))
                # print(p, s_p)
                # print(p, s_p, k >= 0, l >= 0, k < len(coord), l < len(coord),
                #         cloud[k][l])
                if (k >= 0 and l >= 0 and k < len(cloud) and l < len(cloud[k])
                    and cloud[k][l] != 9
                    and is_lowest_point(cloud, p, s_p, False)):
                    # print(p)
                    ext.append(p)
        if len(ext) == 0:
            break
        basin += ext
    return basin


def calc_total_risk(data: Iterator[str]) -> int:
    cloud = parse_input(data)
    return sum(cloud[x][y] + 1 for x, y in lowest_points(cloud))


def get_basins(cloud: list[list[int]]) -> Iterator[list[tuple[int, int]]]:
    for point in lowest_points(cloud):
        # print(point)
        # print(get_basin(cloud, point))
        yield get_basin(cloud, point)


def sol_2(data: Iterator[str]):
    cloud = parse_input(data)
    basins = sorted(get_basins(cloud), key=len)
    return reduce(lambda acc, curr: acc * len(curr), basins[-3:], 1)


def main():
    parser = ArgumentParser(description="Day 9 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = sol_2(data)
        else:
            r = calc_total_risk(data)
    print(r)


if __name__ == '__main__':
    main()
