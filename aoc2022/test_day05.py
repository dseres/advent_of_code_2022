import unittest
import aoc2022.day05 as day


class TestDay(unittest.TestCase):

    def test_day(self):
        input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()
        stacks = day.Stacks(input)

        self.assertEqual( stacks.stacks, [['Z','N'],['M','C','D'],['P']])
        self.assertEqual( stacks.instructions, [ day.Instruction(1,2,1), day.Instruction(3,1,3), day.Instruction(2,2,1), day.Instruction(1,1,2)])

        self.assertEqual( stacks.solve1(), 'CMZ')
        self.assertEqual( stacks.solve2(), 'MCD')

if __name__ == '__main__':
    unittest.main()