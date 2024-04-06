#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Iterable, Optional
from dataclasses import dataclass, field
from itertools import chain, islice, count
from operator import attrgetter


@dataclass
class Range:
    start: int
    length: int

    def __contains__(self, item: int):
        """Check if item is in range"""
        return self.start <= item < self.start + self.length


@dataclass
class Mapping:
    tar: Range
    dest: Range

    def reverse(self) -> Self:
        """Reverse the mappings tar and dest"""
        return Mapping(self.dest, self.tar)

    def __getitem__(self, key: int|Range):
        """Map item or Range"""
        if key not in self.tar:
            return key

        if isinstance(key, Range):
            if key.start not in self and (key.start + key.length) not in self:
                        # head not in mapping
                return (Range(key.start, self.tar.start - key.start),
                        # full mapping overlap
                        self.dest,
                        # tail not in mapping
                        Range(self.tar.start + self.tar.length,
                              (key.start + key.length) - (self.tar.start + self.tar.length)))
            if key.start in self and (key.start + key.length) not in self:
                        # head in mapping
                return (Range(self.dest.start + self.tar.start - key.start,
                              key.length - ((key.start + key.length) - (self.tar.start + self.tar.length))),
                        # tail not in mapping
                        Range(self.tar.start + self.tar.length,
                              (key.start + key.length) - (self.tar.start + self.tar.length)))
            if key.start not in self and (key.start + key.length) in self:
                        # head not in mapping
                return (Range(key.start, self.tar.start - key.start),
                        # tail in mapping
                        Range(key.start, key.length - (self.tar.start - key.start)))
            if key.start in self and (key.start + key.length) in self:
                # all key ranges in mapping
                return (Range(self.dest.start + (key.start - self.tar.start), key.length))

        return self.dest.start + key - self.tar.start

    def __repr__(self):
        """Get string representation"""
        return f"{self.dest.start} {self.tar.start} {self.tar.length}"


@dataclass
class Map:
    type: str
    ranges: list[Mapping] = field(default_factory=list)

    def reverse(self) -> Self:
        """Reverse the maps tar and dest"""
        return Map(self.type, [map.reverse() for map in self.ranges]) 

    def add_range(self, mapping: Mapping):
        """Add a range to the map"""
        self.ranges.append(mapping)

    def __getitem__(self, key: int):
        """Get corresponding destination number"""
        for mapping in self.ranges:
            if key in mapping:
                return mapping[key]
        return key
    
    def __repr__(self):
        """Get string representation"""
        return f"<Map type={self.type} ranges={self.ranges}>"


@dataclass
class GardingPlan:
    seeds: list[int]
    maps: list[Map]= field(default_factory=list)
    rev_maps: list[Map] = field(init=False)

    def find_location(self, seed: int|list[Range]) -> int|list[Range]:
        """Find the location of the seed"""
        if isinstance(seed, list) and all(isinstance(s, Range) for s in seed):
            for m in self.maps:
                print(m[seed])
                # seed = [s for seed in seed for s in m[seed]]
        elif isinstance(seed, int):
            for m in self.maps:
                seed = m[seed]
        return seed

    def find_nth_lowest_location_seed(self, n = 0) -> Optional[int]:
        if not hasattr(self, 'rev_maps'):
            self.rev_maps = [m.reverse() for m in reversed(self.maps)]

        # nth lowest location
        rev_maps = iter(self.rev_maps)
        map = next(rev_maps)
        if map is None:
            raise ValueError('No map in mappings')
        lowest_mappings = sorted(map.ranges, key=attrgetter('tar'))
        if n < lowest_mappings[0].tar:
            lowest_dest = n
        else:
            for m in lowest_mappings:
                if n in m:
                    lowest_dest = m[n]
            # for map in ordered_mappings:
            # nth_lowest_mapping = ordered_mappings[n]].destordernext(islice(ordered_mappings_iter, n, None))
            # lowest_dest = nth_lowest_mapping.dest

        # print(f'{map}: {lowest_dest}')
        for map in rev_maps:
            # print(f'{map}: {lowest_dest}')
            lowest_dest = map[lowest_dest]

        # print(f'{self}: {lowest_dest}')
        for start, length in zip(self.seeds[::2], self.seeds[1::2]):
            if start <= lowest_dest < start + length:
                return lowest_dest
        
    def find_lowest_location_seed(self) -> Optional[int]:
        """Find the seed with the lowest location"""
        return None

    def __repr__(self):
        """Get string representation"""
        if hasattr(self, 'rev_maps'):
            return f"<GardingPlan seeds={self.seeds} maps={self.maps} rev_maps={self.rev_maps}>"
        return f"<GardingPlan seeds={self.seeds} maps={self.maps}>"

    @classmethod
    def from_data(cls, data: Iterator[str]):
        seeds = []
        maps = []
        for line in data:
            if line.startswith('seeds'):
                seeds = [int(c) for c in line.split(':')[1].strip().split(' ')]
            elif line.strip().endswith('map:'):
                t = line.split(' ')[0]
                maps.append(Map(t))
            elif line.strip() == '':
                continue
            else:
                dest, tar, length = [int(c) for c in line.strip().split(' ')]
                maps[-1].add_range(Mapping(Range(tar, length),
                                           Range(dest, length)))

        return cls(seeds, maps)


def lowest_seed_location(data: Iterator[str], debug = False) -> int:
    """Find the lowest seed location for the puzzle input"""
    plan = GardingPlan.from_data(data)
    if debug:
        print(plan)

    return min(plan.find_location(s) for s in plan.seeds)

# def ranged_seed_lowest_location(data: Iterator[str], debug = False) -> int:
#     """Find the lowest seed location for the puzzle input"""
#     plan = GardingPlan.from_data(data)

#     lowest_seed = None
#     for n in count(22562319):
#         print(n)
#         lowest_seed = plan.find_nth_lowest_location_seed(n)
#         if lowest_seed is not None:
#             return lowest_seed

def ranged_seed_lowest_location(data: Iterator[str], debug = False) -> int:
    """Find the lowest seed location for the puzzle input"""
    plan = GardingPlan.from_data(data)
    if debug:
        print(plan)

    seeds = [Range(start, length)
             for start, length in zip(plan.seeds[::2], plan.seeds[1::2])]

    print(plan.find_location(seeds))
    # lowest_seed = None
    # lowest_loc = None
    # for seed in chain(*seeds):
    #     loc = plan.find_location(seed)
    #     print(f'{seed} -> {loc}')
    #     if lowest_loc is None or loc < lowest_loc:
    #         lowest_loc = loc
    #         lowest_seed = seed
    #         print('LOWEST')

    return 0
    # return min(chain(*seeds), key=lambda s: plan.find_location(s))

# def ranged_seed_lowest_location(data: Iterator[str], debug = False) -> int:
#     """Find the lowest seed location for the puzzle input"""
#     plan = GardingPlan.from_data(data)

#     lowest_seed = None
#     for n in count(22562319):
#         print(n)
#         lowest_seed = plan.find_nth_lowest_location_seed(n)
#         if lowest_seed is not None:
#             return lowest_seed

if __name__ == '__main__':
    create_cli(5, part1=lowest_seed_location, part2=ranged_seed_lowest_location)
