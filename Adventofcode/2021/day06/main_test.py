import unittest
from main import progress_days


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = progress_days(data, 80)
        self.assertEqual(result, 5934)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = progress_days(data, 80)
        self.assertEqual(result, 394994)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            result = progress_days(data, 256)
        self.assertEqual(result, 26984457539)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = progress_days(data, 256)
        self.assertEqual(result, 1765974267455)


if __name__ == '__main__':
    unittest.main()

