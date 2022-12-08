import unittest
from main import sum_dir_sizes_lt, smallest_deleted_dir


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            d = sum_dir_sizes_lt(data)
        self.assertEqual(d, 95437)

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            d = smallest_deleted_dir(data)
        self.assertEqual(d, 24933642)


if __name__ == '__main__':
    unittest.main()
