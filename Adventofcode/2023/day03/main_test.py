import unittest
from main import part_numbers, gear_parts


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = part_numbers(data)
        self.assertEqual(n, 4361)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = gear_parts(data)
        self.assertEqual(n, 467835)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            n = part_numbers(data)
        self.assertEqual(n, 546312)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            n = gear_parts(data)
        self.assertEqual(n, 87449461)


if __name__ == '__main__':
    unittest.main()
