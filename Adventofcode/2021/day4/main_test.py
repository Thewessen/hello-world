import unittest
from main import get_best_card, get_least_best_card

class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            best = get_best_card(data)
        self.assertEqual(best.score(), 4512)
                    
    def test_part_2_example(self):
        with open('./test_input') as data:
            best = get_least_best_card(data)
        self.assertEqual(best.score(), 1924)

if __name__ == '__main__':
    unittest.main()
