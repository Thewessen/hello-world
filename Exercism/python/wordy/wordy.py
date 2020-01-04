import re

oper = {
    'plus': '+',
    'minus': '-',
    'multiplied by': '*',
    'divided by': '//',
}


def answer(question: str) -> int:
    """Solve simple word operations"""
    for op, o in oper.items():
        question = question.replace(op, o)
    q = re.match(r"^What is((:? -?\d+ \D{1,2})* -?\d+)\?$", question)
    if q is None:
        raise ValueError("No answer found")
    question = re.sub(r"(-?\d+ \D{1,2} -?\d+)", r"(\1)", q.group(1))
    return eval(question)
