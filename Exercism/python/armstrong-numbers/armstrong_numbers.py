def is_armstrong_number(number: int) -> bool:
    """Checks if a number is an Armstrong number."""
    n = str(number)
    return sum(int(d) ** len(n) for d in n) == number
