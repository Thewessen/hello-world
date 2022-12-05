import unittest
from main import duplicate_item, item_priority, total_score_errors, total_score_badges


class MainTest(unittest.TestCase):
    def test_duplicate_item1(self):
        item = duplicate_item('vJrwpWtwJgWrhcsFMMfFFhFp')
        self.assertEqual(item, 'p')

    def test_duplicate_item2(self):
        item = duplicate_item('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')
        self.assertEqual(item, 'L')

    def test_duplicate_item3(self):
        item = duplicate_item('PmmdzqPrVvPwwTWBwg')
        self.assertEqual(item, 'P')

    def test_duplicate_item4(self):
        item = duplicate_item('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')
        self.assertEqual(item, 'v')

    def test_duplicate_item5(self):
        item = duplicate_item('ttgJtRGJQctTZtZT')
        self.assertEqual(item, 't')

    def test_duplicate_item6(self):
        item = duplicate_item('CrZsJsPPZsGzwwsLwLmpwMDw')
        self.assertEqual(item, 's')

    def test_score_item1(self):
        score = item_priority('p')
        self.assertEqual(score, 16)

    def test_score_item2(self):
        score = item_priority('L')
        self.assertEqual(score, 38)

    def test_score_item3(self):
        score = item_priority('P')
        self.assertEqual(score, 42)

    def test_score_item4(self):
        score = item_priority('v')
        self.assertEqual(score, 22)

    def test_score_item5(self):
        score = item_priority('t')
        self.assertEqual(score, 20)

    def test_score_item6(self):
        score = item_priority('s')
        self.assertEqual(score, 19)

    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            score = total_score_errors(data)
        self.assertEqual(score, 157)

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            score = total_score_badges(data)
        self.assertEqual(score, 70)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            score = total_score_errors(data)
        self.assertEqual(score, 7826)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            score = total_score_badges(data)
        self.assertEqual(score, 2577)


if __name__ == '__main__':
    unittest.main()
