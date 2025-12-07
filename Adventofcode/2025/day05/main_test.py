import unittest
from main import count_fresh_ids, count_all_possible_fresh_ids


class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = count_fresh_ids(data, debug=True)
        self.assertEqual(n, 3)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = count_fresh_ids(data, debug=True)
        self.assertGreater(n, 873)
        self.assertEqual(n, 874)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = count_all_possible_fresh_ids(data, debug=True)
        self.assertEqual(n, 14)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = count_all_possible_fresh_ids(data, debug=True)
        self.assertEqual(n, 348548952146313)


if __name__ == '__main__':
    unittest.main()
