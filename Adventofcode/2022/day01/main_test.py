import unittest
from main import largest_inventory, top_three_total_inventory_size


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        with open('./example_input', 'r') as data:
            largest = largest_inventory(data)
        self.assertEqual(largest, 24000)

    def test_example1_part_2(self):
        with open('./example_input', 'r') as data:
            total = top_three_total_inventory_size(data)
        self.assertEqual(total, 45000)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            largest = largest_inventory(data)
        self.assertEqual(largest, 67633)



if __name__ == '__main__':
    unittest.main()
