import unittest
import aoc2022.day09 as day

class TestDay(unittest.TestCase):

    def test_day(self):
        input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    
        self.assertEqual( day.solve1(input), 13)

        input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
        self.assertEqual( day.solve2(input2), 36)

if __name__ == '__main__':
    unittest.main()