import unittest
from main import count_pickable_papers, count_removed_papers


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = count_pickable_papers(data, debug=True)
        self.assertEqual(n, 13)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = count_pickable_papers(data, debug=True)
        self.assertEqual(n, 1449)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = count_removed_papers(data, debug=True)
        self.assertEqual(n, 43)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = count_removed_papers(data, debug=True)
        self.assertEqual(n, 8746)


if __name__ == '__main__':
    unittest.main()
