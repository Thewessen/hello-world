import unittest
from main import calc_cheapest_horz_position, calc_cheapest_horz_position_crab_engineering


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = calc_cheapest_horz_position(data)
        self.assertEqual(result, 37)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = calc_cheapest_horz_position(data)
        self.assertEqual(result, 359648)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            result = calc_cheapest_horz_position_crab_engineering(data)
        self.assertEqual(result, 168)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = calc_cheapest_horz_position_crab_engineering(data)
        self.assertEqual(result, 100727924)


if __name__ == '__main__':
    unittest.main()
