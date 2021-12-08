import unittest
from main import progress_days


class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        with open('./test_input') as data:
            result = progress_days(data, 80)
        self.assertEqual(result, 5934)

    def test_part_2_example(self):
        with open('./test_input') as data:
            result = progress_days(data, 256)
        self.assertEqual(result, 26984457539)


if __name__ == '__main__':
    unittest.main()

