import unittest
from main import count_superfluous_elves, count_overlapping_sections


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            c = count_superfluous_elves(data)
        self.assertEqual(c, 2)

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            c = count_overlapping_sections(data)
        self.assertEqual(c, 4)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            c = count_superfluous_elves(data)
        self.assertEqual(c, 444)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            c = count_overlapping_sections(data)
        self.assertEqual(c, 801)


if __name__ == '__main__':
    unittest.main()
