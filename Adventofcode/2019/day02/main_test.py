import unittest
from main import parse_input, program


class MainTest(unittest.TestCase):
    def test_example1_solution_part_1(self):
        inp = parse_input('1,0,0,0,99')
        res = parse_input('2,0,0,0,99')
        self.assertListEqual(program(inp), res)

    def test_example2_solution_part_1(self):
        inp = parse_input('2,3,0,3,99')
        res = parse_input('2,3,0,6,99')
        self.assertListEqual(program(inp), res)

    def test_example3_solution_part_1(self):
        inp = parse_input('2,4,4,5,99,0')
        res = parse_input('2,4,4,5,99,9801')
        self.assertListEqual(program(inp), res)

    def test_example4_solution_part_1(self):
        inp = parse_input('1,1,1,4,99,5,6,0,99')
        res = parse_input('30,1,1,4,2,5,6,0,99')
        self.assertListEqual(program(inp), res)


if __name__ == '__main__':
    unittest.main()
