import unittest
from main import get_card

class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            best = get_card(data, min)
        self.assertEqual(best.score(), 4512)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            best = get_card(data, min)
        self.assertEqual(best.score(), 51034)
                    
    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            best = get_card(data, max)
        self.assertEqual(best.score(), 1924)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            best = get_card(data, max)
        self.assertEqual(best.score(), 5434)


if __name__ == '__main__':
    unittest.main()
