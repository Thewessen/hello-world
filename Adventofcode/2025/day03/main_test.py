import unittest
from main import max_joltage


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = max_joltage(data, debug=True)
        self.assertEqual(n, 357)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = max_joltage(data, debug=True)
        self.assertEqual(n, 17207)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = max_joltage(data, batteries=12, debug=True)
        self.assertEqual(n, 3121910778619)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = max_joltage(data, batteries=12, debug=True)
        self.assertEqual(n, 170997883706617)


if __name__ == '__main__':
    unittest.main()
