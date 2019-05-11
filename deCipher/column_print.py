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


class ColumnPrint:
    def __init__(self):
        self._rows = []

    def __str__(self):
        return "This is a test"

    def __repr__(self):
        message = "<ColumnPrint object:\
                    currencly holding {} columns and {} rows>"\
                    .format(len(self._cols), len(self._rows))
        return re.sub(' +', ' ', message)


# def calc_max_width(iteratable):
if __name__ == '__main__':
    C = ColumnPrint()
    print(C)
    print(str(C))
