import unittest
from main import count_easy_digits, solution_part_2


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = count_easy_digits(data)
        self.assertEqual(result, 26)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = count_easy_digits(data)
        self.assertEqual(result, 362)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            result = solution_part_2(data)
        self.assertEqual(result, 61229)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = solution_part_2(data)
        self.assertEqual(result, 1020159)



if __name__ == '__main__':
    unittest.main()
