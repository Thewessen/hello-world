import unittest
from main import solve_puzzle, solve_part_2


class MainTest(unittest.TestCase):
    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = solve_puzzle(data)
        self.assertEqual(r, 3306701)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = solve_part_2(data)
        self.assertEqual(r, 7621)


if __name__ == '__main__':
    unittest.main()
