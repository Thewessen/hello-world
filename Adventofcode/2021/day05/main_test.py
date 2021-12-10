import unittest
from main import count_overlapping_coords


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = count_overlapping_coords(data)
        self.assertEqual(result, 5)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = count_overlapping_coords(data)
        self.assertEqual(result, 7473)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            result = count_overlapping_coords(data, True)
        self.assertEqual(result, 12)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = count_overlapping_coords(data, True)
        self.assertEqual(result, 24164)


if __name__ == '__main__':
    unittest.main()
