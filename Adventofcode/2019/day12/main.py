#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from dataclasses import dataclass
from more_itertools import consume
from numpy import lcm
from typing import Iterator


@dataclass
class Coord:
    x: int
    y: int
    z: int
    
    def __add__(self, other):
        return Coord(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"C({self.x}, {self.y}, {self.z})"


class Moon:
    def __init__(self, pos: Coord, velo = Coord(0, 0, 0)):
        self.position = pos
        self.velocity = velo

    def __eq__(self, other):
        return (self.position == other.position and
                self.velocity == other.velocity)

    @property
    def potential_energy(self):
        return (abs(self.position.x) +
                abs(self.position.y) +
                abs(self.position.z))

    @property
    def kinetic_energy(self):
        return (abs(self.velocity.x) +
                abs(self.velocity.y) +
                abs(self.velocity.z))

    @property
    def energy(self):
        return (self.potential_energy *
                self.kinetic_energy)

class Jupiter:
    def __init__(self, moons: list[Moon]):
        self.moons = moons

    def __iter__(self):
        return self

    def __next__(self):
        deltas = [Coord(
            sum(cmp(moon.position.x, m.position.x) for m in self.moons),
            sum(cmp(moon.position.y, m.position.y) for m in self.moons),
            sum(cmp(moon.position.z, m.position.z) for m in self.moons)
        ) for moon in self.moons]

        for moon, delta in zip(self.moons, deltas):
            moon.velocity += delta
            moon.position += moon.velocity

    @property
    def energy(self):
        return sum(moon.energy for moon in self.moons)

    @property
    def positions(self):
        # For easier testing
        return [moon.position for moon in self.moons]

    @property
    def velocities(self):
        # For easier testing
        return [moon.velocity for moon in self.moons]

    @property
    def period(self):
        return lcm.reduce([
            self._get_period('x'),
            self._get_period('y'),
            self._get_period('z')
        ])

    def _get_period(self, axis: str) -> int:
        io, europa, ganymede, callisto = self.moons
        state = [(getattr(io.position, axis), getattr(io.velocity, axis)),
                 (getattr(europa.position, axis), getattr(europa.velocity, axis)),
                 (getattr(ganymede.position, axis), getattr(ganymede.velocity, axis)),
                 (getattr(callisto.position, axis), getattr(callisto.velocity, axis))]

        states = set([hash_state(state)])
        count = 0
        while True:
            count += 1
            new_state = list()
            for pos, velo in state:
                v = sum(cmp(pos, po) for po, _ in state)
                new_state.append((pos + velo + v, velo + v))
            nsh = hash_state(new_state)
            if nsh in states:
                return count
            states.add(nsh)
            state = new_state


def hash_state(s: list[tuple[int, int]]) -> int:
    rep = ''
    for moon in s:
        rep += ''.join(str(n) for n in moon)
    return hash(rep)


def parse_input(data: Iterator[str]) -> Jupiter:
    """Creates Jupiter representive from input data."""
    positions = (eval('Coord' + line.strip()
                                    .replace('<', '(')
                                    .replace('>', ')'))
                 for line in data)
    return Jupiter([Moon(pos) for pos in positions])


def cmp(a: int, b: int) -> int:
    return (b > a) - (b < a)


def part_1(data: Iterator[str]) -> int:
    """Solution part 1, calculate the energy of Jupiter state after 1000 ticks
       (see Readme)"""
    jupiter = parse_input(data)
    consume(jupiter, 1000)
    return jupiter.energy


def part_2(data: Iterator[str]) -> int:
    """Solution part 2, calculate the period of Jupiter state. The time it
    takes to return to its original state. (see Readme)"""
    jupiter = parse_input(data)
    return jupiter.period


if __name__ == '__main__':
    create_cli(12, part1=part_1, part2=part_2)
