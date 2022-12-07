import unittest
from main import find_first_packet_marker_in_data_stream, find_first_message_marker_in_data_stream


class MainTest(unittest.TestCase):
    def test_example1_part_1(self):
        c = find_first_packet_marker_in_data_stream(iter(['mjqjpqmgbljsphdztnvjfqwrcgsmlb']))
        self.assertEqual(c, 7)

    def test_example2_part_1(self):
        c = find_first_packet_marker_in_data_stream(iter(['bvwbjplbgvbhsrlpgdmjqwftvncz']))
        self.assertEqual(c, 5)

    def test_example3_part_1(self):
        c = find_first_packet_marker_in_data_stream(iter(['nppdvjthqldpwncqszvftbrmjlhg']))
        self.assertEqual(c, 6)

    def test_example4_part_1(self):
        c = find_first_packet_marker_in_data_stream(iter(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']))
        self.assertEqual(c, 10)

    def test_example5_part_1(self):
        c = find_first_packet_marker_in_data_stream(iter(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']))
        self.assertEqual(c, 11)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            c = find_first_packet_marker_in_data_stream(data)
        self.assertEqual(c, 1892)

    def test_example1_part_2(self):
        c = find_first_message_marker_in_data_stream(iter(['mjqjpqmgbljsphdztnvjfqwrcgsmlb']))
        self.assertEqual(c, 19)

    def test_example2_part_2(self):
        c = find_first_message_marker_in_data_stream(iter(['bvwbjplbgvbhsrlpgdmjqwftvncz']))
        self.assertEqual(c, 23)

    def test_example3_part_2(self):
        c = find_first_message_marker_in_data_stream(iter(['nppdvjthqldpwncqszvftbrmjlhg']))
        self.assertEqual(c, 23)

    def test_example4_part_2(self):
        c = find_first_message_marker_in_data_stream(iter(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']))
        self.assertEqual(c, 29)

    def test_example5_part_2(self):
        c = find_first_message_marker_in_data_stream(iter(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']))
        self.assertEqual(c, 26)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            c = find_first_message_marker_in_data_stream(data)
        self.assertEqual(c, 2313)


if __name__ == '__main__':
    unittest.main()
