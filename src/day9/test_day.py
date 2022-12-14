import unittest
import day


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
    
        self.assertEqual( day.solve1(input), 0)
        self.assertEqual( day.solve2(input), 0)

if __name__ == '__main__':
    unittest.main()