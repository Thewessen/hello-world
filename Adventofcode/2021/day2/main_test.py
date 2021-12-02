import unittest
from main import BaseSubState, AdvSubState

class MainTest(unittest.TestCase):
    def test_part_1_example(self):
        state = BaseSubState(0, 0)
        state.process_instructions([
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ])
        self.assertEqual(state, BaseSubState(15, 10))
        self.assertEqual(state.sol(), 150)

    def test_part_2_example(self):
        state = AdvSubState(0, 0, 0)
        state.process_instructions([
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ])
        self.assertEqual(state, BaseSubState(15, 60))
        self.assertEqual(state.sol(), 900)


if __name__ == '__main__':
    unittest.main()
