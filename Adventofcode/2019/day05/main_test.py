import unittest
from main import diagnostic_program, part_1, part_2


class MainTest(unittest.TestCase):
    def test_simple_program(self):
        data = iter(["3,0,4,0,99"])
        r = diagnostic_program(data, 37)
        self.assertEqual(r, 37)

    def test_add_program(self):
        data = iter(["3,5,3,6,1101,0,0,0,4,0,99"])
        r = diagnostic_program(data, 1, 2)
        self.assertEqual(r, 3)

    def test_prod_program(self):
        data = iter(["3,5,3,6,1102,0,0,0,4,0,99"])
        r = diagnostic_program(data, 1, 2)
        self.assertEqual(r, 2)

    def test_position_mode_equal_8(self):
        data = iter(["3,9,8,9,10,9,4,9,99,-1,8"])
        r = diagnostic_program(data, 8)
        self.assertEqual(r, 1)
        data = iter(["3,9,8,9,10,9,4,9,99,-1,8"])
        r = diagnostic_program(data, 1)
        self.assertEqual(r, 0)

    def test_position_mode_less_than_8(self):
        data = iter(["3,9,7,9,10,9,4,9,99,-1,8"])
        r = diagnostic_program(data, 8)
        self.assertEqual(r, 0)
        data = iter(["3,9,7,9,10,9,4,9,99,-1,8"])
        r = diagnostic_program(data, 1)
        self.assertEqual(r, 1)

    def test_immediate_mode_equal_8(self):
        data = iter(["3,3,1108,-1,8,3,4,3,99"])
        r = diagnostic_program(data, 8)
        self.assertEqual(r, 1)
        data = iter(["3,3,1108,-1,8,3,4,3,99"])
        r = diagnostic_program(data, 1)
        self.assertEqual(r, 0)

    def test_immediate_mode_less_than_8(self):
        data = iter(["3,3,1107,-1,8,3,4,3,99"])
        r = diagnostic_program(data, 8)
        self.assertEqual(r, 0)
        data = iter(["3,3,1107,-1,8,3,4,3,99"])
        r = diagnostic_program(data, 1)
        self.assertEqual(r, 1)

    def test_position_jump(self):
        # outputs 0 if input is 0
        data = iter(["3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"])
        r = diagnostic_program(data, 0)
        self.assertEqual(r, 0)
        # outputs 1 if input is not 0
        data = iter(["3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"])
        r = diagnostic_program(data, 3)
        self.assertEqual(r, 1)

    def test_immediate_jump(self):
        # outputs 0 if input is 0
        data = iter(["3,3,1105,-1,9,1101,0,0,12,4,12,99,1"])
        r = diagnostic_program(data, 0)
        self.assertEqual(r, 0)
        # outputs 1 if input is not 0
        data = iter(["3,3,1105,-1,9,1101,0,0,12,4,12,99,1"])
        r = diagnostic_program(data, 3)
        self.assertEqual(r, 1)

    def test_larger_example(self):
        # outputs 999 if input is less than 8
        data = iter([("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
                      "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
                      "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")])
        r = diagnostic_program(data, 0)
        self.assertEqual(r, 999)
        # outputs 1000 if input equals 8
        data = iter([("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
                      "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
                      "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")])
        r = diagnostic_program(data, 8)
        self.assertEqual(r, 1000)
        # outputs 1001 if input is greater than 8
        data = iter([("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
                      "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
                      "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")])
        r = diagnostic_program(data, 13)
        self.assertEqual(r, 1001)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = part_1(data)
        self.assertEqual(r, 13294380)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = part_2(data)
        self.assertEqual(r, 11460760)


if __name__ == '__main__':
    unittest.main()
