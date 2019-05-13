"""Construct tables ready for printing data into nice table-like output.
Nested tables, and cells containing multiple lines, are allowed!
Exports class Table()"""

from itertools import zip_longest

__all__ = ["Table"]


class _Cell:
    """Generates objects for the Table class. Each Table is a
    two-dimensional row containing Cell-objects"""

    def __init__(self, value, max_width=None):
        """Set value and calculates the max_width and height"""
        if max_width is None:
            self.value = value
        else:
            value = self.set_max_width(value, max_width)
        self._max_width = max_width
        self._height = len(str(value).split('\n'))

    def __repr__(self):
        """Representation of this object"""
        return "<Cell object: value='{}'>"\
               .format(self.value)

    def __str__(self):
        """Trunks the value according to the set max_width,
        and returns a string repressentation"""
        v = self._trunk()
        return str(v)

    def __len__(self):
        """Returns the total width of this cell (before trunking)"""
        if type(self.value) == Table:
            return len(self.value)
        else:
            return max(len(v) for v in str(self.value).split('\n'))

    def set_max_width(self, i):
        """Sets the maximum width of this Cell"""
        if self._max_width != i:
            if i < 3:
                raise ValueError("Max_width can't be less then 3!")
            self._max_width = i

    def _trunk(self):
        """Trunks the value in the cell before printing.
        Adds newline chars where possible."""
        v = self.value
        i = self._max_width
        if type(v) == Table:
            v.set_max_width(i)
        elif type(v) == list:
            v = str(v)
        elif type(v) == float:
            if i is not None:
                r = i - len(str(round(v))) - 2
                if r > 0:
                    v = round(v, r)
                else:
                    v = int(v)
            else:
                v = str(v)
        # If! not elif, because float still needs to be trunked!
        if type(v) == int and i is not None:
            if i is not None and len(str(round(v))) > i:
                counter = 0
                while len(str(round(v))) > i - len(str(counter)) - 1:
                    v = float(v) / 10
                    counter += 1
                v = int(v)
                v = str(v) + 'e' + str(counter)
            else:
                v = str(v)
        # If! not elif,
        # Tries to devide list (containing spaces) in multiple rows
        # Also further trunks integer after 'e' if needed
        if type(v) == str:
            if i is not None and len(self) > i:
                # Try splitting in words first
                v = v.split(' ')
                if max(len(w) for w in v) > i:
                    # Didn't work for largest word
                    v = self.value[:i-2] + '..'
                else:
                    # Break into multiple lines
                    line = ''
                    words = v[:]
                    length = 0
                    for w in words:
                        length += len(w) + 1
                        if length > i:
                            line += '\n'
                            length = len(w) + 1
                        line += w + ' '
                    v = line
        return v


