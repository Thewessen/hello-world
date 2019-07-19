SOUNDS = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}


def convert(number: int) -> str:
    """A raindrops song composed of different sounds"""
    return ''.join(SOUNDS[n] for n in SOUNDS if number % n == 0) \
        or str(number)
