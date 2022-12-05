#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_str(self, code: str):
        if code == 'A' or code == 'X':
            return Shape.ROCK
        if code == 'B' or code == 'Y':
            return Shape.PAPER
        if code == 'C' or code == 'Z':
            return Shape.SCISSORS
        raise ValueError(f"Shape not recognized: {code}")


class Score(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def from_str(self, code: str):
        if code == 'X':
            return Score.LOSE
        if code == 'Y':
            return Score.DRAW
        if code == 'Z':
            return Score.WIN
        raise ValueError(f"Shape not recognized: {code}")


def parse_input(data: Iterator[str]) -> Iterator[tuple[Shape, Shape]]:
    """Parses Rock, Paper, Scissors notes (part 1)"""
    for line in data:
        if line.strip():
            a, b = line.strip().split(' ')
            yield (Shape.from_str(a), Shape.from_str(b))


def parse_input_part_2(data: Iterator[str]) -> Iterator[tuple[Shape, Score]]:
    """Parses Rock, Paper, Scissors notes new info (part 2)"""
    for line in data:
        if line.strip():
            a, b = line.strip().split(' ')
            yield (Shape.from_str(a), Score.from_str(b))


def calc_score(elve: Shape, player: Shape) -> int:
    """Score a Rock, Paper, Scissors game"""
    if elve == player:
        # Draw
        return Score.DRAW.value + player.value
    if (elve == Shape.ROCK and player == Shape.SCISSORS
        or elve == Shape.PAPER and player == Shape.ROCK 
        or elve == Shape.SCISSORS and player == Shape.PAPER):
        # Lose
        return Score.LOSE.value + player.value
    # Win
    return Score.WIN.value + player.value


def total_score_notes(data: Iterator[str]) -> int:
    """Score all games from given notes (part 1)"""
    return sum(calc_score(elve, player) for elve, player in parse_input(data))


def required_shape(elve: Shape, score: Score) -> Shape:
    if score == Score.DRAW:
        return elve

    if score == Score.LOSE:
        if elve == Shape.ROCK:
            return Shape.SCISSORS
        if elve == Shape.PAPER:
            return Shape.ROCK
        return Shape.PAPER

    # WIN
    if elve == Shape.ROCK:
        return Shape.PAPER
    if elve == Shape.PAPER:
        return Shape.SCISSORS
    return Shape.ROCK


def score_notes_new_info(data: Iterator[str]) -> int:
    """Score all games from given notes based on desired outcome (part 2)"""
    return sum(calc_score(elve, required_shape(elve, score))
               for elve, score in parse_input_part_2(data))


if __name__ == '__main__':
    create_cli(2, part1=total_score_notes, part2=score_notes_new_info)
