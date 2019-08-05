from string import ascii_lowercase, ascii_uppercase, ascii_letters


def rotate(text: str, key: int) -> str:
    """Caesar ROT Cipher"""
    def s(chars):
        return chars[key:] + chars[:key]
    table = str.maketrans(
                ascii_letters,
                s(ascii_lowercase) + s(ascii_uppercase)
            )
    return text.translate(table)
