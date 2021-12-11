import unittest
from main import OctopusSchool, count_flashes, first_step_synced
from more_itertools import consume

class MainTest(unittest.TestCase):
    def test_example_part_1_after_1_day(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '6594254334',
            '3856965822',
            '6375667284',
            '7252447257',
            '7468496589',
            '5278635756',
            '3287952832',
            '7993992245',
            '5957959665',
            '6394862637',
        ]))
        consume(school, 1)
        self.assertEqual(school, sol)

    def test_example_part_1_after_2_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '8807476555',
            '5089087054',
            '8597889608',
            '8485769600',
            '8700908800',
            '6600088989',
            '6800005943',
            '0000007456',
            '9000000876',
            '8700006848',
        ]))
        consume(school, 2)
        self.assertEqual(school, sol)

    def test_example_part_1_after_3_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '0050900866',
            '8500800575',
            '9900000039',
            '9700000041',
            '9935080063',
            '7712300000',
            '7911250009',
            '2211130000',
            '0421125000',
            '0021119000',
        ]))
        consume(school, 3)
        self.assertEqual(school, sol)

    def test_example_part_1_after_4_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '2263031977',
            '0923031697',
            '0032221150',
            '0041111163',
            '0076191174',
            '0053411122',
            '0042361120',
            '5532241122',
            '1532247211',
            '1132230211',
        ]))
        consume(school, 4)
        self.assertEqual(school, sol)

    def test_example_part_1_after_5_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '4484144000',
            '2044144000',
            '2253333493',
            '1152333274',
            '1187303285',
            '1164633233',
            '1153472231',
            '6643352233',
            '2643358322',
            '2243341322',
        ]))
        consume(school, 5)
        self.assertEqual(school, sol)

    def test_example_part_1_after_6_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '5595255111',
            '3155255222',
            '3364444605',
            '2263444496',
            '2298414396',
            '2275744344',
            '2264583342',
            '7754463344',
            '3754469433',
            '3354452433',
        ]))
        consume(school, 6)
        self.assertEqual(school, sol)

    def test_example_part_1_after_20_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '3936556452',
            '5686556806',
            '4496555690',
            '4448655580',
            '4456865570',
            '5680086577',
            '7000009896',
            '0000000344',
            '6000000364',
            '4600009543',
        ]))
        consume(school, 20)
        self.assertEqual(school, sol)

    def test_example_part_1_after_50_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '9655556447',
            '4865556805',
            '4486555690',
            '4458655580',
            '4574865570',
            '5700086566',
            '6000009887',
            '8000000533',
            '6800000633',
            '5680000538',
        ]))
        consume(school, 50)
        self.assertEqual(school, sol)

    def test_example_part_1_after_100_days(self):
        with open('./test_input', 'r') as data:
            school = OctopusSchool(data)
        sol = OctopusSchool(iter([
            '0397666866',
            '0749766918',
            '0053976933',
            '0004297822',
            '0004229892',
            '0053222877',
            '0532222966',
            '9322228966',
            '7922286866',
            '6789998766',
        ]))
        consume(school, 100)
        self.assertEqual(school, sol)

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = count_flashes(data, 100)
        self.assertEqual(r, 1656)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = count_flashes(data, 100)
        self.assertEqual(r, 1697)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = first_step_synced(data)
        self.assertEqual(r, 195)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = first_step_synced(data)
        self.assertEqual(r, 344)


if __name__ == '__main__':
    unittest.main()
