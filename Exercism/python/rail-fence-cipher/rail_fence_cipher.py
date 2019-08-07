def encode(message: str, rails: int) -> str:
    """Encoding for the rail fence cipher."""
    delta = 1
    code = [''] * rails
    index = 0
    for char in message:
        code[index] += char
        index += delta
        if index == rails - 1 or index == 0:
            delta *= -1
    return ''.join(code)


def decode(encoded_message: str, rails: int) -> str:
    """Decoding for the rail fence cipher."""
    delta = 1
    decode = ''
    index = 0
    for char in message:
        code += char
        index += delta
        if index == rails - 1 or index == 0:
            delta *= -1
    return ''.join(code)

print(encode('WEAREDISCOVEREDFLEEATONCE', 3))


"""
? . . . . . . . ? . . . . . . . ? . . . . . . . ?
. ? . . . . . ? . ? . . . . . ? . ? . . . . . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
. . . ? . ? . . . . . ? . ? . . . . . ? . ? . . .
. . . . ? . . . . . . . ? . . . . . . . ? . . . .
"""
