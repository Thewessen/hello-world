ocr = (
    (" _ ", "| |", "|_|", "   "),
    ("   ", "  |", "  |", "   "),
    (" _ ", " _|", "|_ ", "   "),
    (" _ ", " _|", " _|", "   "),
    ("   ", "|_|", "  |", "   "),
    (" _ ", "|_ ", " _|", "   "),
    (" _ ", "|_ ", "|_|", "   "),
    (" _ ", "  |", "  |", "   "),
    (" _ ", "|_|", "|_|", "   "),
    (" _ ", "|_|", " _|", "   ")
)


def cut(row: str) -> iter:
    """Groups string by three chars"""
    return (row[i:i+3] for i in range(0, len(row), 3))


def convert(input_grid: list) -> str:
    """Converts ocr number into digit string representation"""
    numbers = list()
    for i in range(0, len(input_grid), 4):
        result = ''
        for number in zip(*map(cut, input_grid[i:i+4])):
            if len(number) != 4 or not all(len(row) == 3 for row in number):
                raise ValueError("Invalid grid")
            try:
                result += str(ocr.index(number))
            except ValueError:
                result += '?'
        numbers.append(result)
    return ','.join(numbers)
