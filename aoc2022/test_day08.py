import unittest
import aoc2022.day08 as day


class TestDay(unittest.TestCase):

    def test_day(self):
        input = """30373
25512
65332
33549
35390"""
        forest = day.Forest(input)

        self.assertEqual( forest.solve1(), 21)
        self.assertEqual( forest.count_visibles(1,2), 4)
        self.assertEqual( forest.count_visibles(3,2), 8)

if __name__ == '__main__':
    unittest.main()