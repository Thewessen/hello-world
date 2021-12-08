import unittest
from main import get_card

class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            best = get_card(data, min)
        self.assertEqual(best.score(), 4512)
                    
    def test_part_2_example(self):
        with open('./test_input') as data:
            best = get_card(data, max)
        self.assertEqual(best.score(), 1924)

if __name__ == '__main__':
    unittest.main()
