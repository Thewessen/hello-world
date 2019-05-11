#!/usr/bin/python3


# Maybe a pointer is necessary?
class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<Cell object: value='{}'>"\
                .format(self.value)

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(str(self.value))


class Table:
    def __init__(self, rows=0, columns=0, max_width=None,
                 title='', head=None, fill='',
                 col_sep='|', row_sep='+-'):
        self._head = head
        self._rows = [[Cell(fill) for __ in range(columns)]
                      for __ in range(rows)]
        if len(col_sep) > 1:
            raise ValueError("The column seperator can't be greater then one!")
        if len(row_sep) > 2:
            message =\
                "Max two chars are used for a row seperator"
            raise ValueError(message)
        self._col_sep = col_sep + ' '
        if len(row_sep) == 1:
            self._row_sep = row_sep * 2
        elif row_sep == '':
            self._row_sep = None
        else:
            self._row_sep = row_sep
        self.max_width = max_width

    def __str__(self):
        M = []
        for column in zip(*self._rows):
            M.append(max(len(str(c)) + len(self._col_sep) - 1
                     for c in column))
        # Trunk the width of each column
        # Starting with the largest column
        if self.max_width is not None:
            col_max = self.max_width - len(self._col_sep) * (len(M) - 1)
            while sum(M) > col_max:
                i = M.index(max(M))
                M[i] -= 1
        string = ''
        if self._head is not None:
            string += self._col_sep.join(
                            [self._adjust(str(h), M[i])
                             for i, h in enumerate(self._head)])
            string += '\n'
            # Fill with row seperator
            if self._row_sep is not None:
                for i, j in enumerate(M):
                    string += self._row_sep[1:] * j
                    if i < len(M) - 1:
                        string += self._row_sep
                string += '\n'
        for j, row in enumerate(self._rows):
            string += self._col_sep.join(
                            [self._adjust(str(c), M[i])
                             for i, c in enumerate(row)])
            if j < len(self._rows) - 1:
                string += '\n'
        return string

    def __repr__(self):
        # message =\
        #     "<ColumnPrint object: currencly holding {} columns and {} rows>"\
        #     .format(len(self._rows[0]), len(self._rows))
        return "<Table>"

    def __len__(self):
        M = []
        for column in zip(*self._rows):
            M.append(max(len(str(c)) + len(self._col_sep) + 1
                     for c in column))
        # Returns the total length of the table
        return sum(M) - len(self._col_sep)

    def log(self, row=None, column=None):
        if row is None and column is None:
            print(self._rows)
        elif row is None:
            for row in self._rows:
                print(row[column])
        elif column is None:
            print(' '.join(str(cell) for cell in self._rows[row]))
        else:
            print(self._rows[row][column])

    def get(self, row=None, column=None):
        if row is None and column is None:
            return self
        elif row is None:
            return [c[column] for c in zip(*self._rows)]
        elif column is None:
            return self._rows[row]
        else:
            return self._rows[row][column]

    def add_row(self, data=[], fill=''):
        row = []
        if len(self._rows) == 0:
            width = len(data)
        else:
            width = len(self._rows[0])
        while len(data) > width:
            self.add_column()
        for i in range(width):
            if i < len(data):
                value = data[i]
            else:
                value = fill
            row.append(Cell(value))
        self._rows.append(row)

    def add_head(self, data=[], fill=''):
        head = []
        for i in range(len(data)):
            head.append(Cell(data[i]))
        self._head = head

    def add_column(self, head=None, data=[], fill=''):
        length = len(self._rows)
        while len(data) > length:
            self.add_row()
            length = len(self._rows)
        print(length)
        for i in range(length):
            if i < len(data):
                value = data[i]
            else:
                value = fill
            self._rows[i].append(value)
        if self._head is None and head is not None:
            raise Exception("Head is not yet set!")
        if head is not None:
            while len(self._head) < len(self._rows[0]) - 1:
                self._head.append('')
            self._head.append(head)

    def _adjust(self, string, length):
        if repr(string) == '<Table>':
            string.max_width = length + len(self._col_sep)
        elif len(str(string)) > length:
            # Padding is reduced too 1!
            return str(string)[:length-2] + '..'
        else:
            return str(string).ljust(length)


# def calcmax_width(iteratable):
if __name__ == '__main__':
    T = Table()
    T.add_head(data=['found1', 'found2', 'found3'])
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    F1 = Table()
    F1.add_column(head='blk',
                  data=[alph[i:i+2] for i in range(0, len(alph), 2)])
    F1.add_column(head='freq', data=[i for i in range(13)])
    F1.add_column(head='mean', data=[float(i) for i in range(15, 80, 5)])
    print(F1)
