"""Construct tables ready for printing data into nice table-like output.
Nested tables, and cells containing multiple lines, are allowed!
Exports class Table()"""

import copy
from itertools import zip_longest

__all__ = ["Table"]


class _Cell:
    """Generates objects for the Table class. Each Table is a
    two-dimensional row containing Cell-objects"""

    def __init__(self, value, max_width=None):
        """Set value and calculates the max_width and height"""
        self.value = value
        self.max_width = max_width

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
        if isinstance(self.value, Table):
            return len(self.value)
        else:
            return max(len(v) for v in str(self.value).split('\n'))

    def __iter__(self):
        """Iterate over each trunked row of cells value"""
        v = self._trunk()
        for line in str(v).split('\n'):
            yield line

    @property
    def max_width(self):
        return self._max_width

    @max_width.setter
    def max_width(self, value):
        """Sets the maximum width of this Cell"""
        if value is None:
            return

        try:
            if value > 3:
                self._max_width = value
            else:
                raise ValueError("`max_width` cannot be less then 3")
        except TypeError:
            raise TypeError("`max_width` should be an integer or `None`")

    def copy(self):
        if isinstance(self.value, (int, float, str)):
            return _Cell(value=self.value, max_width=self.max_width)
        elif isinstance(self.value, (list, dict, tuple, object)):
            return _Cell(value=copy.deepcopy(self.value),
                         max_width=self.max_width)

    def get_value(self):
        if isinstance(self.value, (int, float, str)):
            return self.value
        elif isinstance(self.value, (list, dict, tuple, object)):
            return copy.deepcopy(self.value)

    def _trunk(self):
        """Trunks the value in the cell before printing.
        Adds newline chars where possible."""
        v = self.value
        i = self.max_width
        if v is None:
            v = ''
        elif isinstance(v, Table):
            v.max_width = i
        elif isinstance(v, list):
            v = str(v)
        elif isinstance(v, float):
            if i is not None:
                r = i - len(str(round(v))) - 2
                if r > 0:
                    v = round(v, r)
                else:
                    v = int(v)
            else:
                v = str(v)
        # If, not elif, because float still needs to be trunked!
        if isinstance(v, int) and i is not None:
            if i is not None and len(str(round(v))) > i:
                counter = 0
                while len(str(round(v))) > i - len(str(counter)) - 1:
                    v = float(v) / 10
                    counter += 1
                v = int(v)
                v = str(v) + 'e' + str(counter)
            else:
                v = str(v)
        # If, not elif,
        # Tries to devide list (containing spaces) in multiple rows
        # Also further trunks integer after 'e' if needed
        if isinstance(v, str):
            if i is not None and len(self) > i:
                # Try splitting in words first
                words = v.split(' ')
                if max(len(w) for w in words) > i:
                    # Didn't work for largest word
                    v = v[:i-2] + '..'
                else:
                    # Break into multiple lines
                    line = ''
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
        fill      -- String of the default fill for empty cells.
        col_sep   -- String of the column seperator used.
        head_sep  -- String of the head/table seperator used.
        max_width -- Maxmum width of the Table
    methods:
        add_head        -- Add a list of column headings to the table.
        add_row         -- Add a list of row data to the table.
        add_column      -- Add a list of column data to the table.
        remove_head     -- Add a list of column headings to the table.
        remove_row      -- Add a list of row data to the table.
        remove_column   -- Add a list of column data to the table.
        copy            -- Returns an instance Table containing specified
                           row(s) and/or column(s)
        log             -- Same as print(Table.copy(row, column))
        get             -- Returns a copy of the value(s) from the Table
        nr_of_rows      -- Returns the numbers of rows in the Table as integer.
        column_count    -- Returns the numbers of columns in the Table as
                           an integer.
    """

    def __init__(self, data=None, rows=0, columns=0, max_width=None,
                 fill='', col_sep='|', head_sep='+-'):
        """
        Keyword arguments:
            data        -- Initial data. Needs to be an iterable object of
                           iterable objects (default None)
            rows        -- Number of initial rows (default 0)
            columns     -- Number of initial columns (default 0)
            max_width   -- Max width of the Table for printing (default None)
            fill        -- Empty cell fill (default '')
            col_sep     -- Seperator between columns (default '|')
            head_sep    -- Seperator for heading/table.
                           First char is the char at crossing of head_sep with
                           col_sep, second char is the fillchar (default '+-')
                           When one char is given, crosschar and fillchar are
                           the same.
        """
        self._head = None
        self.fill = fill
        # TODO More chars for seperators?
        # TODO Row seperator?
        if len(col_sep) > 1:
            raise ValueError("The column seperator can't be greater then one.")
        if len(head_sep) > 2:
            raise ValueError("Max two chars are used for a row seperator.")
        if rows < 0:
            raise ValueError("Number of rows can't be less then zero.")
        if columns < 0:
            raise ValueError("Number of columns can't be less then zero.")
        self.col_sep = col_sep + ' '
        if len(head_sep) == 1:
            self.head_sep = head_sep * 2
        elif head_sep == '':
            self.head_sep = None
        else:
            self.head_sep = head_sep
        self.max_width = max_width
        if data is None:
            self._data = [[_Cell(fill) for __ in range(columns)]
                          for __ in range(rows)]
        else:
            self._data = []
            for i, row in enumerate(data):
                if i >= rows and rows != 0:
                    break
                self._data.append([])
                for j, c in enumerate(row):
                    if j >= columns and columns != 0:
                        break
                    self._data[i].append(_Cell(data[i][j]))
                while len(self._data[i]) < columns:
                    self._data[i].append(_Cell(fill))
            while len(self._data) < rows:
                self.add_row(fill=fill)

    @property
    def max_width(self):
        return self._max_width

    @max_width.setter
    def max_width(self, value):
        """Sets the max_width of the Table
        Arguments:
        i       -- Integer of maxs width (in chars)"""
        if value is None:
            return

        self._max_width = value

    def __repr__(self):
        """Representation of this object. Nr of columns and rows are added."""
        message = "<Table object: {} rows and {} columns>"\
                  .format(self.row_count, self.column_count)
        return message

    def __str__(self):
        """A performance heavy operation. Returns a string representation,
        of the current table. Trunks values as needed (set by max_width).
        Also adds seperators specified by head_sep and col_sep."""
        string = ''
        if self._head is not None:
            while len(self._head) < self.column_count:
                self._head.append(_Cell(''))
            string += self._convert_row_to_string(self._head, self.col_sep)
            if self.head_sep is not None and self.head_sep != '':
                if len(self.head_sep) == 1:
                    self.head_sep = head_sep * 2
                sep_row = [_Cell(self.head_sep[1:] * j)
                           for j in self.column_widths]
                string += self._convert_row_to_string(sep_row, self.head_sep)
        for row in self._data:
            string += self._convert_row_to_string(row, self.col_sep)
        return string.strip('\n')

    def __len__(self):
        """Returns the total width of the table when printed"""
        if self.column_count == 0:
            return 0
        else:
            length = sum(w for w in self.column_widths)\
                     + len(self.col_sep)\
                     * (self.column_count - 1)
        return length

    def add_head(self, data=None, fill=None):
        """Add a list of column headings to the table.
        Keyword arguments:
        data    -- List containing the headings (default None)
        fill    -- Empty heading fill for excesive columns (default None)
        Note: If none given, the Table fill param is used!"""
        head = []
        if data is None:
            data = ''
        for i in range(len(data)):
            if data[i] is None:
                value = ''
            else:
                value = data[i]
            head.append(_Cell(value))
        while len(head) < self.column_count:
            if fill is None:
                head.append(_Cell(self.fill))
            else:
                head.append(_Cell(fill))
        while self.column_count < len(head):
            self.add_column(self.fill)
        self._head = head

    def add_row(self, data=None, fill=None):
        """Add a list of row data to the table.
        Keyword arguments:
        data    -- List containing cell data (default [])
        fill    -- The filling too use when creating more cells to fit
                   the Table size (default None)
        Note: If none given, the Table fill param is used!"""
        row = []
        if data is None:
            data = ''
        if self.column_count == 0:
            width = len(data)
        else:
            width = self.column_count
        while len(data) > width:
            self.add_column()
            width = self.column_count
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

    def add_column(self, head=None, data=None, fill=None):
        """Add a list of column data to the table.
        Keyword arguments:
        head    -- The table heading of this column (default None)
        data    -- List containing cell data (default [])
        fill    -- The filling too use when creating more cells to fit
                   the Table size (default None)
        Note: If none given, the Table fill param is used!"""
        length = self.row_count
        if data is None:
            data = ''
        while len(data) > length:
            self.add_row()
            length = self.row_count
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
            while len(self._head) < self.column_count - 1:
                self._head.append(_Cell(''))
            self._head.append(_Cell(head))

    def remove_head(self, index=None, autoremove=False):
        """Removes range of head(s) of the table. Data is lost!
        Keywordarguments:
        index -- Integer or range of the columnhead(s) to be removed.
                 (default total heading removed)
        autoremove -- Boolean: if false, only the value of the head is removed,
                      leaving an empty cell. If true, complete cell is removed,
                      shifting remaining cells to the left (default false)
        Note: index start at 0"""
        if self._head is not None:
            if type(index) == int:
                index = [index]
            if index is not None and max(index) >= len(self._head):
                raise ValueError("Head index out of range")
            if autoremove and index is None:
                self._head = None
            elif autoremove:
                for r, i in enumerate(index):
                    self._head = self._head[:i-r] + self._head[i-r+1:]
                    self._head.append(_Cell(self.fill))
            elif index is None:
                for h in self._head:
                    h.value = self.fill
            else:
                for i in index:
                    self._head[i] = _Cell(self.fill)

    def remove_row(self, row=None, autoremove=True):
        """Removes the row(s) of the table.
        Keyarguments:
        row -- Integer or range of row(s) to be removed.
               (default last row)
        autoremove -- Boolean: remove head when there are no rows left,
                      leaving an empty table (default True)
        Note: index start at 0"""
        if row is None:
            row = self.row_count - 1
        if type(row) == int:
            row = [row]
        if max(row) >= self.row_count:
            raise ValueError("Row index out of range")
        for r, i in enumerate(row):
            self._data = self._data[:i-r] + self._data[i-r+1:]
        if autoremove and self.row_count == 0:
            self.remove_head(autoremove=True)

    def remove_column(self, column=None, autoremove=True):
        """Removes the column(s) of the table.
        Keyarguments:
        column -- Integer or range of column(s) to be removed.
                  (default last column)
        autoremove -- Boolean: if true, entire column is removed.
                      If false, column still excists, but is filled
                      with the default fill value.
                      (default True)
        Note: index start at 0"""
        if column is None:
            column = self.column_count - 1
        if type(column) == int:
            column = [column]
        if max(column) >= self.column_count:
            raise ValueError("Column index out of range")
        if autoremove:
            for r, i in enumerate(column):
                self._data = [row[:i-r] + row[i-r+1:] for row in self._data]
            self.remove_head(index=column, autoremove=True)
        else:
            for i in column:
                for row in self_data:
                    row[i] = _Cell(self.fill)

    def copy(self, row=None, column=None):
        """Returns an instance of the Table containing the heading and
        Cell(s) from the current Table.
        Note: If both row and column are ommited, return an instance of
        the whole Table.
        Keyword arguments:
        row     -- Integer, range or list of the corresponding row(s)
                   (default None)
        column  -- Integer, range or list of the corresponding column(s)
                   (default None)
        Note: index start at 0"""
        if type(row) == int:
            row = [row]
        if type(column) == int:
            column = [column]
        if row is not None and max(row) >= self.row_count:
            raise IndexError("Exceeding max rows!\n" + repr(self))
        if column is not None and max(column) >= self.column_count:
            raise IndexError("Exceeding max columns!\n" + repr(self))
        T = Table(
                max_width=self._max_width,
                fill=self.fill,
                col_sep=self.col_sep[:1],
                head_sep=self.head_sep
        )
        if row is None and column is None:
            T._data = [[c.copy() for c in row] for row in self._data]
            T._head = [h.copy() for h in self._head]
            if self._column_widths is not None:
                T._column_widths = self._column_widths.copy()
        elif row is None:
            for c in column:
                col = [r[c].copy() for r in self._data]
                head = None
                if self._head is not None:
                    head = self._head[c].copy()
                T.add_column(head=head, data=col)
                if self._column_widths is not None:
                    T._column_widths.append(self._column_widths[c])
        elif column is None:
            for r in row:
                T.add_row(data=[c.copy() for c in self._data[r]])
            if self._column_widths is not None:
                T._column_widths = self._column_widths.copy()
            if self._head is not None:
                T.add_head(data=[c.copy() for c in self._head])
        else:
            T._data = []
            for r in row:
                T._data.append([self._data[r][c].copy() for c in column])
            if self._column_widths is not None:
                T._column_widths = self._column_widths.copy()
            if self._head is not None:
                T.add_head(data=[self._head[c].copy() for c in column])
        return T

    def log(self, row=None, column=None):
        """Prints the Cell, row or column.
        Same as print(Table.copy(row, column))
        Keyword arguments:
        row     -- Integer or range of the corresponding row(s)
                   (default None)
        column  -- Integer or range of the corresponding column(s)
                   (default None)
        Note: index start at 0"""
        # TODO Make logging more efficient...
        print(self.copy(row=row, column=column))

    def get(self, row=None, column=None):
        """Returns the data contained in the range of row and column.
        Returns as single value or (multi-dimensional) list of values,
        depending on the keyargument values of row and column. Values
        (like lists, or tupples) are always copied.
        Note: if both row and column are ommited, return an multidimensional
        of list the whole Table.
        Note: doesn't return the head of the table.
        Keyword arguments:
        row     -- Integer, range or list of the corresponding row(s)
                   (default None)
        column  -- Integer, range or list of the corresponding column(s)
                   (default None)
        Note: index start at 0"""
        if type(row) == int:
            row = [row]
        if type(column) == int:
            column = [column]
        if row is not None and max(row) >= self.row_count:
            raise IndexError("Exceeding max rows!\n" + repr(self))
        if column is not None and max(column) >= self.column_count:
            raise IndexError("Exceeding max columns!\n" + repr(self))
        if row is None and column is None:
            return [[c.get_value() for c in r] for r in self._data]
        elif row is None:
            # Should return a list (or multi) of column values.
            # Inverse of the _data list, which is made of list(s) of rows.
            if len(column) == 1:
                return [r[column[0]].get_value() for r in self._data]
            else:
                return [[r[c].get_value() for r in self._data] for c in column]
        elif column is None:
            if len(row) == 1:
                return [c.get_value() for c in self._data[row[0]]]
            else:
                return [[c.get_value() for c in self._data[r]] for r in row]
        else:
            if len(row) == 1 and len(column) == 1:
                return self._data[row[0]][column[0]].get_value()
            elif len(column) == 1:
                return [self._data[r][column[0]].get_value() for r in row]
            elif len(row) == 1:
                return [self._data[row[0]][c].get_value() for c in column]
            else:
                return [[self._data[r][c].get_value() for c in column]
                        for r in row]

    @property
    def row_count(self):
        """Returns the numbers of rows in the Table as integer."""
        return len(self._data)

    @property
    def column_count(self):
        """Returns the numbers of columns in the Table as integer."""
        if self.row_count == 0:
            return 0
        else:
            return len(self._data[0])

    @property
    def column_widths(self):
        M = []
        # Add head when calculating max-widths?
        if self._head is not None:
            z = zip(self._head, *self._data)
        else:
            z = zip(*self._data)
        for column in z:
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

    def _convert_row_to_string(self, row, sep):
        string = ''
        for i, c in enumerate(row):
            c.max_width = self.column_widths[i]
        for line in zip_longest(*row, fillvalue=''):
            for ii, l in enumerate(line):
                string += l.ljust(self.column_widths[ii])
                if ii < len(self.column_widths) - 1:
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
# - Make logging more efficient...
# - More chars for seperators?
# - Add row seperator?
# - Add max height?
