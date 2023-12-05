import unittest
from main import lowest_seed_location, ranged_seed_lowest_location, Range, Mapping


class MainTest(unittest.TestCase):
    # def test_part_1(self):
    #     with open('./example_input', 'r') as data:
    #         n = lowest_seed_location(data)
    #     self.assertEqual(n, 35)

    def test_mapping_get_item_from_range(self):
        seed = Range(0, 10)
        mapping = Mapping(Range(2, 4), Range(5, 4))
        self.assertTrue(seed in mapping)
        self.assertListEqual(mapping[seed], [
            Range(0, 2),
            Range(5, 4),
            Range(6, 4)
        ])


    # def test_part_2(self):
    #     with open('./example_input', 'r') as data:
    #         n = ranged_seed_lowest_location(data)
    #     self.assertEqual(n, 82)

    # def test_solution_part_1(self):
    #     with open('./input', 'r') as data:
    #         n = lowest_seed_location(data)
    #     self.assertEqual(n, 177942185)

    # def test_solution_part_2(self):
    #     with open('./input', 'r') as data:
    #         n = ranged_seed_lowest_location(data)
    #     self.assertEqual(n, 0)


if __name__ == '__main__':
    unittest.main()
