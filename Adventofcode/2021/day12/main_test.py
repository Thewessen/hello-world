import unittest
from main import count_valid_paths

class MainTest(unittest.TestCase):
    def test_small_example_solution_part_1(self):
        with open('./small_test_input', 'r') as data:
            r = count_valid_paths(data)
        self.assertEqual(r, 10)

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_valid_paths(data)
        self.assertEqual(r, 19)

    def test_large_example_solution_part_1(self):
        with open('./large_test_input', 'r') as data:
            r = count_valid_paths(data)
        self.assertEqual(r, 226)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_valid_paths(data)
        self.assertEqual(r, 3495)

    def test_small_example_solution_part_2(self):
        with open('./small_test_input', 'r') as data:
            r = count_valid_paths(data, True)
        self.assertEqual(r, 36)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = count_valid_paths(data, True)
        self.assertEqual(r, 103)

    def test_large_example_solution_part_2(self):
        with open('./large_test_input', 'r') as data:
            r = count_valid_paths(data, True)
        self.assertEqual(r, 3509)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = count_valid_paths(data, True)
        self.assertEqual(r, 94849)


if __name__ == '__main__':
    unittest.main()
