import unittest
from main import syntax_error_score, autocomplete_score


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = syntax_error_score(data)
        self.assertEqual(result, 26397)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            result = syntax_error_score(data)
        self.assertEqual(result, 392367)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            result = autocomplete_score(data)
        self.assertEqual(result, 288957)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            result = autocomplete_score(data)
        self.assertEqual(result, 2192104158)


if __name__ == '__main__':
    unittest.main()
