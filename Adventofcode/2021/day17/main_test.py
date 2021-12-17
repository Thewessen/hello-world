import unittest
from main import calc_max_height, valid_velocity_values


class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = calc_max_height(data)
        self.assertEqual(r, 45) 

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = len(set(valid_velocity_values(data)))
        self.assertEqual(r, 112) 

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = calc_max_height(data)
        self.assertEqual(r, 9180) 

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = len(set(valid_velocity_values(data)))
        self.assertEqual(r, 3767) 


if __name__ == '__main__':
    unittest.main()
