import unittest
from main import part_1


class MainTest(unittest.TestCase):
    def test_example_1_part_1(self):
        p = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        res = part_1(iter([p]))
        self.assertEqual(res, 43210)

    def test_example_2_part_1(self):
        p = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        res = part_1(iter([p]))
        self.assertEqual(res, 54321)

    def test_example_3_part_1(self):
        p = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
        res = part_1(iter([p]))
        self.assertEqual(res, 65210)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 298586)



if __name__ == '__main__':
    unittest.main()
