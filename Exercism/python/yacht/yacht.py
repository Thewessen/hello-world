def score(dice: list, scr: object) -> int:
    """Calls corresponding scoring function."""
    return scr(dice)


def _score_dice(score: object, check: object = None) -> object:
    """Little helper function"""
    def scr(dice):
        if check is None or check(dice):
            if isinstance(score, int):
                return score
            return score(dice)
        return 0
    return scr


YACHT = _score_dice(50, check=lambda dice: len(set(dice)) == 1)
CHOICE = _score_dice(lambda dice: sum(dice))
ONES = _score_dice(lambda dice: dice.count(1) * 1)
TWOS = _score_dice(lambda dice: dice.count(2) * 2)
THREES = _score_dice(lambda dice: dice.count(3) * 3)
FOURS = _score_dice(lambda dice: dice.count(4) * 4)
FIVES = _score_dice(lambda dice: dice.count(5) * 5)
SIXES = _score_dice(lambda dice: dice.count(6) * 6)
LITTLE_STRAIGHT = _score_dice(
        30, lambda dice: all(n in dice for n in range(1, 6)))
BIG_STRAIGHT = _score_dice(
        30, lambda dice: all(n in dice for n in range(2, 7)))
FULL_HOUSE = _score_dice(
    lambda dice: sum(dice),
    lambda dice: all(dice.count(d) == 2 or dice.count(d) == 3
                     for d in set(dice))
)
FOUR_OF_A_KIND = _score_dice(
    lambda dice: sum(4 * d if dice.count(d) >= 4 else 0 for d in set(dice)),
    lambda dice: any(dice.count(d) >= 4 for d in set(dice))
)
