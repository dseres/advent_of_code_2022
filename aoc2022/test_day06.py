import unittest
import aoc2022.day06 as day



class TestDay(unittest.TestCase):


    def test_day(self):
        self.assertEqual( day.solve1('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 7)
        self.assertEqual( day.solve1('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
        self.assertEqual( day.solve1('nppdvjthqldpwncqszvftbrmjlhg'), 6)
        self.assertEqual( day.solve1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
        self.assertEqual( day.solve1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)

        self.assertEqual( day.solve2('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 19)
        self.assertEqual( day.solve2('bvwbjplbgvbhsrlpgdmjqwftvncz'), 23)
        self.assertEqual( day.solve2('nppdvjthqldpwncqszvftbrmjlhg'), 23)
        self.assertEqual( day.solve2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 29)
        self.assertEqual( day.solve2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 26)

if __name__ == '__main__':
    unittest.main()