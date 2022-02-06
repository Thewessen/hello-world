import unittest
from main import Movement, Coord, create_path, closest_crossing, least_steps


class MainTest(unittest.TestCase):
    def test_coords_from_movement(self):
        coords = create_path(iter([Movement("U", 3)]))
        self.assertListEqual(list(coords), [
            Coord(0, 1),
            Coord(0, 2),
            Coord(0, 3)
        ])

    def test_coords_from_movement2(self):
        coords = create_path(iter([
            Movement("U", 2),
            Movement("R", 1),
        ]))
        self.assertListEqual(list(coords), [
            Coord(0, 1),
            Coord(0, 2),
            Coord(1, 2)
        ])

    def test_part1_example_1(self):
        line1 = "R8,U5,L5,D3"
        line2 = "U7,R6,D4,L4"
        r = closest_crossing(iter([line1, line2]))
        self.assertEqual(r, 6)

    def test_part1_example_2(self):
        line1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        line2 = "U62,R66,U55,R34,D71,R55,D58,R83"
        r = closest_crossing(iter([line1, line2]))
        self.assertEqual(r, 159)

    def test_part1_example_3(self):
        line1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        line2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        r = closest_crossing(iter([line1, line2]))
        self.assertEqual(r, 135)

    def test_part2_example_2(self):
        line1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        line2 = "U62,R66,U55,R34,D71,R55,D58,R83"
        r = least_steps(iter([line1, line2]))
        self.assertEqual(r, 610)

    def test_part2_example_3(self):
        line1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        line2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        r = least_steps(iter([line1, line2]))
        self.assertEqual(r, 410)

    def test_solution_part1(self):
        with open('./input', 'r') as data:
            r = closest_crossing(data)
        self.assertEqual(r, 221)

    def test_solution_part2(self):
        with open('./input', 'r') as data:
            r = least_steps(data)
        self.assertEqual(r, 18542)



if __name__ == '__main__':
    unittest.main()
