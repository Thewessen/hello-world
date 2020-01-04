import re


def is_paired(input_string: str) -> bool:
    """Determine if any and all pairs are matched"""
    string = re.sub(r"[^(){}\]\[]*", "", input_string)
    pairs = re.compile(r"\(\)|\{\}|\[\]")
    while pairs.search(string) is not None:
        string = re.sub(pairs, "", string)
    return len(string) == 0
