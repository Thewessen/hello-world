import unittest
from main import lowest_seed_location, ranged_seed_lowest_location, Mapping, Range, Map


class MainTest(unittest.TestCase):
    # def test_part_1(self):
    #     with open('./example_input', 'r') as data:
    #         n = lowest_seed_location(data)
    #     self.assertEqual(n, 35)

    # def test_get_range_item_from_mapping_1(self):
    #     # full overlap
    #     seeds = Range(0, 10)
    #     mapping = Mapping(Range(1, 2), Range(3, 2))
    #     self.assertTrue(seeds in mapping)
    #     self.assertEqual(mapping[seeds], (
    #         Range(0, 1),
    #         Range(3, 2),
    #         Range(3, 7)
    #     ))

    def test_get_range_item_from_mappings_1(self):
        # full overlap
        seeds = Range(0, 10)
        [Range(0, 1), Range(1, 9)]
        [Range(0, 1), Range(1, 2), Range(3, 7)]
        [Range(0, 1), Range(1, 2), Range(3, 2), Range(5, 5)]
        mappings = [
            Mapping(Range(1, 2), Range(3, 2)),
            Mapping(Range(3, 2), Range(8, 2)),
        ]
        [
            Mapping(Range(0, 1), Range(0, 1)),
            Mapping(Range(1, 2), Range(3, 2)),
            Mapping(Range(3, 2), Range(8, 2)),
            Mapping(Range(5, 5), Range(5, 5)),
        ]
        map = Map('A', ranges=mappings)
        self.assertEqual(map[seeds], (
            Range(0, 1),
            Range(3, 2),
            Range(8, 2),
            Range(5, 5)
        ))

    # def test_get_range_item_from_mapping_2(self):
    #     # head overlap
    #     seeds = Range(0, 10)
    #     mapping = Mapping(Range(9, 2), Range(0, 2))
    #     self.assertTrue(seeds in mapping)
    #     self.assertEqual(mapping[seeds], (
    #         Range(0, 9),
    #         Range(0, 1)
    #     ))

    # def test_get_range_item_from_mapping_3(self):
    #     # tail overlap
    #     seeds = Range(0, 10)
    #     mapping = Mapping(Range(0, 2), Range(6, 2))
    #     plan = GardingPlan(seeds=[0, 10], maps=[Map('A', ranges=[mapping])])
    #     self.assertTrue(seeds in mapping)
    #     self.assertEqual(mapping[seeds], (
    #         Range(6, 2),
    #         Range(2, 8)
    #     ))
    #     self.assertEqual(plan.find_lowest_location_seed(), 2)

    # def test_get_range_item_from_mapping_4(self):
    #     # no overlap
    #     seeds = Range(2, 4)
    #     mapping = Mapping(Range(0, 10), Range(10, 10))
    #     self.assertTrue(seeds in mapping)
    #     self.assertEqual(mapping[seeds], (
    #         Range(12, 4)
    #     ))

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
