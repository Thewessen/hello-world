import unittest
from main import parse_input, count_orbits, santa_distance


class MainTest(unittest.TestCase):
    def test_example_orbits_map_count(self):
        data = parse_input(iter((
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L")))
        orbits, planets = count_orbits(data)
        self.assertEqual(planets, 12)
        self.assertEqual(orbits, 42)

    def test_example_santa_distance(self):
        data = parse_input(iter((
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN"
        )))
        dist = santa_distance(data)
        self.assertEqual(dist, 4)

if __name__ == '__main__':
    unittest.main()
