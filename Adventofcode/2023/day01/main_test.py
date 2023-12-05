import unittest
from main import calibrate, adv_calibrate


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = calibrate(data)
        self.assertEqual(n, 142)

    def test_part_2(self):
        with open('./example_input2', 'r') as data:
            n = adv_calibrate(data)
        self.assertEqual(n, 281)


if __name__ == '__main__':
    unittest.main()
