import unittest
from main import count_steps, count_ghost_steps


class MainTest(unittest.TestCase):
    # def test_part_1(self):
    #     with open('./example_input', 'r') as data:
    #         n = count_steps(data)
    #     self.assertEqual(n, 2)

    def test_part_2(self):
        with open('./example_input2', 'r') as data:
            n = count_ghost_steps(data, True)
        self.assertEqual(n, 6)

    # def test_solution_part_1(self):
    #     with open('./input', 'r') as data:
    #         n = count_steps(data)
    #     self.assertEqual(n, 11911)

    # def test_solution_part_2(self):
    #     with open('./input', 'r') as data:
    #         n = total_winnings(data, False, True)
    #     self.assertEqual(n, 248750699)


if __name__ == '__main__':
    unittest.main()
