import unittest
from main import calc_gamma_epsilon_rate, calc_oxygen_co2_rate

class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        gamma_rate, epsilon_rate = calc_gamma_epsilon_rate(iter([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ]))
        self.assertEqual(gamma_rate, 22)
        self.assertEqual(epsilon_rate, 9)

    def test_part_2_example(self):
        oxygen_rate, co2_rate = calc_oxygen_co2_rate([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ])
        self.assertEqual(oxygen_rate, 23)
        self.assertEqual(co2_rate, 10)
        

if __name__ == '__main__':
    unittest.main()
