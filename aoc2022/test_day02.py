import unittest
import aoc2022.day02 as day



class TestDay2(unittest.TestCase):

    def test_day1(self):
        test_input = """A Y
B X
C Z""".splitlines(keepends=False)
        self.assertEqual( day.solve1(test_input), 15)
        self.assertEqual( day.solve2(test_input), 12)

if __name__ == '__main__':
    unittest.main()