import unittest
import day


class TestDay(unittest.TestCase):

    def test_day(self):
        input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
        dirs = day.Dir.parse(input)

        self.assertEqual( dirs.solve1(), 0)
        self.assertEqual( dirs.solve2(), 0)

if __name__ == '__main__':
    unittest.main()