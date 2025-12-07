import unittest
from main import count_splitters


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = count_splitters(data, debug=True)
        self.assertEqual(n, 21)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = count_splitters(data, debug=True)
        self.assertEqual(n, 1717)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = count_splitters(data, debug=True, part2=True)
        self.assertEqual(n, 40)

    def test_solution_2(self):
        with open('./example_input', 'r') as data:
            n = count_splitters(data, debug=True, part2=True)
        self.assertEqual(n, 231507396180012)


if __name__ == '__main__':
    unittest.main()
