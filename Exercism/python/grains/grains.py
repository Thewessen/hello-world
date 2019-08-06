def square(number: int) -> int:
    """Calculate the number of grains of wheat on
    a square of the chessboard."""
    if type(number) is not int or number <= 0 or number > 64:
        raise ValueError('Invalid square count')
    return 2 ** (number - 1)


def total(number: int) -> int:
    """Calculate the total number of grains of wheat on a chessboard
    with `number` squares."""
    if type(number) is not int or number <= 0 or number > 64:
        raise ValueError('Invalid square count')
    return sum(2 ** n for n in range(number))
