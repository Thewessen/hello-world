class Queen:
    def __init__(self, row: int, column: int) -> object:
        if not 0 <= row < 8 or not 0 <= column < 8:
            raise ValueError("Wrong queen position")
        self.row = row
        self.column = column

    def can_attack(self, aq: object) -> bool:
        """Determine if this queen can attack another queen"""
        if self.row == aq.row and self.column == aq.column:
            raise ValueError("Same queen")
        return (self.row == aq.row
                or self.column == aq.column
                or self.row - self.column == aq.row - aq.column
                or self.row + self.column == aq.row + aq.column)
