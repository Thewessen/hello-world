#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from more_itertools import consume
from operator import attrgetter
from collections import Counter
from copy import copy


class Dice:
    def __init__(self, mx, start = 1):
        self.max = mx
        self.next_roll = start

    def __iter__(self):
        return self
    
    def __next__(self):
        roll = self.next_roll
        self.next_roll += 1
        if self.next_roll > self.max:
            self.next_roll %= self.max
        return roll

    def __eq__(self, other):
        return (self.max == other.max
                and self.next_roll == other.next_roll)

    def __repr__(self):
        return f'Dice({self.next_roll} ({self.max}))'

    def __copy__(self):
        return Dice(self.max, self.next_roll)


class Board:
    def __init__(self, start: int):
        self.position = start

    def __repr__(self):
        return f'Board({self.position})'

    def __eq__(self, other):
        return self.position == other.position

    def __copy__(self):
        return Board(self.position)

    def move(self, roll):
        self.position += roll
        self.position %= 10
        if self.position == 0:
            self.position = 10
        return self.position


class Player:
    def __init__(self, dice: Dice, board: Board, score = 0):
        self.dice = dice
        self.board = board
        self.score = score

    def __repr__(self):
        return f'Player(score={self.score}, position={self.board.position}, dice={self.dice})'

    def __eq__(self, other):
        return (self.board == other.board
                and self.dice == other.dice
                and self.score == other.score)

    def __copy__(self):
        return Player(copy(self.dice), copy(self.board), self.score)


class DiceGame:
    def __init__(self, players: list[Player], turn = 0, roll_count = 0):
        self.players = players
        self.turn = turn
        self.roll_count = roll_count
        self.finished = False

    def __iter__(self):
        return self

    def switch_turns(self):
        self.turn += 1
        self.turn %= len(self.players)


class TestGame(DiceGame):
    def __repr__(self):
        return f'TestGame({self.roll_count}, {self.players})'

    def __next__(self):
        if self.finished:
            raise StopIteration('Game finished')
        player = self.players[self.turn]
        roll = next(player.dice)
        score = player.board.move(roll)
        self.roll_count += 1
        if self.roll_count % 3 == 0:
            player.score += score
            self.switch_turns()
        if player.score >= 1000:
            self.finished = True
            raise StopIteration('Game finished')

    @property
    def losing_player(self):
        return min(self.players, key=attrgetter('score'))

    @classmethod
    def from_iter(cls, data: Iterator[str]):
        dice = Dice(100)
        p1_start = int(next(data).split(' ')[-1])
        p2_start = int(next(data).split(' ')[-1])
        return cls([Player(dice, Board(p1_start)),
                    Player(dice, Board(p2_start))])


class Dirac(DiceGame):
    def __repr__(self):
        return f'Dirac({self.roll_count}, {self.players})'

    def __hash__(self):
        p1, p2 = self.players
        return hash((p1.board.position, p2.board.position, self.turn,
                     p1.dice.next_roll, p1.score, p2.score))

    def __eq__(self, other):
        return all(p1 == p2 for p1, p2 in zip(self.players, other.players))

    def __next__(self):
        if self.finished:
            raise StopIteration('Game finished')
        player = self.players[self.turn]
        roll = next(player.dice)
        score = player.board.move(roll)
        self.roll_count += 1
        if self.roll_count % 3 == 0:
            player.score += score
            if player.score >= 21:
                self.finished = True
                raise StopIteration('Game finished')
            self.switch_turns()

    def multivers(self):
        for i in range(1, 4):
            g = self.clone(i)
            if g != self:
                yield g

    def __copy__(self):
        p1, p2 = self.players
        new_p1, new_p2 = (copy(p1), copy(p2))
        return Dirac([new_p1, new_p2], self.turn, self.roll_count)

    def clone(self, dice_start):
        dice = Dice(3, dice_start)
        game = copy(self)
        for player in game.players:
            player.dice = dice
        return game

    @classmethod
    def from_iter(cls, data: Iterator[str]):
        dice = Dice(3)
        p1_start = int(next(data).split(' ')[-1])
        p2_start = int(next(data).split(' ')[-1])
        return cls([Player(dice, Board(p1_start)),
                    Player(dice, Board(p2_start))])


def play_test_game(data: Iterator[str]) -> int:
    game = TestGame.from_iter(data)
    consume(game)
    return game.roll_count * game.losing_player.score


def calc_winning_universe(games: Counter) -> int:
    universes = Counter()
    for game, count in games.items():
        universes.update({ game.turn: count })
    return max(universes.values())


def play_real_game(data: Iterator[str]) -> int:
    game = Dirac.from_iter(data)
    games = Counter({game})
    while True:
        new_games = Counter()
        for game, count in games.items():
            if game.finished:
                continue
            new_games.update({g: count
                              for g in game.multivers()})
        if len(new_games) == 0:
            break
        games.update(new_games)
        for game in games:
            if game.finished:
                continue
            try:
                next(game)
            except StopIteration:
                continue
    return calc_winning_universe(games)


def main():
    parser = ArgumentParser(description="Day 21 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open('./input', 'r') as data:
        if args.part2:
            r = play_real_game(data)
        else:
            r = play_test_game(data)
    print(r)


if __name__ == '__main__':
    main()
