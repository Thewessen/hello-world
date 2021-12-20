import unittest
from main import parse_input, create_coord_map, count_unique_beacons, possible_match, largest_manhattan_distance


class MainTest(unittest.TestCase):
    def test_coord_map_exists_for_all_scanners_in_input(self):
        with open('./test_input', 'r') as data:
            scanners = list(parse_input(data))
        for s0 in scanners:
            self.assertTrue(any(create_coord_map(s0.distance_map,
                                                 s1.distance_map)
                                for s1 in scanners
                                if s1 != s0))

    def test_only_one_mapping_exists_in_input(self):
        with open('./input', 'r') as data:
            scanners = list(parse_input(data))
        for s0 in scanners:
            for s1 in scanners:
                if s0 == s1:
                    continue
                matched_mapping = dict()
                for coord_a, dist_a in s0.distance_map.items():
                    matched_mapping[coord_a] = list()
                    for coord_b, dist_b in s1.distance_map.items():
                        if possible_match(dist_a, dist_b):
                            matched_mapping[coord_a].append(coord_b)
                crds = matched_mapping.values()
                if len(set(matched_mapping.keys())) == len(crds) or len(crds) >= 12:
                    self.assertTrue(all(len(coords) == 0 or len(coords) == 1 for coords in crds))

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_unique_beacons(data)
        self.assertEqual(r, 79)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_unique_beacons(data)
        self.assertEqual(r, 335)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = largest_manhattan_distance(data)
        self.assertEqual(r, 3621)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = largest_manhattan_distance(data)
        self.assertEqual(r, 10864)


if __name__ == '__main__':
    unittest.main()
