def flatten(iterable) -> list:
    lst = []
    for el in iterable:
        if isinstance(el, list) or isinstance(el, tuple):
            lst += flatten(el)
        elif el is not None:
            lst += [el]
    return lst
