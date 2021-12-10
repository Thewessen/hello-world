import unittest
from main2 import get_card_score

class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            best = get_card_score(data, min)
        self.assertEqual(best, 4512)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            best = get_card_score(data, min)
        self.assertEqual(best, 51034)
                    
    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            best = get_card_score(data, max)
        self.assertEqual(best, 1924)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            best = get_card_score(data, max)
        self.assertEqual(best, 5434)


if __name__ == '__main__':
    unittest.main()
