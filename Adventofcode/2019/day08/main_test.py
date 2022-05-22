import unittest
from main import part_1, part_2


class MainTest(unittest.TestCase):
    def test_example_part_2(self):
        enc = iter(['0222112222120000'])
        pixels = list(part_2(enc))
        self.assertListEqual(['0','1','1','0'], pixels)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 298586)


if __name__ == '__main__':
    unittest.main()
