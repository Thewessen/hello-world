def find_anagrams(word: str, candidates: list) -> list:
    """Given a word and a list of possible anagrams,
    selects the correct sublist."""
    return [w for w in candidates if
            w.lower() != word.lower() and
            sorted(w.lower()) == sorted(word.lower())]
