import unittest
from main import Validator, count_valid_numbers, count_valid_numbers_part2


class MainTest(unittest.TestCase):
    def test_111111_valid_part1(self):
        n = 111111
        validator = Validator.part1()
        self.assertTrue(validator.validate(n))

    def test_223450_invalid_part1(self):
        n = 223450
        validator = Validator.part1()
        self.assertFalse(validator.validate(n))

    def test_123789_invalid_part1(self):
        n = 123789
        validator = Validator.part1()
        self.assertFalse(validator.validate(n))

    def test_solution_part1(self):
        with open('./input', 'r') as data:
            r = count_valid_numbers(data)
        self.assertEqual(r, 925)

    def test_112233_valid_part2(self):
        n = 112233
        validator = Validator.part2()
        self.assertTrue(validator.validate(n))

    def test_123444_invalid_part2(self):
        n = 123444
        validator = Validator.part2()
        self.assertFalse(validator.validate(n))

    def test_111122_valid_part2(self):
        n = 111122
        validator = Validator.part1()
        self.assertTrue(validator.validate(n))

    def test_solution_part2(self):
        with open('./input', 'r') as data:
            r = count_valid_numbers_part2(data)
        self.assertEqual(r, 607)


if __name__ == '__main__':
    unittest.main()
