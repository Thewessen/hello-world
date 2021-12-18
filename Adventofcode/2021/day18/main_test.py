import unittest
from main import SnailfishNumber, final_sum, addition_homework, largest_sum


class MainTest(unittest.TestCase):
    def test_parse_str_to_snailfishnumber_0_nested(self):
        from_str = SnailfishNumber.from_str('[2,3]')
        self.assertEqual(from_str, SnailfishNumber((2, 3))) 

    def test_parse_str_to_snailfishnumber_1_nested_1(self):
        from_str = SnailfishNumber.from_str('[[1,2],3]')
        part_parsed = SnailfishNumber((SnailfishNumber.from_str('[1,2]'), 3)) 
        self.assertEqual(from_str, part_parsed)

    def test_parse_str_to_snailfishnumber_1_nested_2(self):
        from_str = SnailfishNumber.from_str('[[1,2],[3,4]]')
        part_parsed = SnailfishNumber((SnailfishNumber.from_str('[1,2]'),
                                       SnailfishNumber.from_str('[3,4]'))) 
        self.assertEqual(from_str, part_parsed)

    def test_parse_str_to_snailfishnumber_adv(self):
        from_str = SnailfishNumber.from_str('[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]')
        a1 = SnailfishNumber((3, 8))
        a2 = SnailfishNumber((0, 9))
        a3 = SnailfishNumber((3, 7))
        a4 = SnailfishNumber((4, 9))
        b1 = SnailfishNumber((9, a1))
        b2 = SnailfishNumber((a2, 6))
        b3 = SnailfishNumber((a3, a4))
        c1 = SnailfishNumber((b1, b2))
        c2 = SnailfishNumber((b3, 3))
        parsed = SnailfishNumber((c1, c2))
        self.assertEqual(from_str, parsed)

    def test_explode_example_1(self):
        n = SnailfishNumber.from_str('[[[[[9,8],1],2],3],4]')
        r = SnailfishNumber.from_str('[[[[0,9],2],3],4]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_explode_example_2(self):
        n = SnailfishNumber.from_str('[7,[6,[5,[4,[3,2]]]]]')
        r = SnailfishNumber.from_str('[7,[6,[5,[7,0]]]]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_explode_example_3(self):
        n = SnailfishNumber.from_str('[[6,[5,[4,[3,2]]]],1]')
        r = SnailfishNumber.from_str('[[6,[5,[7,0]]],3]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_explode_example_4(self):
        n = SnailfishNumber.from_str('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
        r = SnailfishNumber.from_str('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_explode_example_5(self):
        n = SnailfishNumber.from_str('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
        r = SnailfishNumber.from_str('[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_explode_fails_example(self):
        n = SnailfishNumber.from_str('[[3,[2,[0,0]]],[9,[5,[0,[0,2]]]]]')
        r = SnailfishNumber.from_str('[[3,[2,[0,0]]],[9,[5,[0,0]]]]')
        self.assertIsNotNone(n.explode())
        self.assertEqual(n, r)

    def test_split_different(self):
        n = SnailfishNumber.from_str('[11,3]')
        r = SnailfishNumber.from_str('[[5,6],3]')
        self.assertTrue(n.split())
        self.assertEqual(n, r)

    def test_split_same(self):
        n = SnailfishNumber.from_str('[5,12]')
        r = SnailfishNumber.from_str('[5,[6,6]]')
        self.assertTrue(n.split())
        self.assertEqual(n, r)

    def test_reduce(self):
        n = SnailfishNumber.from_str('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
        r = SnailfishNumber.from_str('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(n.reduce(), r)

    def test_final_sum_example_1(self):
        n = final_sum(iter([
            '[1,1]',
            '[2,2]',
            '[3,3]',
            '[4,4]',
        ]))
        r = SnailfishNumber.from_str('[[[[1,1],[2,2]],[3,3]],[4,4]]')
        self.assertEqual(n, r)

    def test_final_sum_example_2(self):
        n = final_sum(iter([
            '[1,1]',
            '[2,2]',
            '[3,3]',
            '[4,4]',
            '[5,5]',
        ]))
        r = SnailfishNumber.from_str('[[[[3,0],[5,3]],[4,4]],[5,5]]')
        self.assertEqual(n, r)

    def test_final_sum_example_3(self):
        n = final_sum(iter([
            '[1,1]',
            '[2,2]',
            '[3,3]',
            '[4,4]',
            '[5,5]',
            '[6,6]',
        ]))
        r = SnailfishNumber.from_str('[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(n, r)

    def test_final_sum_example_large(self):
        a = SnailfishNumber.from_str('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
        b = SnailfishNumber.from_str('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[7,[5,[[3,8],[1,4]]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[[2,[2,2]],[8,[8,1]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[2,9]')
        a += b
        r = SnailfishNumber.from_str('[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[1,[[[9,3],9],[[9,0],[0,7]]]]')
        a += b
        r = SnailfishNumber.from_str('[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[[[5,[7,4]],7],1]')
        a += b
        r = SnailfishNumber.from_str('[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]')
        self.assertEqual(a.reduce(), r)
        b = SnailfishNumber.from_str('[[[[4,2],2],6],[8,7]]')
        a += b
        r = SnailfishNumber.from_str('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
        self.assertEqual(a.reduce(), r)

    def test_failing_split_bug(self):
        n = SnailfishNumber.from_str('[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,10],20],[8,[9,0]]]]')
        r = SnailfishNumber.from_str('[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,[5,5]],20],[8,[9,0]]]]')
        # r = SnailfishNumber.from_str('[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,10],[10,10]],[8,[9,0]]]]')
        self.assertTrue(n.split())
        self.assertEqual(n, r)

    def test_failing_addition_bug(self):
        a = SnailfishNumber.from_str('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]')
        b = SnailfishNumber.from_str('[7,[5,[[3,8],[1,4]]]]')
        r = SnailfishNumber.from_str('[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]')
        self.assertEqual((a + b).reduce(), r)

    def test_magnitude_example_1(self):
        n = SnailfishNumber.from_str('[[1,2],[[3,4],5]]')
        self.assertEqual(n.magnitude, 143)

    def test_magnitude_example_2(self):
        n = SnailfishNumber.from_str('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(n.magnitude, 1384)

    def test_magnitude_example_3(self):
        n = SnailfishNumber.from_str('[[[[1,1],[2,2]],[3,3]],[4,4]]')
        self.assertEqual(n.magnitude, 445)

    def test_magnitude_example_4(self):
        n = SnailfishNumber.from_str('[[[[3,0],[5,3]],[4,4]],[5,5]]')
        self.assertEqual(n.magnitude, 791)

    def test_magnitude_example_5(self):
        n = SnailfishNumber.from_str('[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(n.magnitude, 1137)

    def test_magnitude_example_6(self):
        n = SnailfishNumber.from_str('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
        self.assertEqual(n.magnitude, 3488)

    def test_example_solution_part_1(self):
        with open('./test_input', 'r') as data:
            r = addition_homework(data)
        self.assertEqual(r, 4140)

    def test_solution_part_1(self):
        with open('./input', 'r') as data:
            r = addition_homework(data)
        self.assertEqual(r, 4480)

    def test_example_solution_part_2(self):
        with open('./test_input', 'r') as data:
            r = largest_sum(data)
        self.assertEqual(r, 3993)

    def test_solution_part_2(self):
        with open('./input', 'r') as data:
            r = largest_sum(data)
        self.assertEqual(r, 4676)


if __name__ == '__main__':
    unittest.main()
