import unittest
from main import exec_program


class MainTest(unittest.TestCase):
    def test_three_times_3_9(self):
        inp = "39"
        r = exec_program(iter([
            'inp z',
            'inp x',
            'mul z 3',
            'eql z x',
        ]), inp)
        self.assertEqual(r['z'], 1)

    def test_not_three_times_2_4(self):
        inp = "24"
        r = exec_program(iter([
            'inp z',
            'inp x',
            'mul z 3',
            'eql z x',
        ]), inp)
        self.assertEqual(r['z'], 0)

    def test_binary_program_7(self):
        inp = "7"
        r = exec_program(iter([
            'inp w',
            'add z w',
            'mod z 2',
            'div w 2',
            'add y w',
            'mod y 2',
            'div w 2',
            'add x w',
            'mod x 2',
            'div w 2',
            'mod w 2',
        ]), inp)
        self.assertEqual(f'{r["w"]}{r["x"]}{r["y"]}{r["z"]}', "0111")


if __name__ == '__main__':
    unittest.main()
