import unittest
from main import score_polymer


class MainTest(unittest.TestCase):
    def test_example_part_1_after_step_1(self):
        with open('./test_input', 'r') as data:
            result = score_polymer(data, 1)
        self.assertEqual(result, 1)

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            result = score_polymer(data, 10)
        self.assertEqual(result, 1588)

    # def example_part_1_after_step_2(self):
    #     with open('./test_input', 'r') as data:
    #         result = ''.join(pair_insertion(data, 2))
    #     self.assertEqual(result, 'NBCCNBBBCBHCB')

    # def example_part_1_after_step_3(self):
    #     with open('./test_input', 'r') as data:
    #         result = ''.join(pair_insertion(data, 3))
    #     self.assertEqual(result, 'NBBBCNCCNBBNBNBBCHBHHBCHB')

    # def example_part_1_after_step_4(self):
    #     with open('./test_input', 'r') as data:
    #         result = ''.join(pair_insertion(data, 4))
    #     self.assertEqual(result, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    def test_solution_example_part_2(self):
        with open('./test_input', 'r') as data:
            result = score_polymer(data, 40)
        self.assertEqual(result, 2188189693529)


if __name__ == '__main__':
    unittest.main()
