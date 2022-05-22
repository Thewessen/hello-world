import unittest
from Program import Program

class MainTest(unittest.TestCase):
    def test_example1_solution_part_1(self):
        p = Program.from_str('1,0,0,0,99')
        p.run()
        res = '2,0,0,0,99'
        self.assertEqual(str(p.mem), res)

    def test_example2_solution_part_1(self):
        p = Program.from_str('2,3,0,3,99')
        p.run()
        res = '2,3,0,6,99'
        self.assertEqual(str(p.mem), res)

    def test_example3_solution_part_1(self):
        p = Program.from_str('2,4,4,5,99,0')
        p.run()
        res = '2,4,4,5,99,9801'
        self.assertEqual(str(p.mem), res)

    def test_example4_solution_part_1(self):
        p = Program.from_str('1,1,1,4,99,5,6,0,99')
        p.run()
        res = '30,1,1,4,2,5,6,0,99'
        self.assertEqual(str(p.mem), res)

    def test_relative_base_day9_part1_example1(self):
        p = Program.from_str('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        self.assertListEqual(list(p), [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

    def test_relative_base_day9_part1_example2(self):
        p = Program.from_str('1102,34915192,34915192,7,4,7,99,0')
        # examlpe hints it's a 16digit number
        self.assertEqual(len(str(next(p))), 16)

    def test_relative_base_day9_part1_example3(self):
        p = Program.from_str('104,1125899906842624,99')
        # examlpe hints at middle number
        self.assertEqual(next(p), 1125899906842624)

if __name__ == '__main__':
    unittest.main()
