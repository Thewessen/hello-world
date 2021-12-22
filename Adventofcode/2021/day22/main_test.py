import unittest
from main import Cuboid, Range, count_active_cubes


class MainTest(unittest.TestCase):
    def test_equality_range(self):
        a = Range(42, 47)
        b = Range(42, 47)
        self.assertEqual(a, b)

    def test_cuboids_sub(self):
        a = Cuboid(Range(-3, 1), Range(1, 2), Range(1, 2))
        b = Cuboid(Range(0, 3), Range(1, 2), Range(1, 2))
        r = [Cuboid(Range(-3, -1), Range(1, 2), Range(1, 2))]
        self.assertListEqual(a - b, r)

    def test_subset_bug(self):
        a = Cuboid(x=Range(-20, 26), y=Range(-36, 17), z=Range(-47, 7))
        b = Cuboid(x=Range(-20, 26), y=Range(-36, -22), z=Range(8, 28))
        self.assertFalse(b.subset(a))

    def test_edge_case(self):
        a = Cuboid(x=Range(-1, 2), y=Range(0, 2), z=Range(0, 2))
        b = Cuboid(x=Range(0, 2), y=Range(0, 2), z=Range(0, 2))
        r = [Cuboid(Range(-1, -1), Range(0, 2), Range(0, 2))]
        self.assertListEqual(a - b, r)
        self.assertEqual(len(r[0]), 9)

    def test_overlapping_bug(self):
        a = Cuboid(x=Range(27, 28), y=Range(-21, -4), z=Range(28, 28))
        b = Cuboid(x=Range(24, 28), y=Range(23, 23), z=Range(28, 28))
        self.assertFalse(a.overlapping(b))
        self.assertFalse(b.overlapping(a))

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_active_cubes(data, Cuboid.cube(-50, 50))
        self.assertEqual(r, 590784)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_active_cubes(data, Cuboid.cube(-50, 50))
        self.assertEqual(r, 581108)

    def test_example_solution_part_2(self):
        with open('./test_input2', 'r') as data:
            r = count_active_cubes(data)
        self.assertEqual(r, 2758514936282235)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = count_active_cubes(data)
        self.assertEqual(r, 1325473814582641)


if __name__ == '__main__':
    unittest.main()
