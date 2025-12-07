import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self
from dataclasses import dataclass
from itertools import groupby

@dataclass
class Coord:
    x: int
    y: int

    @property
    def surrounding(self) -> Iterator[Self]:
        """Get all surrounding coordinates"""
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                yield Coord(self.x + dx, self.y + dy)

    def __repr__(self) -> str:
        """String representation of the coordinate"""
        return f'({self.x}, {self.y})'

    def __hash__(self) -> int:
        """Hash the coordinate"""
        return hash(repr(self))


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
        return '\n'.join(''.join(' ' if d is None else str(d) for d in row)
                         for row in self._grid)

    @classmethod
    def from_iter(cls, data: Iterator[str]):
        return cls([list(line.strip()) for line in data
                                       if line.strip() != ''])

    @property
    def size(self) -> tuple[int, int]:
        return (len(max(self._grid, key=len)), len(self._grid))

    @property
    def all_coords(self) -> Iterator[Coord]:
        for y, row in enumerate(self._grid):
            for x, _ in enumerate(row):
                yield Coord(x, y)

    @property
    def values(self) -> Iterator[str]:
        for row in self._grid:
            for v in row:
                yield v

    def get(self, point: Coord) -> str:
        if not self.in_bound(point):
            return None
        return self._grid[point.y][point.x]

    def set(self, point: Coord, value: str) -> None:
        if not self.in_bound(point):
            return
        self._grid[point.y][point.x] = value

    def in_bound(self, point: Coord) -> bool:
        height, width = self.size
        return 0 <= point.x < width and 0 <= point.y < height

    def count(self, value: str) -> int:
        return sum(1 for v in self.values
                   if v == value)

    def surrounding(self, point: Coord, mark: str = '_') -> 'Grid':
        """Get a new grid with the surrounding points of the given point"""
        return Grid([[self.get(p) if p != point else mark for p in points]
                      for _, points in groupby(point.surrounding, key=lambda p: p.y)])


def pickable_paper_coords(grid: Grid, debug: bool = False) -> Iterator[Coord]:
    """Get all pickable paper coordinates"""
    for point in grid.all_coords:
        if grid.get(point) == '@' and grid.surrounding(point).count('@') < 4:
            if debug:
                print(f'Paper at {point} is pickable!')
            yield point

def count_pickable_papers(data: Iterator[str], debug: bool = False) -> int:
    """Count the number of pickable papers"""
    g = Grid.from_iter(data)
    if debug:
        print(g)
    return sum(1 for _ in pickable_paper_coords(g, debug))

def count_removed_papers(data: Iterator[str], debug: bool = False) -> int:
    """Count the number of removed papers"""
    total = 0
    g = Grid.from_iter(data)
    if debug:
        print(g)

    while True:
        pickable_papers = list(pickable_paper_coords(g, debug))
        if len(pickable_papers) == 0:
            break

        total += len(pickable_papers)
        for paper in pickable_papers:
            if debug:
                print(f'Removing {paper}')
            g.set(paper, '.')

        if debug:
            print(f'New grid:\n{g}')

    return total


if __name__ == '__main__':
    create_cli(4, part1=count_pickable_papers, part2=count_removed_papers)
