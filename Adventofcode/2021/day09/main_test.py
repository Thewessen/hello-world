import unittest
from main import calc_total_risk, sol_2


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input') as data:
            result = calc_total_risk(data)
        self.assertEqual(result, 15)

    def test_solution_part_1(self):
        with open('./input') as data:
            result = calc_total_risk(data)
        self.assertEqual(result, 439)

    def test_example_solution_part_2(self):
        with open('./test_input') as data:
            result = sol_2(data)
        self.assertEqual(result, 1134)

    def test_solution_part_2(self):
        with open('./input') as data:
            result = sol_2(data)
        self.assertEqual(result, 900900)


if __name__ == '__main__':
    unittest.main()
