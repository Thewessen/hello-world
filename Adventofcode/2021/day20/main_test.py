import unittest
from main import PartialImage, enhanced_image_from_data

class MainTest(unittest.TestCase):
    def test_example_solution_part_1_enhance_1(self):
        with open('./test_input', 'r') as data:
            img = enhanced_image_from_data(data, 1)
        r = PartialImage.from_iter(iter([
            '.##.##.',
            '#..#.#.',
            '##.#..#',
            '####..#',
            '.#..##.',
            '..##..#',
            '...#.#.',
        ]))
        self.assertEqual(img, r)

    def test_example_solution_part_1_enhance_2(self):
        with open('./test_input', 'r') as data:
            img = enhanced_image_from_data(data, 2)
        r = PartialImage.from_iter(iter([
            '.......#.',
            '.#..#.#..',
            '#.#...###',
            '#...##.#.',
            '#.....#.#',
            '.#.#####.',
            '..#.#####',
            '...##.##.',
            '....###..',
        ]))
        self.assertEqual(img, r)

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            img = enhanced_image_from_data(data, 2)
        self.assertEqual(img.lit, 35)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            img = enhanced_image_from_data(data, 2)
        self.assertEqual(img.lit, 5819)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            img = enhanced_image_from_data(data, 50)
        self.assertEqual(img.lit, 3351)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            img = enhanced_image_from_data(data, 50)
        self.assertEqual(img.lit, 18516)


if __name__ == '__main__':
    unittest.main()
