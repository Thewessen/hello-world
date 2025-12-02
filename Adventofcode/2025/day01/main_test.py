import unittest
from main import count_passes, count_hits


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = count_hits(data)
        self.assertEqual(n, 3)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = count_hits(data)
        self.assertEqual(n, 1074)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = count_passes(data)
        self.assertEqual(n, 6)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = count_passes(data)
        self.assertEqual(n, 6254)


if __name__ == '__main__':
    unittest.main()
