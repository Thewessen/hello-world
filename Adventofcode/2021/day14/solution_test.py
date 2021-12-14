import unittest
from main import score_polymer


class SolutionTest(unittest.TestCase):
    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = score_polymer(data, 10)
        self.assertEqual(result, 3213)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = score_polymer(data, 40)
        self.assertEqual(result, 3711743744429)


if __name__ == '__main__':
    unittest.main()
