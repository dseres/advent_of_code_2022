import unittest
import aoc2022.day04 as day

class TestDay(unittest.TestCase):

    def test_contains(self):
        self.assertFalse(day.contains([3, 26, 25, 84]))

    def test_day(self):
        input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()
        self.assertEqual( day.solve1(input), 2)
        self.assertEqual( day.solve2(input), 4)

if __name__ == '__main__':
    unittest.main()