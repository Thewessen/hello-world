ROMAN_NUMBERS = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
}


def roman(number: int) -> str:
    """Converts normal number to Roman Numerals."""
    result = ''
    for roman, arabic in ROMAN_NUMBERS.items():
        count, number = divmod(number, arabic)
        result += roman * count
    return result
