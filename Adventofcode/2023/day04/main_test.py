import unittest
from main import score_scratchcards, number_of_scratchcards


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = score_scratchcards(data)
        self.assertEqual(n, 13)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = number_of_scratchcards(data)
        self.assertEqual(n, 30)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            n = score_scratchcards(data)
        self.assertEqual(n, 24706)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            n = number_of_scratchcards(data)
        self.assertEqual(n, 13114317)


if __name__ == '__main__':
    unittest.main()