class Table:
    """
    Construct tables ready for printing data into nice table-like output.
    Nested tables, and cells containing multiple lines, are allowed!
    properties:
        fill    -- String of the default fill for empty cells.
        col_sep -- String of the column seperator used.
        head_sep-- String of the head/table seperator used.
    methods:
        add_head   -- Add a list of column headings to the table.
        add_row    -- Add a list of row data to the table.
        add_column -- Add a list of column data to the table.
        get        -- Returns an instance of the Table
        log        -- Same as print(Table.get(row, column))
        nr_of_rows -- Returns the numbers of rows in the Table as integer.
        nr_of_columns-- Returns the numbers of columns in the Table as integer.
        set_max_width-- Sets the max_width of the Table
    """

    def __init__(self, rows=0, columns=0, max_width=None,
                 fill='', col_sep='|', head_sep='+-'):
        """
        Keyword arguments:
            rows        -- Number of initial rows (default 0)
            columns     -- Number of initial columns (default 0)
            fill        -- Empty cell fill (default '')
            max_width   -- Max width of the Table for printing (default None)
            col_sep     -- Seperator between columns (default '|')
            head_sep    -- Seperator for heading/table.
                           First char is the char at crossing of head_sep with
                           col_sep, second char is the fillchar (default '+-')
                           When one char is given, crosschar and fillchar are
                           the same.
        """
        self._head = None
        self._data = [[_Cell(fill) for __ in range(columns)]
                      for __ in range(rows)]
        self.fill = fill
        if len(col_sep) > 1:
            raise ValueError("The column seperator can't be greater then one!")
        if len(head_sep) > 2:
            message =\
                "Max two chars are used for a row seperator"
            raise ValueError(message)
        self.col_sep = col_sep + ' '
        if len(head_sep) == 1:
            self.head_sep = head_sep * 2
        elif head_sep == '':
            self.head_sep = None
        else:
            self.head_sep = head_sep
        self._max_width = max_width
        self._column_widths = None
        if max_width is not None:
            self._column_widths = self._calc_column_widths()

    def __repr__(self):
        message =\
            "<Table object: currencly holding {} columns and {} rows>"\
            .format(self.nr_of_columns(), self.nr_of_rows())
        return message

    def __str__(self):
        string = ''
        if self._head is not None:
            while len(self._head) < self.nr_of_columns():
                self._head.append(_Cell(''))
            string += self._convert_row_to_string(self._head, self.col_sep)
            if self.head_sep is not None:
                sep_row = [_Cell(self.head_sep[1:] * j)
                           for j in self._calc_column_widths()]
                string += self._convert_row_to_string(sep_row, self.head_sep)
        for row in self._data:
            string += self._convert_row_to_string(row, self.col_sep)
        return string.strip('\n')

    def __len__(self):
        length = sum(w for w in self._calc_column_widths())\
                 + len(self.col_sep)\
                 * (self.nr_of_columns() - 1)
        return length

    def add_head(self, data=[], fill=None):
        """Add a list of column headings to the table.
        Keyword arguments:
        data    -- List containing the headings (default [])
        fill    -- Empty heading fill for excesive columns (default None)
        Note: If none given, the Table fill param is used!"""
        head = []
        for i in range(len(data)):
            head.append(_Cell(data[i]))
        while len(head) < self.nr_of_columns():
            if fill is None:
                head.append(_Cell(self.fill))
            else:
                head.append(_Cell(fill))
        self._head = head

    def add_row(self, data=[], fill=None):
        """Add a list of row data to the table.
        Keyword arguments:
        data    -- List containing cell data (default [])
        fill    -- The filling too use when creating more cells to fit
                   the Table size (default None)
        Note: If none given, the Table fill param is used!"""
        row = []
        if self.nr_of_columns() == 0:
            width = len(data)
        else:
            width = self.nr_of_columns()
        while len(data) > width:
            self.add_column()
        for i in range(width):
            if i < len(data):
                value = data[i]
            else:
                if fill is None:
                    value = self.fill
                else:
                    value = fill
            row.append(_Cell(value))
        self._data.append(row)
        self._column_widths = self._calc_column_widths()

    def add_column(self, head=None, data=[], fill=None):
        """Add a list of column data to the table.
        Keyword arguments:
        head    -- The table heading of this column (default None)
        data    -- List containing cell data (default [])
        fill    -- The filling too use when creating more cells to fit
                   the Table size (default None)
        Note: If none given, the Table fill param is used!"""
        length = self.nr_of_rows()
        while len(data) > length:
            self.add_row()
            length = self.nr_of_rows()
        for i in range(length):
            if i < len(data):
                value = data[i]
            else:
                if fill is None:
                    value = self.fill
                else:
                    value = fill
            self._data[i].append(_Cell(value))
        if self._head is None and head is not None:
            self._head = []
        if head is not None:
            while len(self._head) < self.nr_of_columns() - 1:
                self._head.append(_Cell(''))
            self._head.append(_Cell(head))
        self._column_widths = self._calc_column_widths()

    def get(self, row=None, column=None):
        """Returns an instance of the Table containing the heading and
        Cell(s) from the Table.
        Note: If both row and column are ommited, return an instance of
        the Table.
        Keyword arguments:
        row     -- Integer or range of the corresponding row (default None)
        column  -- Integer or range of the corresponding column (default None)
        Note: index start at 0"""
        if type(row) == int:
            row = [row]
        if type(column) == int:
            column = [column]
        if row is not None and max(row) >= self.nr_of_rows():
            raise IndexError("Exceeding max rows!\n" + repr(self))
        if column is not None and max(column) >= self.nr_of_columns():
            raise IndexError("Exceeding max columns!\n" + repr(self))
        T = Table(
                max_width=self._max_width,
                fill=self.fill,
                col_sep=self.col_sep[:1],
                head_sep=self.head_sep
        )
        if row is None and column is None:
            T._rows = list(self._data)
            T._column_widths = list(self._column_widths)
        elif row is None:
            for c in column:
                col = [r[c] for r in self._data]
                if self._head is not None and c < len(self._head):
                    head = self._head[c]
                T.add_column(head=head, data=col)
        elif column is None:
            for r in row:
                T.add_head(data=self._head)
                T.add_row(data=self._data[r])
        else:
            if self._head is not None and column < len(self._head):
                head = self._head[column]
            T.add_column(head=head, data=[self._data[row][column]])
        return T

    def log(self, row=None, column=None):
        """Prints the Cell, row or column.
        Same as print(Table.get(row, column))
        Keyword arguments:
        row     -- Integer or range of the corresponding row (default None)
        column  -- Integer or range of the corresponding column (default None)
        Note: index start at 0"""
        print(self.get(row=row, column=column))

    def nr_of_rows(self):
        """Returns the numbers of rows in the Table as integer."""
        return len(self._data)

    def nr_of_columns(self):
        """Returns the numbers of columns in the Table as integer."""
        if self.nr_of_rows() == 0:
            return 0
        else:
            return len(self._data[0])

    def set_max_width(self, i):
        """Sets the max_width of the Table
        Arguments:
        i       -- Integer of maxs width (in chars)"""
        if self._max_width != i:
            self._max_width = i
            self._column_widths = self._calc_column_widths()

    def _calc_column_widths(self):
        M = []
        for column in zip(*self._data):
            # One space extra...
            mx = max(len(c) + len(self.col_sep) - 1 for c in column)
            if mx < 3:
                M.append(3)
            else:
                M.append(mx)
        # The last column needs to be smaller
        if len(M) > 1 and M[len(M)-1] > 3:
            M[len(M)-1] -= 1
        if self._max_width is not None:
            # Trunk the width of each column
            # Starting with the largest column
            # Remove the seperators for the Cell's max-width
            col_max = self._max_width - len(self.col_sep) * (len(M) - 1)
            while sum(M) > col_max:
                i = M.index(max(M))
                M[i] -= 1
        return M

    def _row_height(self, row):
        return max(c._height for c in row)

    def _convert_row_to_string(self, row, sep):
        cols = []
        string = ''
        W = self._calc_column_widths()
        for i, c in enumerate(row):
            print(repr(c))
            c.set_max_width(W[i])
            cols.append(str(c).split('\n'))
        for line in zip_longest(*cols, fillvalue=self.fill):
            for ii, l in enumerate(line):
                string += l.ljust(W[ii])
                if ii < len(W) - 1:
                    string += sep
                else:
                    string += '\n'
        return string


if __name__ == '__main__':
    print("This module is supposed to be imported!")
# TODO:
# - When setting max_width Table tries too shrink largest column first,
#   This isn't always desirable, especially with nested tables of different
#   sizes.
# - Head isn't taken into account when setting/calculating column width.
#   Is this the desired behaviour?
# - Nested tables side by side won't line row by row... This leaves room for
#   discussion. At the end, it's a cell containing a table, not a splitted
#   cell...
