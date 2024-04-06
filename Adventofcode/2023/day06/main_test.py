import unittest
from main import product_margins_of_error, single_race


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = product_margins_of_error(data)
        self.assertEqual(n, 288)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = single_race(data)
        self.assertEqual(n, 71503)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            n = product_margins_of_error(data)
        self.assertEqual(n, 1108800)

    # def test_solution_part_2(self):
    #     with open('./input', 'r') as data:
    #         n = number_of_scratchcards(data)
    #     self.assertEqual(n, 13114317)


if __name__ == '__main__':
    unittest.main()
