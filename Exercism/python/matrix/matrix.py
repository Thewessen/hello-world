class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [[int(cell) for cell in row.split(' ')]
                        for row in matrix_string.split('\n')]

    @property
    def matrix(self):
        return [row[:] for row in self._matrix]

    def row(self, index):
        return [cell for cell in self.matrix[index - 1]]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
