import unittest
from main import count_increasing, count_windowed_increasing


class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        exmpl = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
        self.assertIs(count_increasing(iter(exmpl)), 7)

    def test_part_2_example(self):
        exmpl = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
        self.assertIs(count_windowed_increasing(iter(exmpl)), 5)


if __name__ == '__main__':
    unittest.main()
