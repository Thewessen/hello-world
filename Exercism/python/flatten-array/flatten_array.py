def flatten(iterable) -> list:
    arr = []
    for el in iterable:
        if isinstance(el, list) or isinstance(el, tuple):
            arr += flatten(el)
        elif el is not None:
            arr = [arr, el]
    return list(arr)

inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
print(flatten(inputs))
