import unittest
from main import calc_cheapest_horz_position, calc_cheapest_horz_position_crab_engineering


class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            result = calc_cheapest_horz_position(data)
        self.assertEqual(result, 37)

    def test_part_2_example(self):
        with open('./test_input') as data:
            result = calc_cheapest_horz_position_crab_engineering(data)
        self.assertEqual(result, 168)


if __name__ == '__main__':
    unittest.main()
