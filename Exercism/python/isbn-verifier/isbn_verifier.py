import re


def is_valid(isbn: str) -> bool:
    """ISBN Verifier"""
    isbn = isbn.replace('-', '')
    if re.match(r'^\d{9}[0-9X]$', isbn) is None:
        return False
    return sum(int(n) * (i + 1) if n != 'X' else 10 * (i + 1)
               for i, n in enumerate(isbn[::-1])) % 11 == 0
