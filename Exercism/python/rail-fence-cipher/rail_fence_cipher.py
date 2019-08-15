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
    length = range(len(encoded_message))
    look_up = encode((chr(i) for i in length), rails)
    return ''.join(encoded_message[look_up.index(chr(i))] for i in length)
