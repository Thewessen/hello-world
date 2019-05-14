#!/usr/bin/python3

import unittest
from tables import Table


class TestTableInit(unittest.TestCase):
    def setUp(self):
        self.not_double_iter = [
            [10, 10],
            ['hello', 10],
            10,
            [None],
            {0: [0], 1: [1]},
            {0: 0, 1: 1},
            {1: 1, 2: 2},
            {'hello': 1, 'hey': 2},
            {1: 'hello', 2: 'hey'},
            {'hello': 'hello', 'hey': 'hey'},
            range(10)
        ]
        self.not_int = [
            None,
            'hello',
            ['hello'],
            [10, 10],
            ['hello', 10],
            [None],
            {0: [0], 1: [1]},
            {0: 0, 1: 1},
            {1: 1, 2: 2},
            {'hello': 1, 'hey': 2},
            {1: 'hello', 2: 'hey'},
            {'hello': 'hello', 'hey': 'hey'},
            range(10)
        ]
        self.not_pos_int = [
            *[i for i in range(-1, -15, -3)]
        ]
        self.not_str = [
            ['hello'],
            [10, 10],
            ['hello', 10],
            [None],
            {0: [0], 1: [1]},
            {0: 0, 1: 1},
            {1: 1, 2: 2},
            {'hello': 1, 'hey': 2},
            {1: 'hello', 2: 'hey'},
            {'hello': 'hello', 'hey': 'hey'},
            range(10)
        ]
        # How to check for valid input??
        valid = [
            None,
            'hello',
            ['hello']
        ]

    def test_data(self):
        for x in self.not_double_iter:
            with self.assertRaises((TypeError, KeyError),
                                   msg='data='+str(x)):
                Table(data=x)

    def test_rows(self):
        for x in self.not_int:
            with self.assertRaises((TypeError, KeyError),
                                   msg='rows='+str(x)):
                Table(rows=x)
        for x in self.not_pos_int:
            with self.assertRaises(ValueError, msg='rows='+str(x)):
                Table(rows=x)

    def test_columns(self):
        for x in self.not_int:
            with self.assertRaises((TypeError, KeyError),
                                   msg='columns='+str(x)):
                Table(columns=x)
        for x in self.not_pos_int:
            with self.assertRaises(ValueError, msg='columns='+str(x)):
                Table(columns=x)

    def test_fill(self):

if __name__ == '__main__':
    unittest.main()
