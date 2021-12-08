import unittest
from main import count_easy_digits, solution_part_2


class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            result = count_easy_digits(data)
        self.assertEqual(result, 26)

    def test_part_2_example(self):
        with open('./test_input') as data:
            result = solution_part_2(data)
        self.assertEqual(result, 61229)



if __name__ == '__main__':
    unittest.main()
