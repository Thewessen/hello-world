import unittest
from main import BaseSubState, AdvSubState

class MainTest(unittest.TestCase):
    def test_example_solution_part_1(self):
        state = BaseSubState(0, 0)
        with open('./test_input', 'r') as data:
            state.process_instructions(data)
        self.assertEqual(state, BaseSubState(15, 10))
        self.assertEqual(state.sol(), 150)

    def test_solution_part_1(self):
        state = BaseSubState(0, 0)
        with open('./input', 'r') as data:
            state.process_instructions(data)
        self.assertEqual(state.sol(), 1947824)

    def test_example_solution_part_2(self):
        state = AdvSubState(0, 0, 0)
        with open('./test_input', 'r') as data:
            state.process_instructions(data)
        self.assertEqual(state, BaseSubState(15, 60))
        self.assertEqual(state.sol(), 900)

    def test_solution_part_2(self):
        state = AdvSubState(0, 0, 0)
        with open('./input', 'r') as data:
            state.process_instructions(data)
        self.assertEqual(state.sol(), 1813062561)


if __name__ == '__main__':
    unittest.main()
