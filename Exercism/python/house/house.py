words = [
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def verse(nr: int) -> str:
    """One verse of the famous house song"""
    return ("This is the " +
            (''.join(f"{w[0]} that {w[1]} the " for w in words[nr-2::-1])
             if nr > 1 else '') +
            "house that Jack built.")


def recite(start_verse: int, end_verse: int) -> list:
    """Recite verses of the famous house song"""
    return [verse(n) for n in range(start_verse, end_verse + 1)]
