def deviders(number: int) -> int:
    """Generates all deviders for a given number"""
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            yield i


def classify(number: int) -> str:
    """Determine the class of a number"""
    if number <= 0:
        raise ValueError("Error: positive integer required")
    aliquot_sum = sum(deviders(number))
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
        return "deficient"
