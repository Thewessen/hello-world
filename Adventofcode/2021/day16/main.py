#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from dataclasses import dataclass, field
from more_itertools import take
from itertools import islice
from math import prod


@dataclass
class Packet:
    """The base Packet data class."""
    version: int
    type_id: int
    value: int = field(init=False, default=0)


@dataclass
class OperatorPacket(Packet):
    """The base operator packet class. Contains the logic for building operator
    packets."""
    subpackets: list = field(init=False, default_factory=lambda: [])
    
    def build(self, bin_stream: Iterator[str]):
        mode = next(bin_stream)
        if mode == '0':
            length = bits_value(15, bin_stream)
            subpackets = islice(bin_stream, 0, length)
            while True:
                try:
                    packet = PacketFactory(subpackets)
                    self.subpackets.append(packet)
                except StopIteration:
                    break
        if mode == '1':
            length = bits_value(11, bin_stream)
            for _ in range(length):
                try:
                    packet = PacketFactory(bin_stream)
                    self.subpackets.append(packet)
                except StopIteration:
                    break
        return self

    def version_sum(self):
        """see README part 1"""
        return self.version + sum(packet.version_sum()
                                  for packet in self.subpackets)


@dataclass
class SumPacket(OperatorPacket):
    """An operator packet where it's value is the sum of all subpackets
    value."""
    type_id: int = field(init=False, default=0)

    @property
    def value(self):
        return sum(packet.value for packet in self.subpackets)


@dataclass
class ProductPacket(OperatorPacket):
    """An operator packet where it's value is the product of all subpackets
    value."""
    type_id: int = field(init=False, default=1)

    @property
    def value(self):
        return prod(packet.value for packet in self.subpackets)


@dataclass
class MinimumPacket(OperatorPacket):
    """An operator packet where it's value is the minimum value of
    all subpackets value."""
    type_id: int = field(init=False, default=2)

    @property
    def value(self):
        return min(packet.value for packet in self.subpackets)


@dataclass
class MaximumPacket(OperatorPacket):
    """An operator packet where it's value is the maximum value of
    all subpackets value."""
    type_id: int = field(init=False, default=3)

    @property
    def value(self):
        return max(packet.value for packet in self.subpackets)


@dataclass
class GreaterThanPacket(OperatorPacket):
    """An operator packet where it's value is an integer representation
    of the condition where the value of the first subpacket is greater than
    the value of the second subpacket."""
    type_id: int = field(init=False, default=5)

    @property
    def value(self):
        return int(self.subpackets[0].value > self.subpackets[1].value)


@dataclass
class LessThanPacket(OperatorPacket):
    """An operator packet where it's value is an integer representation
    of the condition where the value of the first subpacket is less than
    the value of the second subpacket."""
    type_id: int = field(init=False, default=6)

    @property
    def value(self):
        return int(self.subpackets[0].value < self.subpackets[1].value)


@dataclass
class EqualToPacket(OperatorPacket):
    """An operator packet where it's value is an integer representation
    of the condition where the value of the first subpacket is equal to
    the value of the second subpacket."""
    type_id: int = field(init=False, default=7)

    @property
    def value(self):
        return int(self.subpackets[0].value == self.subpackets[1].value)


@dataclass
class LiteralPacket(Packet):
    """A literal packet class. Contains the logic for building a literal
    packet."""
    type_id: int = field(init=False, default=4)

    def build(self, bin_stream: Iterator[str]):
        while True:
            first_bit = next(bin_stream)
            self.value <<= 4
            self.value += bits_value(4, bin_stream)
            if first_bit == '0':
                break
        return self

    def version_sum(self):
        """see README part 1"""
        return self.version


def hex_to_bin_stream(hex_str: str) -> Iterator[str]:
    """Helper function converting a hex string to bit stream."""
    for h in hex_str.strip():
        v = int(h, 16)
        yield from f'{v:04b}'


def PacketFactory(bin_stream: Iterator[str]):
    """Creates a single packet out of a bit stream. Discards left over bits."""
    try:
        version = bits_value(3, bin_stream)
    except ValueError:
        raise StopIteration
    type_id = bits_value(3, bin_stream)

    return {
        0: SumPacket,
        1: ProductPacket,
        2: MinimumPacket,
        3: MaximumPacket,
        4: LiteralPacket,
        5: GreaterThanPacket,
        6: LessThanPacket,
        7: EqualToPacket,
    }[type_id](version).build(bin_stream)


def parse_packet(data: Iterator[str]):
    hex_stream = next(data).strip()
    bin_stream = hex_to_bin_stream(hex_stream)
    return PacketFactory(bin_stream)


def bits_value(count: int, bin_stream: Iterator[str]) -> int:
    return int(''.join(take(count, bin_stream)), 2)


def main():
    parser = ArgumentParser(description="Day 16 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            packet = parse_packet(data)
            print(packet.value)
        else:
            packet = parse_packet(data)
            print(packet.version_sum())


if __name__ == '__main__':
    main()
