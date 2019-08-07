import math


def normalize(text: str) -> str:
    """Normalizes a str (lowercase, only alphabetic chars ond digits)"""
    return ''.join(char.lower() for char in text
                   if char.isalpha() or char.isdigit())


def cipher_text(plain_text: str) -> str:
    """Creates a secret messages called a square code."""
    text = normalize(plain_text)
    sqr = math.sqrt(len(text))
    rows = math.ceil(sqr)
    columns = round(sqr)
    return ' '.join(f'{row:<{columns}}' for row in
                    (text[i::rows] for i in range(rows)))
