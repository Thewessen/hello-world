def closing_parants(count: int) -> str:
    """Returns a string of {count} matching open and closing parants"""
    # return '{' * count + '}' * count
    return wrap_parants("", count)


def wrap_parants(word: str, count: int) -> str:
    """Wraps a {word} in {count} parantheses"""
    return word if count == 0 else \
        wrap_parants('{' + word + '}', count - 1)


print(closing_parants(5))
