import unittest
from main import parse_input, Coord, TreeContext, count_visible_trees, max_scenic_score


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            grid = parse_input(data)
        t = grid.get_tree_context(Coord(1, 1))
        self.assertEqual(t, TreeContext(size=5,
                                        top=[0],
                                        right=[5, 1, 2],
                                        bottom=[5, 3, 5],
                                        left=[2]))
        self.assertTrue(t.is_visible('left'))
        self.assertTrue(t.is_visible('top'))
        self.assertFalse(t.is_visible('right'))
        self.assertFalse(t.is_visible('bottom'))
        self.assertTrue(t.visible)

    def test_example2_part_1(self):
        with open('./example_input', 'r') as data:
            grid = parse_input(data)
        t = grid.get_tree_context(Coord(2, 1))
        self.assertEqual(t, TreeContext(size=5,
                                        top=[3],
                                        right=[1, 2],
                                        bottom=[3, 5, 3],
                                        left=[2, 5]))
        self.assertTrue(t.is_visible('top'))
        self.assertTrue(t.is_visible('right'))
        self.assertFalse(t.is_visible('left'))
        self.assertFalse(t.is_visible('bottom'))
        self.assertTrue(t.visible)

    def test_example3_part_1(self):
        with open('./example_input', 'r') as data:
            grid = parse_input(data)
        t = grid.get_tree_context(Coord(3, 1))
        self.assertEqual(t, TreeContext(size=1,
                                        top=[7],
                                        right=[2],
                                        bottom=[3, 4, 9],
                                        left=[2, 5, 5]))
        self.assertFalse(t.is_visible('top'))
        self.assertFalse(t.is_visible('right'))
        self.assertFalse(t.is_visible('bottom'))
        self.assertFalse(t.is_visible('left'))
        self.assertFalse(t.visible)

    def test_solution_example_part_1(self):
        with open('./example_input', 'r') as data:
            v = count_visible_trees(data)
        self.assertEqual(v, 21)

    # def test_example1_part_2(self):
    #     with open('./example_input', 'r') as data:
    #         grid = parse_input(data)
    #     t = grid.get_tree_context(Coord(2, 1))
    #     self.assertEqual(t.visible_trees('top'), 1)
    #     self.assertEqual(t.visible_trees('right'), 2)
    #     self.assertEqual(t.visible_trees('bottom'), 2)
    #     self.assertEqual(t.visible_trees('left'), 1)
    #     self.assertEqual(t.scenic_score, 4)

    def test_example2_part_2(self):
        with open('./example_input', 'r') as data:
            grid = parse_input(data)
        t = grid.get_tree_context(Coord(2, 3))
        self.assertEqual(t.visible_trees('top'), 2)
        self.assertEqual(t.visible_trees('right'), 2)
        self.assertEqual(t.visible_trees('bottom'), 1)
        self.assertEqual(t.visible_trees('left'), 2)
        self.assertEqual(t.scenic_score, 8)

    def test_own_example_part_2(self):
        with open('./example_input', 'r') as data:
            grid = parse_input(data)
        t = grid.get_tree_context(Coord(3, 2))
        self.assertEqual(t.visible_trees('top'), 2)
        self.assertEqual(t.visible_trees('right'), 1)
        self.assertEqual(t.visible_trees('bottom'), 1)
        self.assertEqual(t.visible_trees('left'), 1)
        self.assertEqual(t.scenic_score, 2)

    def test_solution_example_part_2(self):
        with open('./example_input', 'r') as data:
            v = max_scenic_score(data)
        self.assertEqual(v, 8)


if __name__ == '__main__':
    unittest.main()
