from string import ascii_lowercase, punctuation, whitespace

TABLE = str.maketrans(
    ascii_lowercase,
    ascii_lowercase[::-1],
    punctuation + whitespace)


def encode(plain_text: str) -> str:
    """Atbash decipher"""
    text = plain_text.lower().translate(TABLE)
    return ' '.join(text[i:i+5] for i in range(0, len(text), 5))


def decode(ciphered_text: str) -> str:
    """Atbash cipher"""
    return ciphered_text.translate(TABLE)
