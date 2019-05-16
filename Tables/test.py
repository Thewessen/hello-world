#!/usr/bin/python3

import unittest
from tables import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.types = {
            'positive_int': [
                                *[i for i in range(1, 10)],
                                *[i for i in range(1337, 1400, 7)],
                            ],
            'negative_int': [
                                *[i for i in range(-10, -1)],
                                *[i for i in range(-1337, -1300, 7)],
                            ],
            'positive_float': [
                                *[float(i)/7 for i in range(1, 10)],
                                *[float(i)/37 for i in range(1337, 1400, 7)],
                                1e32,
                                2e64
                              ],
            'negative_float': [
                                *[float(i)/7 for i in range(-10, -1)],
                                *[float(i)/37 for i in range(-1337, -1300, 7)],
                                -1e32,
                                -2e64
                              ],
            'dict': [
                        {0: [0], 1: [1]},
                        {0: 0, 1: 1},
                        {1: 1, 2: 2},
                        {'hello': 1, 'hey': 2},
                        {1: 'hello', 2: 'hey'},
                        {'hello': 'hello', 'hey': 'hey'}
                    ],
            'single_iter': [
                                [10, 10],
                                [0, 0],
                                ['hello', 10],
                                [None],
                                [None, None]
                            ],
            'double_iter': [
                                ['hello'],
                                [[0], [0]],
                                [[10, 10]],
                                ['hello', [10]],
                                [[None]],
                                [[None, None]],
                                [[None], [None]]
                            ],
            'str': [
                        'hello',
                        'world\n',
                        '\they',
                        '\r\"',
                        '\3',
                        '0',
                        'None',
                        '!@#$%^&*()'
                   ]
        }

    def test__init__(self):
        # data
        for k, v in self.types.items():
            if k != 'double_iter' and k != 'str':
                for x in v:
                    with self.assertRaises((TypeError, KeyError),
                                           msg='data='+str(x)):
                        Table(data=x)
        for x in self.types['double_iter'] + self.types['str']:
            self.assertIsInstance(Table(data=x), Table, msg='data='+str(x))
        # rows
        for k, v in self.types.items():
            if k != 'positive_int':
                for x in v:
                    with self.assertRaises((ValueError, TypeError, KeyError),
                                           msg='rows='+str(x)):
                        Table(rows=x)
        for x in self.types['positive_int']:
            self.assertIsInstance(Table(rows=x), Table, msg='rows='+str(x))
        # columns
        for k, v in self.types.items():
            if k != 'positive_int':
                for x in v:
                    with self.assertRaises((ValueError, TypeError, KeyError),
                                           msg='columns='+str(x)):
                        Table(rows=1, columns=x)
        for x in self.types['positive_int']:
            self.assertIsInstance(Table(columns=x), Table,
                                  msg='columns='+str(x))
        # col_sep
        for k, v in self.types.items():
            for x in v:
                if k != 'str' or (k == 'str' and len(x) > 1):
                    with self.assertRaises((ValueError, TypeError, KeyError),
                                           msg='col_sep='+str(x)):
                        Table(col_sep=x)
        for x in self.types['str']:
            if len(x) < 2:
                self.assertIsInstance(Table(col_sep=x), Table,
                                      msg='col_sep='+str(x))
        # head_sep
        for k, v in self.types.items():
            for x in v:
                if k != 'str' or (k == 'str' and len(x) > 2):
                    with self.assertRaises((ValueError, TypeError, KeyError),
                                           msg='head_sep='+str(x)):
                        Table(head_sep=x)
        for x in self.types['str']:
            if len(x) < 3:
                self.assertIsInstance(Table(head_sep=x), Table,
                                      msg='head_sep='+str(x))
        # fill
        for k, v in self.types.items():
            for x in v:
                self.assertIsInstance(Table(rows=5, columns=5, fill=x), Table,
                                      msg='fill='+str(x))

    def table_regex(self, rows, columns, head=0):
        # fill='', col_sep='|', head_sep='+-'):
        sep = '(-+\\+)*-+\n'
        row = '([^\n]*? \\| ){'+str(columns-1)+'}[^\n]*? *?\n'
        last = '([^\n]*? \\| ){'+str(columns-1)+'}[^\n]*? *?$'
        if head != 0:
            return '^' + row * head + sep + row * (rows - 1) + last
        else:
            return '^' + row * (rows - 1) + last

    def onerow_fill_test_regex(self, fullempty):
        # fullempty = (nr_of_full, nr_of_empty, nr_of_full, etc...)
        full = 'test \\| '
        empty = ' *?\\| '
        end_full = 'test *?\n'
        end_empty = ' *?\n'
        regex = '^'
        for i, fe in enumerate(fullempty[:-1]):
            if i % 2 == 0:
                regex += full * fe
                if i == len(fullempty) - 1:
                    regex += end_empty * fullempty[i+1]
            else:
                regex += empty * fe
                if i == len(fullempty) - 1:
                    regex += end_full * fullempty[i+1]
        return regex

    def test__str__(self):
        expect = [
                (' ', (3, 3)),
                ('\n', (6, 3)),
                (['\n'], (3, 3))
        ]
        for (inp, (rows, columns)) in expect:
            T = Table(rows=3, columns=3, fill=inp)
            regex = self.table_regex(rows, columns)
            self.assertRegex(str(T), regex,
                             msg='fill='+str(inp))

    def test_add_head(self):
        # Starting with three columns and three rows (no head)
        expect = [
                (None, (3, 3, 1)),
                ([], (3, 3, 1)),
                ([''], (3, 3, 1)),
                ('hey', (3, 3, 1)),
                ('', (3, 3, 1)),
                ([None], (3, 3, 1)),
                (['']*4, (3, 4, 1)),
                (['']*10, (3, 10, 1)),
                ('helloworld', (3, 10, 1)),
                (['\n'], (3, 3, 2)),
                ('\n', (3, 3, 2)),
                (['\n\n\n'], (3, 3, 4)),
                ('\n\n\n\n\n', (3, 5, 2))
        ]
        for (inp, (rows, columns, head)) in expect:
            T = Table(rows=3, columns=3)
            T.add_head(data=inp)
            regex = self.table_regex(rows, columns, head)
            self.assertRegex(str(T), regex,
                             msg='data='+str(inp))

    def test_add_row(self):
        # Starting with three rows and three columns
        expect = [
                (None, (4, 3)),
                ([], (4, 3)),
                ([''], (4, 3)),
                ('hey', (4, 3)),
                ('', (4, 3)),
                ([None], (4, 3)),
                (['']*4, (4, 4)),
                (['']*10, (4, 10)),
                ('helloworld', (4, 10)),
                (['\n'], (5, 3)),
                ('\n', (5, 3)),
                (['\n\n\n'], (7, 3)),
                ('\n\n\n\n\n', (5, 5))
        ]
        for (inp, (rows, columns)) in expect:
            T = Table(rows=3, columns=3)
            T.add_row(data=inp)
            regex = self.table_regex(rows, columns)
            self.assertRegex(str(T), regex,
                             msg='data='+str(inp))

    def test_add_column(self):
        # Starting with three rows and three columns
        expect = [
                (None, (3, 4)),
                ([], (3, 4)),
                ([''], (3, 4)),
                ('hey', (3, 4)),
                ('', (3, 4)),
                ([None], (3, 4)),
                (['']*4, (4, 4)),
                (['']*10, (10, 4)),
                ('helloworld', (10, 4)),
                (['\n'], (4, 4)),
                ('\n', (4, 4)),
                (['\n\n\n'], (6, 4)),
                ('\n\n\n\n\n', (10, 4))
        ]
        for (inp, (rows, columns)) in expect:
            T = Table(rows=3, columns=3)
            T.add_column(data=inp)
            regex = self.table_regex(rows, columns)
            self.assertRegex(str(T), regex,
                             msg='data='+str(inp))
        expect_width_head = [
                (None, None, (3, 4, 0)),
                ([], [], (3, 4, 1)),
                ([''], [''], (3, 4, 1)),
                ('hey', 'hey', (3, 4, 1)),
                ('', '', (3, 4, 1)),
                ([None], [None], (3, 4, 1)),
                (['']*4, ['']*4, (4, 4, 1)),
                (['']*10, ['']*10, (10, 4, 1)),
                ('helloworld', 'helloworld', (10, 4, 1)),
                (['\n'], ['\n'], (4, 4, 1)),
                ('\n', '\n', (4, 4, 2)),
                (['\n\n\n'], ['\n\n\n'], (6, 4, 1)),
                ('\n\n\n\n\n', '\n\n\n\n\n', (10, 4, 6))
        ]
        for (data, head, (rows, columns, heads)) in expect_width_head:
            T = Table(rows=3, columns=3)
            T.add_column(data=data, head=head)
            regex = self.table_regex(rows, columns, heads)
            self.assertRegex(str(T), regex,
                             msg='data={}, head={}'
                             .format(str(data), str(head)))

    def test_remove_head(self):
        autoremove_expect = [
                (None, (0, 5)),
                (0, (4, 1)),
                (1, (4, 1)),
                (range(2), (3, 2)),
                ([1, 3], (3, 2))
        ]
        for (inp, fullempty) in autoremove_expect:
            T = Table(rows=1, columns=5)
            T.add_head(fill='test')
            T.remove_head(column=inp, autoremove=True)
            regex = self.onerow_fill_test_regex(fullempty)
            self.assertRegex(str(T), regex,
                             msg='column='+str(inp))
        expect = [
                (None, (0, 5)),
                (0, (0, 1, 4)),
                (1, (1, 1, 3)),
                (range(2), (0, 2, 3)),
                ([1, 3], (1, 1, 1, 1, 1)),
                ([0, 0], (0, 1, 4)),
                ([0, 0, 1, 1], (0, 2, 3))
        ]
        for (inp, fullempty) in expect:
            T = Table(rows=1, columns=5)
            T.add_head(fill='test')
            T.remove_head(column=inp, autoremove=False)
            regex = self.onerow_fill_test_regex(fullempty)
            self.assertRegex(str(T), regex,
                             msg='column={},autoremove=False'
                                 .format(str(inp)))
        for k, v in self.types.items():
            for x in v:
                if k != 'positive_int' and k != 'single_iter'\
                        or (k == 'positive_int' and x > 5):
                    T = Table(rows=1, columns=5)
                    T.add_head(fill='test')
                    with self.assertRaises((ValueError, TypeError),
                                           msg='column='+str(x)):
                        T.remove_head(column=x)

    def test_remove_row(self):
        # TODO: Make sure the proper row is removed!
        # Starting with three rows and three columns
        autoremove_expect = [
                (None, (2, 3)),
                (0, (2, 3)),
                (1, (2, 3)),
                (range(2), (1, 3)),
                ([0, 2], (1, 3)),
                ([0, 0], (2, 3)),
                ([0, 0, 1, 1], (1, 2))
        ]
        for (inp, (rows, columns)) in autoremove_expect:
            T = Table(rows=3, columns=3)
            T.remove_row(row=inp, autoremove=True)
            regex = self.table_regex(rows, columns)
            self.assertRegex(str(T), regex,
                             msg='row={},autoremove=True'
                                 .format(str(inp)))
        # TODO: Same as autoremove=True??
        expect = [
                (None, (2, 3)),
                (0, (2, 3)),
                (1, (2, 3)),
                (range(2), (1, 3)),
                ([0, 2], (1, 3)),
                ([0, 0], (2, 3)),
                ([0, 0, 1, 1], (1, 2))
        ]
        for (inp, (rows, columns)) in expect:
            T = Table(rows=3, columns=3)
            T.remove_row(row=inp, autoremove=False)
            regex = self.table_regex(rows, columns)
            self.assertRegex(str(T), regex,
                             msg='row={},autoremove=False'
                                 .format(str(inp)))
        for k, v in self.types.items():
            for x in v:
                if k != 'positive_int' and k != 'single_iter'\
                        or (k == 'positive_int' and x > 2):
                    T = Table(rows=3, columns=3)
                    with self.assertRaises((ValueError, TypeError),
                                           msg='row='+str(x)):
                        T.remove_row(row=x)

    def test_remove_column(self):
        # TODO: Make sure the proper column is removed!
        # Starting with three columns and three columns
        autoremove_expect = [
                (None, (3, 2)),
                (0, (3, 2)),
                (1, (3, 2)),
                (range(2), (3, 1)),
                ([0, 2], (3, 1)),
                ([0, 0], (3, 2)),
                ([0, 0, 1, 1], (2, 1))
        ]
        for (inp, (columns, columns)) in autoremove_expect:
            T = Table(rows=3, columns=3)
            T.remove_column(column=inp, autoremove=True)
            regex = self.table_regex(columns, columns)
            self.assertRegex(str(T), regex,
                             msg='column={},autoremove=True'
                                 .format(str(inp)))
        # TODO: Same as autoremove=True??
        expect = [
                (None, (3, 2)),
                (0, (3, 2)),
                (1, (3, 2)),
                (range(2), (3, 1)),
                ([0, 2], (3, 1)),
                ([0, 0], (3, 2)),
                ([0, 0, 1, 1], (2, 1))
        ]
        for (inp, (columns, columns)) in expect:
            T = Table(rows=3, columns=3)
            T.remove_column(column=inp, autoremove=False)
            regex = self.table_regex(columns, columns)
            self.assertRegex(str(T), regex,
                             msg='column={},autoremove=False'
                                 .format(str(inp)))
        for k, v in self.types.items():
            for x in v:
                if k != 'positive_int' and k != 'single_iter'\
                        or (k == 'positive_int' and x > 2):
                    T = Table(rows=3, columns=3)
                    with self.assertRaises((ValueError, TypeError),
                                           msg='column='+str(x)):
                        T.remove_column(column=x)


if __name__ == '__main__':
    unittest.main()
