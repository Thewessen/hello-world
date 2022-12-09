import unittest
from main import count_tail_small_rope, count_tail_larger_rope


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            c = count_tail_small_rope(data)
        self.assertEqual(c, 13)

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            c = count_tail_larger_rope(data)
        self.assertEqual(c, 1)

    def test_example2_part_2(self):
        with open('./example_input2', 'r') as data:
            c = count_tail_larger_rope(data)
        self.assertEqual(c, 36)


if __name__ == '__main__':
    unittest.main()
