import unittest
import day3 as day



class TestDay2(unittest.TestCase):

    def test_priority(self):
        self.assertEqual(day.get_priority('a'), 1)        
        self.assertEqual(day.get_priority('z'), 26)        
        self.assertEqual(day.get_priority('A'), 27)        
        self.assertEqual(day.get_priority('Z'), 52)        

    def test_split(self):
        self.assertEqual(day.split("vJrwpWtwJgWrhcsFMMfFFhFp"), ["vJrwpWtwJgWr","hcsFMMfFFhFp"])
        self.assertEqual(day.split("ab"), ["a","b"])
        self.assertEqual(day.split("abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"), ["abcdefghijklmnopqrstuvxyz","ABCDEFGHIJKLMNOPQRSTUVXYZ"])

    def test_day3(self):
        test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines(keepends=False)
        self.assertEqual( day.solve1(test_input), 157)
        self.assertEqual( day.solve2(test_input), 70)

if __name__ == '__main__':
    unittest.main()