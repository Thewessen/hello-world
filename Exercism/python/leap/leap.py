def leap_year(year: int) -> bool:
    """Given a year, report if it is a leap year."""
    return year % 4 == 0 and \
           (year % 100 != 0 or year % 400 == 0)
