import unittest
from main import total_score_notes, score_notes_new_info


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            score = total_score_notes(data)
        self.assertEqual(score, 15)

    def test_example1_part_2(self): 
        with open('./example_input', 'r') as data:
            score = score_notes_new_info(data)
        self.assertEqual(score, 12)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            score = total_score_notes(data)
        self.assertEqual(score, 13005)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            score = total_score_notes(data)
        self.assertEqual(score, 11373)


if __name__ == '__main__':
    unittest.main()
