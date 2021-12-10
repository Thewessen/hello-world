import unittest
from main import count_increasing, count_windowed_increasing


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_increasing(data)
        self.assertEqual(r, 7)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_increasing(data)
        self.assertEqual(r, 1532)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = count_windowed_increasing(data)
        self.assertEqual(r, 5)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = count_windowed_increasing(data)
        self.assertEqual(r, 1571)


if __name__ == '__main__':
    unittest.main()
