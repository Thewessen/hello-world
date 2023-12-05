import unittest
from main import valid_games, power_of_games


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = valid_games(data)
        self.assertEqual(n, 8)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = power_of_games(data)
        self.assertEqual(n, 2286)


if __name__ == '__main__':
    unittest.main()
