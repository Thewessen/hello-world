import unittest
from main import part_1, part_2


class MainTest(unittest.TestCase):
    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 2662308295)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 63441)


if __name__ == '__main__':
    unittest.main()
