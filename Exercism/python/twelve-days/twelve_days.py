PRESENTS = [
    'a Partridge in a Pear Tree',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
]

NUMBERS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]


def recite(start_verse: int, end_verse: int) -> list:
    """Outputs the lyrics to 'The Twelve Days of Christmas'."""
    verse = []
    for i in range(start_verse, end_verse + 1):
        verse.append(f'On the {NUMBERS[i-1]} day of Christmas'
                     ' my true love gave to me: '
                     f'{", ".join(PRESENTS[i-1:0:-1])}'
                     f'{", and " if i > 1 else ""}'
                     f'{PRESENTS[0]}.')
    return verse
