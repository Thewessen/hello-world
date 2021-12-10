import unittest
from main import calc_gamma_epsilon_rate, calc_oxygen_co2_rate

class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            gamma_rate, epsilon_rate = calc_gamma_epsilon_rate(data)
        self.assertEqual(gamma_rate, 22)
        self.assertEqual(epsilon_rate, 9)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            gamma_rate, epsilon_rate = calc_gamma_epsilon_rate(data)
        self.assertEqual(gamma_rate * epsilon_rate, 1307354)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            oxygen_rate, co2_rate = calc_oxygen_co2_rate(data.readlines())
        self.assertEqual(oxygen_rate, 23)
        self.assertEqual(co2_rate, 10)
        
    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            oxygen_rate, co2_rate = calc_oxygen_co2_rate(data.readlines())
        self.assertEqual(oxygen_rate * co2_rate, 482500)


if __name__ == '__main__':
    unittest.main()
