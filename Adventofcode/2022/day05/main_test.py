import unittest
from main import top_boxes_9000_instructions, top_boxes_9001_instructions


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            c = top_boxes_9000_instructions(data)
        self.assertEqual(c, 'CMZ')

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            c = top_boxes_9000_instructions(data)
        self.assertEqual(c, 'RTGWZTHLD')

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            c = top_boxes_9001_instructions(data)
        self.assertEqual(c, 'MCD')


if __name__ == '__main__':
    unittest.main()
