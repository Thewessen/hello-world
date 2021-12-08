import unittest
from main2 import get_card_score

class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            r = get_card_score(data, min)
        self.assertEqual(r, 4512)
                    
    def test_part_2_example(self):
        with open('./test_input') as data:
            r = get_card_score(data, max)
        self.assertEqual(r, 1924)

if __name__ == '__main__':
    unittest.main()
