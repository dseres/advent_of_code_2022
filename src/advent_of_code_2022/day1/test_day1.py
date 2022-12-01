import unittest
import day1



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

10000""".splitlines(keepends=True)
        self.assertEqual( day1.solve1(test_input), 24000)
        self.assertEqual( day1.solve2(test_input), 45000)

if __name__ == '__main__':
    unittest.main()