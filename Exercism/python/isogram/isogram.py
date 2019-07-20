from string import ascii_lowercase


def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram."""
    letters = [char for char in string.lower()
               if char in ascii_lowercase]
    return len(set(letters)) == len(letters)
