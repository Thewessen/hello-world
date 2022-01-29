import unittest
from main import calc_fuel, calc_exact_fuel


class MainTest(unittest.TestCase):
    def test_example1_solution_part_1(self):
        r = calc_fuel(12)
        self.assertEqual(r, 2)

    def test_example2_solution_part_1(self):
        r = calc_fuel(14)
        self.assertEqual(r, 2)

    def test_example3_solution_part_1(self):
        r = calc_fuel(1969)
        self.assertEqual(r, 654)

    def test_example4_solution_part_1(self):
        r = calc_fuel(100756)
        self.assertEqual(r, 33583)

    def test_example1_solution_part_2(self):
        r = calc_exact_fuel(14)
        self.assertEqual(r, 2)

    def test_example2_solution_part_2(self):
        r = calc_exact_fuel(1969)
        self.assertEqual(r, 966)

    def test_example3_solution_part_2(self):
        r = calc_exact_fuel(100756)
        self.assertEqual(r, 50346)



if __name__ == '__main__':
    unittest.main()
