import re


def decode(string: str) -> str:
    """Run length decoding"""
    return ''.join(int(count or 1) * char
                   for count, char in re.findall(r'(\d*)(.)', string))


def encode(string: str) -> str:
    """Run length encoding"""
    return ''.join(str(len(rest) + 1) + char if len(rest) else char
                   for char, rest in re.findall(r'(.)(\1*)', string))
