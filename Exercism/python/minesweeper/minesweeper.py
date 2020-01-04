def annotate(minefield: list) -> list:
    """Creates annotations for minesweeper field"""
    if len(minefield) == 0:
        return minefield
    width = max(len(row) for row in minefield)
    if width == 0:
        return minefield
    if not all(len(row) == width for row in minefield):
        raise ValueError("Minefield not a rectangle")
    annotated = ''
    for i, row in enumerate(minefield):
        for j, field in enumerate(row):
            if field not in ' *':
                raise ValueError("None bomb found")
            if field == '*':
                annotated += field
                continue
            sur = (row[max(j - 1, 0):min(j + 2, len(row))] for row in
                   minefield[max(i - 1, 0):min(i + 2, len(minefield))])
            mines = ''.join(sur).count('*')
            annotated += ' ' if mines == 0 else str(mines)
    return [annotated[i:i+width] for i in range(0, len(annotated), width)]
