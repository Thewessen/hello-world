import unittest
from main import play_test_game, play_real_game


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = play_test_game(data)
        self.assertEqual(r, 739785)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = play_test_game(data)
        self.assertEqual(r, 855624)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = play_real_game(data)
        self.assertEqual(r, 444356092776315)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = play_real_game(data)
        self.assertEqual(r, 187451244607486)


if __name__ == '__main__':
    unittest.main()
