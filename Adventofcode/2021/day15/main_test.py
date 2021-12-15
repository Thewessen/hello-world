import unittest
from main import Grid, find_shortest_path, enhance_data

class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            grid = Grid.from_iter(line.strip() for line in data)
        self.assertEqual(find_shortest_path(grid), 40)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            grid = Grid.from_iter(enhance_data(data))
        self.assertEqual(find_shortest_path(grid), 315)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            grid = Grid.from_iter(line.strip() for line in data)
        self.assertEqual(find_shortest_path(grid), 673)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            grid = Grid.from_iter(enhance_data(data))
        self.assertEqual(find_shortest_path(grid), 2893)



if __name__ == '__main__':
    unittest.main()
