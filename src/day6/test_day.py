import unittest
import day


class TestDay(unittest.TestCase):


    def test_day(self):
        self.assertEqual( day.solve1('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 7)
        self.assertEqual( day.solve1('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
        self.assertEqual( day.solve1('nppdvjthqldpwncqszvftbrmjlhg'), 6)
        self.assertEqual( day.solve1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
        self.assertEqual( day.solve1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)

        self.assertEqual( day.solve2('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 0)

if __name__ == '__main__':
    unittest.main()