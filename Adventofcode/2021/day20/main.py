#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Iterable
import math


class Grid:
    """A helper class for easy access to internal grid points and their
    surrounding points, with eq-comparison and a nice representation
    of the internal grid."""
    def __init__(self, grid: list[list]):
        self._grid = grid
    
    def __eq__(self, other) -> bool:
        return all(all(self.get((i, j)) == other.get((i, j))
                   for j, _ in enumerate(row))
                   for i, row in enumerate(self._grid))

    def __repr__(self):
        return '\n'.join(''.join(str(d) for d in row)
                         for row in self._grid)

    @property
    def size(self):
        return (len(max(self._grid, key=len)), len(self._grid))

    def get(self, point):
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        x, y = point
        return self._grid[y][x]

    def in_bound(self, point) -> bool:
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        x, y = point
        height, width = self.size
        return 0 <= x < width and 0 <= y < height

    def all_coords(self):
        for y, row in enumerate(self._grid):
            for x, _ in enumerate(row):
                yield x, y

    def values(self):
        for row in self._grid:
            for v in row:
                yield v

    def count(self, value):
        return sum(1 for v in self.values()
                   if v == value)


class PartialImage(Grid):
    """A Grid like data class considering its infinity (surrounding)."""
    def __init__(self, grid, surr):
        super().__init__(grid)
        self.surrounding = surr

    @property
    def lit(self):
        if self.surrounding == '#':
            return math.inf
        return self.count('#')

    @classmethod
    def from_iter(cls, data: Iterator[Iterable]):
        return cls([list(line) for line in data], '.')

    def get(self, point):
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        if not self.in_bound(point):
            return self.surrounding
        x, y = point
        return self._grid[y][x]


class ImgEnhAlgo:
    """A simple image enhance algoritm class"""
    def __init__(self, algo: str):
        self.algo = algo.strip()
        self.trans = ''.maketrans('#.', '10')

    def enhance_str(self, stream:str) -> str:
        key = int(stream.translate(self.trans), 2)
        return self.algo[key]

    def _for_coords(self, coords, img):
        for point in coords:
            bin_str = ''.join(img.get(surr)
                              for surr in relevant_square_coords(point))
            yield self.enhance_str(bin_str)

    def enhance(self, img: PartialImage):
        width, height = img.size
        new_img = [list(self._for_coords(((x, y) for x in range(-1, width + 2)), img))
                   for y in range(-1, height + 2)]
        return PartialImage(new_img, self.enhance_str(img.surrounding * 9))


def relevant_square_coords(point: tuple[int, int]) -> Iterator[tuple[int, int]]:
    """Iterates through the relevent 3x3 square coords from given point."""
    # order matters
    x, y = point
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            yield x + dx, y + dy


def enhanced_image_from_data(data: Iterator[str], enhance: int) -> PartialImage:
    """Aplies the image enhance algoritm `enhance` times to get a better image
    from output image found in data (see README)"""
    algo = ImgEnhAlgo(next(data))
    next(data) #skip new line
    img = PartialImage.from_iter(line.strip() for line in data)
    while enhance != 0:
        img = algo.enhance(img)
        enhance -= 1
    return img


def main():
    parser = ArgumentParser(description="Day 20 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open('./input', 'r') as data:
        if args.part2:
            img = enhanced_image_from_data(data, 50)
        else:
            img = enhanced_image_from_data(data, 2)
    print(img.lit)


if __name__ == '__main__':
    main()
