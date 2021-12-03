#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Tuple
from functools import reduce
from more_itertools import nth

def calc_bit_balance(acc: int, curr: str) -> int:
    """Reducer function to convert an iterable of bits to a positive or
    negetave number, resp. more '1' bits or '0' bits."""
    if curr == '1':
        return acc + 1
    return acc - 1


def gamma_epsilon_bits(balance: int) -> Tuple[int, int]:
    """Separates a given balance into gamma and epsilon bits resp."""
    if balance > 0:
        return 1, 0
    elif balance < 0:
        return 0, 1
    print("Don't know what to do if '1' and '0' bits have equal significance")
    exit(1)


def calc_gamma_epsilon_bin(acc: Tuple[str, str], curr: Tuple[int, int]) -> Tuple[str, str]:
    """Reducer function converting a gamma_bit, epsilon_bit tuple iterable into their
    corresponding binary string tuple"""
    gamma, epsilon = acc
    gb, eb = curr
    return gamma + str(gb), epsilon + str(eb)


def calc_gamma_epsilon_rate(data: Iterator[str]) -> Tuple[int, int]:
    """Given lines of binary string, returns the gamma-, epsilon-rates as tuple."""
    bit_balance = (reduce(calc_bit_balance, position, 0)
                   for position in zip(*data))
    gamm_eps_bits = map(gamma_epsilon_bits, bit_balance)
    gamma_bin, epsilon_bin = reduce(calc_gamma_epsilon_bin, gamm_eps_bits, ('', '')) 
    return int(gamma_bin, 2), int(epsilon_bin, 2)


def filter_by_criteria(data: list[str], criteria, poss=0) -> str:
    """With a given criteria for bit vs. corresponding bit_balance (1 or 0),
    keeps filtering until one line of data is left."""
    if len(data) == 1:
        return data[0]

    position = nth(zip(*data), poss)
    if position is None:
        print('No solution found, terminating...')
        exit(1)

    bit_balance = reduce(calc_bit_balance, position, 0)
    return filter_by_criteria(
               list(filter(lambda b: criteria(b[poss], bit_balance), data)),
               criteria,
               poss + 1)


def oxygen_criteria(position_bit: str, balance: int) -> bool: 
    """Criteria for a valid oxygen binary, given its current possitional bit
    and corresponding bit balance"""
    return int(position_bit) == int(balance >= 0)


def co2_criteria(position_bit: str, balance: int) -> bool: 
    """Criteria for a valid co2 binary, given its current possitional bit
    and corresponding bit balance"""
    return int(position_bit) == int(balance < 0)


def calc_oxygen_co2_rate(data: list[str]) -> Tuple[int, int]:
    """Given lines of binary string, returns the oxygen-, co2-rates as tuple."""
    oxygen_bit = filter_by_criteria(data, oxygen_criteria)
    co2_bit = filter_by_criteria(data, co2_criteria)
    return int(oxygen_bit, 2), int(co2_bit, 2)


def main():
    parser = ArgumentParser(description="Day 2 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            rates = calc_oxygen_co2_rate(data.readlines())
        else:
            rates = calc_gamma_epsilon_rate(data)
        print(rates[0] * rates[1])


if __name__ == '__main__':
    main()
