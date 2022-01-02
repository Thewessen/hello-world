import unittest
from main import SeaCucumbers
from more_itertools import consume


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = SeaCucumbers.from_iter(data)
        consume(r)
        self.assertEqual(r.moves, 58)


if __name__ == '__main__':
    unittest.main()
