import unittest
import aoc2022.day01 as day



class TestDay1(unittest.TestCase):

    def test_day1(self):
        test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()
        self.assertEqual( day.solve1(test_input), 24000)
        self.assertEqual( day.solve2(test_input), 45000)

if __name__ == '__main__':
    unittest.main()