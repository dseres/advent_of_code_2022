import unittest
import aoc2022.day12 as day



class TestDay(unittest.TestCase):

    def test_day(self):
        input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
    
        self.assertEqual( day.solve1(input), 0)
        self.assertEqual( day.solve2(input), 0)

if __name__ == '__main__':
    unittest.main()