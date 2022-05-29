import unittest
from main import parse_input, Coord, part_1, part_2
from more_itertools import consume


class MainTest(unittest.TestCase):
    def test_example_part_1_parse_input(self):
        with open('./test_input1', 'r') as data:
            jupiter = parse_input(data)
        self.assertListEqual(jupiter.positions, [
            Coord(-1, 0, 2),
            Coord(2, -10, -7),
            Coord(4, -8, 8),
            Coord(3, 5, -1),
        ])

    def test_example1_part_1(self):
        with open('./test_input1', 'r') as data:
            jupiter = parse_input(data)

        # step 0
        self.assertListEqual(jupiter.positions, [
            Coord(-1,   0,  2),
            Coord( 2, -10, -7),
            Coord( 4,  -8,  8),
            Coord( 3,   5, -1),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( 0,  0,  0),
             Coord( 0,  0,  0),
             Coord( 0,  0,  0),
             Coord( 0,  0,  0),
        ])

        # step 1
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 2, -1,  1),
            Coord( 3, -7, -4),
            Coord( 1, -7,  5),
            Coord( 2,  2,  0),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 3, -1, -1),
            Coord( 1,  3,  3),
            Coord(-3,  1, -3),
            Coord(-1, -3,  1),
        ])

        # step 2
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 5, -3, -1),
            Coord( 1, -2,  2),
            Coord( 1, -4, -1),
            Coord( 1, -4,  2),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 3, -2, -2),
            Coord(-2,  5,  6),
            Coord( 0,  3, -6),
            Coord(-1, -6,  2),
        ])

        # step 3
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 5, -6, -1),
            Coord( 0,  0,  6),
            Coord( 2,  1, -5),
            Coord( 1, -8,  2),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 0, -3,  0),
            Coord(-1,  2,  4),
            Coord( 1,  5, -4),
            Coord( 0, -4,  0),
        ])

        # step 4
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 2, -8,  0),
            Coord( 2,  1,  7),
            Coord( 2,  3, -6),
            Coord( 2, -9,  1),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord(-3, -2,  1),
            Coord( 2,  1,  1),
            Coord( 0,  2, -1),
            Coord( 1, -1, -1),
        ])

        # step 5
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord(-1, -9,  2),
            Coord( 4,  1,  5),
            Coord( 2,  2, -4),
            Coord( 3, -7, -1),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord(-3, -1,  2),
            Coord( 2,  0, -2),
            Coord( 0, -1,  2),
            Coord( 1,  2, -2),
        ])

        # step 6
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord(-1, -7,  3),
            Coord( 3,  0,  0),
            Coord( 3, -2,  1),
            Coord( 3, -4, -2),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 0,  2,  1),
            Coord(-1, -1, -5),
            Coord( 1, -4,  5),
            Coord( 0,  3, -1),
        ])

        # step 7
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 2, -2,  1),
            Coord( 1, -4, -4),
            Coord( 3, -7,  5),
            Coord( 2,  0,  0),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 3,  5, -2),
            Coord(-2, -4, -4),
            Coord( 0, -5,  4),
            Coord(-1,  4,  2),
        ])

        # step 8
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 5,  2, -2),
            Coord( 2, -7, -5),
            Coord( 0, -9,  6),
            Coord( 1,  1,  3),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 3,  4, -3),
            Coord( 1, -3, -1),
            Coord(-3, -2,  1),
            Coord(-1,  1,  3),
        ])

        # step 9
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 5,  3, -4),
            Coord( 2, -9, -3),
            Coord( 0, -8,  4),
            Coord( 1,  1,  5),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord( 0,  1, -2),
            Coord( 0, -2,  2),
            Coord( 0,  1, -2),
            Coord( 0,  0,  2),
        ])

        # step 10
        next(jupiter)
        self.assertListEqual(jupiter.positions, [
            Coord( 2,  1, -3),
            Coord( 1, -8,  0),
            Coord( 3, -6,  1),
            Coord( 2,  0,  4),
        ])
        self.assertListEqual(jupiter.velocities, [
            Coord(-3, -2,  1),
            Coord(-1,  1,  3),
            Coord( 3,  2, -3),
            Coord( 1, -1, -1),
        ])

        self.assertEqual(jupiter.energy, 179)

    def test_example2_part_1(self):
        with open('./test_input2', 'r') as data:
            jupiter = parse_input(data)

        # step 0
        self.assertListEqual(jupiter.positions, [
            Coord( -8, -10,   0),
            Coord(  5,   5,  10),
            Coord(  2,  -7,   3),
            Coord(  9,  -8,  -3),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord(  0,   0,   0),
             Coord(  0,   0,   0),
             Coord(  0,   0,   0),
             Coord(  0,   0,   0),
        ])

        # After 10 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord( -9, -10,   1),
            Coord(  4,  10,   9),
            Coord(  8, -10,  -3),
            Coord(  5, -10,   3),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -2,  -2,  -1),
             Coord( -3,   7,  -2),
             Coord(  5,  -1,  -2),
             Coord(  0,  -4,   5),
        ])

        # After 20 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord(-10,   3,  -4),
            Coord(  5, -25,   6),
            Coord( 13,   1,   1),
            Coord(  0,   1,   7),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -5,   2,   0),
             Coord(  1,   1,  -4),
             Coord(  5,  -2,   2),
             Coord( -1,  -1,   2),
        ])

        # After 30 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord( 15,  -6,  -9),
            Coord( -4, -11,   3),
            Coord(  0,  -1,  11),
            Coord( -3,  -2,   5),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -5,   4,   0),
             Coord( -3, -10,   0),
             Coord(  7,   4,   3),
             Coord(  1,   2,  -3),
        ])

        # After 40 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord( 14, -12,  -4),
            Coord( -1,  18,   8),
            Coord( -5, -14,   8),
            Coord(  0, -12,  -2),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( 11,   3,   0),
             Coord( -5,   2,   3),
             Coord(  1,  -2,   0),
             Coord( -7,  -3,  -3),
        ])

        # After 50 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord(-23,   4,   1),
            Coord( 20, -31,  13),
            Coord( -4,   6,   1),
            Coord( 15,   1,  -5),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -7,  -1,   2),
             Coord(  5,   3,   4),
             Coord( -1,   1,  -3),
             Coord(  3,  -3,  -3),
        ])

        # After 60 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord( 36, -10,   6),
            Coord(-18,  10,   9),
            Coord(  8, -12,  -3),
            Coord(-18,  -8,  -2),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord(  5,   0,   3),
             Coord( -3,  -7,   5),
             Coord( -2,   1,  -7),
             Coord(  0,   6,  -1),
        ])

        # After 70 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord(-33,  -6,   5),
            Coord( 13,  -9,   2),
            Coord( 11,  -8,   2),
            Coord( 17,   3,   1),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -5,  -4,   7),
             Coord( -2,  11,   3),
             Coord(  8,  -6,  -7),
             Coord( -1,  -1,  -3),
        ])

        # After 80 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord( 30,  -8,   3),
            Coord( -2,  -4,   0),
            Coord(-18,  -7,  15),
            Coord( -2,  -1,  -8),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord(  3,   3,   0),
             Coord(  4, -13,   2),
             Coord( -8,   2,  -2),
             Coord(  1,   8,   0),
        ])

        # After 90 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord(-25,  -1,   4),
            Coord(  2,  -9,   0),
            Coord( 32,  -8,  14),
            Coord( -1,  -2,  -8),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord(  1,  -3,   4),
             Coord( -3,  13,  -1),
             Coord(  5,  -4,   6),
             Coord( -3,  -6,  -9),
        ])

        # After 100 steps:
        consume(jupiter, 10)
        self.assertListEqual(jupiter.positions, [
            Coord(  8, -12,  -9),
            Coord( 13,  16,  -3),
            Coord(-29, -11,  -1),
            Coord( 16, -13,  23),
        ])
        self.assertListEqual(jupiter.velocities, [
             Coord( -7,   3,   0),
             Coord(  3, -11,  -5),
             Coord( -3,   7,   4),
             Coord(  7,   1,   1),
        ])

        self.assertEqual(jupiter.energy, 1940)

    def test_example1_part_2(self):
        with open('./test_input1', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 2772)

    def test_example2_part_2(self):
        with open('./test_input2', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 4686774924)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 9999)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 282399002133976)


if __name__ == '__main__':
    unittest.main()
