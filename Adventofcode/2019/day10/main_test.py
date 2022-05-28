import unittest
from main import Matrix, Coord, visible_astroids, part_1, best_station, destroy_astroids, nth_destroyed, part_2


class MainTest(unittest.TestCase):
    def test_count_example_1_part_1(self):
        with open('./example_input1', 'r') as data:
            m = Matrix.from_iter(data)
        self.assertEqual(visible_astroids(Coord(3, 4), m), 8)

    def test_example_1_part_1(self):
        with open('./example_input1', 'r') as data:
            s = part_1(data)
        self.assertEqual(s, 8)

    def test_example_2_part_1(self):
        with open('./example_input2', 'r') as data:
            s = part_1(data)
        self.assertEqual(s, 33)

    def test_example_3_part_1(self):
        with open('./example_input3', 'r') as data:
            s = part_1(data)
        self.assertEqual(s, 35)

    def test_example_4_part_1(self):
        with open('./example_input4', 'r') as data:
            s = part_1(data)
        self.assertEqual(s, 41)

    def test_example_5_part_1(self):
        with open('./example_input5', 'r') as data:
            s = part_1(data)
        self.assertEqual(s, 210)

    def test_example_1_part_2(self):
        with open('./example_input_part_2', 'r') as data:
            m = Matrix.from_iter(data)
        s = best_station(m)
        self.assertEqual(s, Coord(8, 3))
        destroyed_stars = destroy_astroids(s, m)
        self.assertEqual(next(destroyed_stars), Coord(8, 1))
        self.assertEqual(next(destroyed_stars), Coord(9, 0))
        self.assertEqual(next(destroyed_stars), Coord(9, 1))
        self.assertEqual(next(destroyed_stars), Coord(10, 0))
        self.assertEqual(next(destroyed_stars), Coord(9, 2))
        self.assertEqual(next(destroyed_stars), Coord(11, 1))
        self.assertEqual(next(destroyed_stars), Coord(12, 1))
        self.assertEqual(next(destroyed_stars), Coord(11, 2))
        self.assertEqual(next(destroyed_stars), Coord(15, 1))
        self.assertEqual(next(destroyed_stars), Coord(12, 2))
        self.assertEqual(next(destroyed_stars), Coord(13, 2))
        self.assertEqual(next(destroyed_stars), Coord(14, 2))
        self.assertEqual(next(destroyed_stars), Coord(15, 2))
        self.assertEqual(next(destroyed_stars), Coord(12, 3))
        self.assertEqual(next(destroyed_stars), Coord(16, 4))
        self.assertEqual(next(destroyed_stars), Coord(15, 4))
        self.assertEqual(next(destroyed_stars), Coord(10, 4))
        self.assertEqual(next(destroyed_stars), Coord(4, 4))
        self.assertEqual(next(destroyed_stars), Coord(2, 4))
        self.assertEqual(next(destroyed_stars), Coord(2, 3))
        self.assertEqual(next(destroyed_stars), Coord(0, 2))
        self.assertEqual(next(destroyed_stars), Coord(1, 2))
        self.assertEqual(next(destroyed_stars), Coord(0, 1))
        self.assertEqual(next(destroyed_stars), Coord(1, 1))
        self.assertEqual(next(destroyed_stars), Coord(5, 2))
        self.assertEqual(next(destroyed_stars), Coord(1, 0))
        self.assertEqual(next(destroyed_stars), Coord(5, 1))
        self.assertEqual(next(destroyed_stars), Coord(6, 1))
        self.assertEqual(next(destroyed_stars), Coord(6, 0))
        self.assertEqual(next(destroyed_stars), Coord(7, 0))
        self.assertEqual(next(destroyed_stars), Coord(8, 0))
        self.assertEqual(next(destroyed_stars), Coord(10, 1))
        self.assertEqual(next(destroyed_stars), Coord(14, 0))
        self.assertEqual(next(destroyed_stars), Coord(16, 1))
        self.assertEqual(next(destroyed_stars), Coord(13, 3))
        self.assertEqual(next(destroyed_stars), Coord(14, 3))

    def test_example_2_part_2_1(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 1), Coord(11, 12))

    def test_example_2_part_2_2(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 2), Coord(12, 1))

    def test_example_2_part_2_3(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 3), Coord(12, 2))

    def test_example_2_part_2_4(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 10), Coord(12, 8))

    def test_example_2_part_2_5(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 20), Coord(16, 0))

    def test_example_2_part_2_6(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 50), Coord(16, 9))

    def test_example_2_part_2_7(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 100), Coord(10, 16))

    def test_example_2_part_2_8(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 199), Coord(9, 6))

    def test_example_2_part_2_9(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(part_2(data), 802)

    def test_example_2_part_2_10(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 201), Coord(10, 9))

    def test_example_2_part_2_11(self):
        with open('./example_input5', 'r') as data:
            self.assertEqual(nth_destroyed(data, 299), Coord(11, 1))

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 303)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 408)


if __name__ == '__main__':
    unittest.main()
