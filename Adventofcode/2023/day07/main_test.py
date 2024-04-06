import unittest
from main import total_winnings


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = total_winnings(data)
        self.assertEqual(n, 6440)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = total_winnings(data, False, True)
        self.assertEqual(n, 5905)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            n = total_winnings(data)
        self.assertEqual(n, 247961593)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            n = total_winnings(data, False, True)
        self.assertEqual(n, 248750699)


if __name__ == '__main__':
    unittest.main()
