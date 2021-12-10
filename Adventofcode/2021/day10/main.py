#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
import re


def remove_matching(chunk: str) -> tuple[str, str]:
    """Strips a chunk from matching open and closing characters.
    Returns the rest of the chunk, inc. the first nonmatching closing
    character."""
    brackets = r'\(\)|\[\]|\{\}|\<\>'

    while re.search(brackets, chunk):
        chunk = re.sub(brackets, '', chunk)

    if re.search(r'\[\)|\{\)|\<\)', chunk):
        return chunk, ')'
    if re.search(r'\(\]|\{\]|\<\]', chunk):
        return chunk, ']'
    if re.search(r'\(\}|\[\}|\<\}', chunk):
        return chunk, '}'
    if re.search(r'\(\>|\[\>|\{\>', chunk):
        return chunk, '>'

    return chunk, ''


def syntax_error_score(data: Iterator[str]) -> int:
    """Calculates the score of syntax errors in all chunks of code.
    (see README part 1."""
    parsed = (remove_matching(line) for line in data)
    return sum({
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }[char] for _, char in parsed if char != '')


def autocomplete(seq: str) -> str:
    """Completes an incomplete chunk of characters.
    Returns the completion"""
    table = seq.maketrans('([{<', ')]}>', ')]}>')
    return seq.translate(table)[::-1]


def score_completion(seq: str) -> int:
    """The score of each completion is calculate. (see README part 2)"""
    score = 0
    for char in seq:
        score *= 5
        score += { ')': 1, ']': 2, '}': 3, '>': 4 }[char]
    return score


def completion_winner(scores: Iterator[int]) -> int:
    """The middle completion of all completion scores has the best completion.
    (see README part 2)"""
    sort = sorted(scores)
    return sort[int(len(sort) / 2)]


def autocomplete_score(data: Iterator[str]) -> int:
    """Calculates the score of autocompletion after chunks of data are
    evaluated. (see README part 2)"""
    evaluation = (remove_matching(line.strip()) for line in data)
    incomplete = (chunk for chunk, char in evaluation if char == '')
    completions = (autocomplete(line) for line in incomplete)
    return completion_winner(score_completion(c) for c in completions)


def main():
    parser = ArgumentParser(description="Day 10 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = autocomplete_score(data)
        else:
            r = syntax_error_score(data)
    print(r)


if __name__ == '__main__':
    main()
