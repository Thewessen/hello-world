def square_of_sum(number: int) -> int:
    """Calc square of sum of numbers"""
    return sum(range(number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Calc sum of squares of numbers"""
    return sum(map(lambda n: n ** 2, range(number + 1)))


def difference_of_squares(number: int) -> int:
    """Calc diff between sum of squares and square of sum"""
    return abs(sum_of_squares(number) - square_of_sum(number))
