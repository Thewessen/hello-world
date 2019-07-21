SCORES = dict()
for d in (dict.fromkeys('AEIOULNRST', 1),
          dict.fromkeys('DG', 2),
          dict.fromkeys('BCMP', 3),
          dict.fromkeys('FHVWY', 4),
          dict.fromkeys('K', 5),
          dict.fromkeys('JX', 8),
          dict.fromkeys('QZ', 10)):
    SCORES.update(d)


def score(word: str) -> int:
    """Computes the scrabble score for a given word."""
    return sum(SCORES[char] or 0 for char in word.upper())
