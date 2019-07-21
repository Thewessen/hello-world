import re


def abbreviate(words: str) -> str:
    """Converts a phrase to its acronym."""
    return ''.join(re.findall(r"([A-Z])(?:[A-Z']+)?", words.upper()))
