from itertools import product


def is_matrix(matrix: list) -> bool:
    """Checks if twodimensional list has equal width and height"""
    try:
        width = len(matrix[0])
    except IndexError:
        return True
    return all(len(row) == width for row in matrix[1:])


def saddle_points(matrix: list) -> list:
    """Lists all saddlepoints of given matrix"""
    if not is_matrix(matrix):
        raise ValueError("Error: not a matrix")

    rows = range(len(matrix))
    columns = range(len(matrix[0]) if len(matrix) > 0 else 0)

    return [{"row": i + 1, "column": j + 1}
            for i, j in product(rows, columns)
            if matrix[i][j] == max(matrix[i])
            and matrix[i][j] == min(row[j] for row in matrix)]
