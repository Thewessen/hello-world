#!/usr/bin/python3

# Example...

# monogram:      found1:              found2:              found3:
# blk  relative  blk  freq  relative  blk  freq  relative  blk  freq  relative
# THE  0.01814   JDS  19    0.044     JDS  33    0.056     JDS  9     0.058
# AND  0.007252  DSN  11    0.026     SQN  16    0.027     QGW  7     0.045
# ING  0.007178  QGW  11    0.026     UDQ  12    0.02      SNS  4     0.026
# ENT  0.004188  SUQ  10    0.023     JSN  12    0.02      CGE  4     0.026
# ION  0.004157  JCB  10    0.023     SNS  11    0.019     DSN  3     0.019
# HER  0.003574  CBG  10    0.023     QNS  11    0.019     NQG  3     0.019
# FOR  0.003436  DCU  10    0.023     DQF  10    0.017     GWQ  3     0.019
# THA  0.003327  ZCY  8     0.019     QFS  10    0.017     JDQ  3     0.019
# NTH  0.003303  CYD  8     0.019     FSU  10    0.017     UZQ  3     0.019

# Data:
# head = ['monogram:', 'found1:', 'found2:', 'found3:']
# data =
# import string as st
import re
# from itertools import zip_longest


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
    def __init__(self, rows=0, columns=0, title='', fill=''):
        self._rows = [[Cell(fill) for j in range(columns)]
                      for i in range(rows)]

    def __str__(self):
        return "This is a test"

    def __repr__(self):
        message = "<ColumnPrint object:\
                    currencly holding {} columns and {} rows>"\
                    .format(len(self._rows[0]), len(self._rows))
        return re.sub(' +', ' ', message)

    def __len__(self):
        return 5

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

    def add_row(self, head='', data=[], fill=''):
        row = []
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

    def add_column(self, head='', data=[], fill=''):
        col = []
        length = len(self._rows)
        while len(data) > length:
            self.add_row()
        for i in range(length):
            if i < len(data):
                value = data[i]
            else:
                value = fill
            self._rows[i].append(value)


# def calc_max_width(iteratable):
if __name__ == '__main__':
    C = Table(5, 5, fill='hello')
    C.add_row(data=[1, 2, 3], fill='hey')
    C.add_row(data=[1, 2, 3], fill='hey')
    C.log(row=5)
