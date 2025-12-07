import unittest
from main import count_invalid_ids, count_more_invalid_ids, generate_invalid_ids, Range

def read_char_by_char(data):
    while True:
        c = data.read(1)
        if not c:
            break
        yield c

class MainTest(unittest.TestCase):
    def test_part_1(self):
        with open('./example_input', 'r') as data:
            n = count_invalid_ids(read_char_by_char(data), debug=True)
        self.assertEqual(n, 1227775554)

    def test_bug_1(self):
        n = count_invalid_ids(iter("755745207-755766099"), debug=True)
        self.assertEqual(n, 0)

    def test_bug_2(self):
        n = count_invalid_ids(iter("48-130"), debug=True)
        self.assertEqual(n, 385)

    def test_solution_1(self):
        with open('./input', 'r') as data:
            n = count_invalid_ids(read_char_by_char(data), debug=True)
        self.assertEqual(n, 23534117921)

    def test_part_2(self):
        with open('./example_input', 'r') as data:
            n = count_more_invalid_ids(read_char_by_char(data), debug=True)
        self.assertEqual(n, 4174379265)

    def test_bug_2_1(self):
        n = count_more_invalid_ids(iter("998-1012"), debug=True)
        self.assertEqual(n, 2009)

    def test_bug_2_2(self):
        n = count_more_invalid_ids(iter("222220-222224"), debug=True)
        self.assertEqual(n, 222222)

    def test_edge_case_2(self):
        n = count_more_invalid_ids(iter("14-1234"), debug=True)
        # self.assertEqual(n, 5039)
        self.assertEqual(n, 8812)

    def test_solution_2(self):
        with open('./input', 'r') as data:
            n = count_more_invalid_ids(read_char_by_char(data), debug=True)
        self.assertGreater(n, 31670221358)
        self.assertLess(n, 31755323498)

    # def test_generate_invalid_ids_1(self):
    #     invalid_ids = list(generate_invalid_ids(Range(10, 132), True))
    #     print(invalid_ids)
    #     self.assertEqual(invalid_ids, [
    #         11,
    #         22,
    #         33,
    #         44,
    #         55,
    #         66,
    #         77,
    #         88,
    #         99,
    #         111,
    #     ])

    # def test_generate_invalid_ids_2(self):
    #     invalid_ids = list(generate_invalid_ids(Range(1010, 1320), True))
    #     print(invalid_ids)
    #     self.assertEqual(invalid_ids, [
    #         1010,
    #         1111,
    #         1212,
    #         1313,
    #     ])

    # def test_generate_invalid_ids_3(self):
    #     invalid_ids = list(generate_invalid_ids(Range(131, 232), True))
    #     print(invalid_ids)
    #     self.assertEqual(invalid_ids, [
    #         222,
    #     ])


if __name__ == '__main__':
    unittest.main()
