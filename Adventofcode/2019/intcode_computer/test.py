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


if __name__ == '__main__':
    unittest.main()
