import unittest
from main import grand_total, grand_total_part_2


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = grand_total(data, debug=True)
        self.assertEqual(n, 4277556)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = grand_total(data, debug=True)
        self.assertEqual(n, 6295830249262)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = grand_total_part_2(data, debug=True)
        self.assertEqual(n, 3263827)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = grand_total_part_2(data, debug=True)
        self.assertEqual(n, 9194682052782)


if __name__ == '__main__':
    unittest.main()
