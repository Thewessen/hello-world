import unittest
from main import count_overlapping_coords


class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            result = count_overlapping_coords(data)
        self.assertEqual(result, 5)

    def test_part_2_example(self):
        with open('./test_input') as data:
            result = count_overlapping_coords(data, True)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
