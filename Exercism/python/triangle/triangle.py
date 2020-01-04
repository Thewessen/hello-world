def valid(sides: list) -> bool:
    """Test if triangle is valid"""
    a, b, c = sorted(sides)
    return min(sides) > 0 and a + b > c


def equilateral(sides: int) -> bool:
    """Test if triangle is equilateral"""
    return len(set(sides)) == 1 and valid(sides)


def isosceles(sides: int) -> bool:
    """Test if triangle is isosceles"""
    return len(set(sides)) < 3 and valid(sides)


def scalene(sides: int) -> bool:
    """Test if triangle is scalene"""
    return len(set(sides)) == 3 and valid(sides)
