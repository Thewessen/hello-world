import re


def count_words(sentence: str) -> dict:
    """Counts the occurrences of each word in a phrase."""
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    return {
        wrd: words.count(wrd)
        for wrd in set(words)
    }
