import unittest
from main import Grid, parse_input, count_dots_first_fold, get_code
from more_itertools import take

class MainTest(unittest.TestCase):
    def test_example_first_fold(self):
        with open('./test_input', 'r') as data:
            coords, instructs = parse_input(data)
            instr = next(instructs)
            coords = set(instr.fold(*coord) for coord in coords)
            r = Grid.from_coords(coords)
        self.assertEqual(r, Grid.from_str([
            '#.##..#..#.',
            '#...#......',
            '......#...#',
            '#...#......',
            '.#.#..#.###',
            '...........',
            '...........',
        ]))

    def test_example_second_fold(self):
        with open('./test_input', 'r') as data:
            coords, instructs = parse_input(data)
            for instr in take(2, instructs):
                coords = set(instr.fold(*coord) for coord in coords)
            r = Grid.from_coords(coords)
        self.assertEqual(r, Grid.from_str([
            '#####',
            '#...#',
            '#...#',
            '#...#',
            '#####',
            '.....',
            '.....',
        ]))

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_dots_first_fold(data)
        self.assertEqual(r, 17)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_dots_first_fold(data)
        self.assertEqual(r, 810)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            g = get_code(data)
        self.assertEqual(g, Grid.from_str([
            '#..#.#....###..#..#.###...##..####.###.',
            '#..#.#....#..#.#..#.#..#.#..#.#....#..#',
            '####.#....###..#..#.###..#....###..#..#',
            '#..#.#....#..#.#..#.#..#.#.##.#....###.',
            '#..#.#....#..#.#..#.#..#.#..#.#....#.#.',
            '#..#.####.###...##..###...###.#....#..#',
        ]))


if __name__ == '__main__':
    unittest.main()
