import aoc2022.day01 as day01
import aoc2022.day02 as day02
import aoc2022.day03 as day03
import aoc2022.day04 as day04
import aoc2022.day05 as day05
import aoc2022.day06 as day06
import aoc2022.day07 as day07
import aoc2022.day08 as day08
import aoc2022.day09 as day09
import aoc2022.day10 as day10
import aoc2022.day11 as day11
import aoc2022.day12 as day12
import aoc2022.day13 as day13
import aoc2022.day14 as day14
import aoc2022.day15 as day15
import aoc2022.day16 as day16
import aoc2022.day17 as day17
import aoc2022.day18 as day18
import aoc2022.day19 as day19
import aoc2022.day20 as day20
import aoc2022.day21 as day21
import aoc2022.day22 as day22
import aoc2022.day23 as day23
import aoc2022.day24 as day24
import aoc2022.day25 as day25

from datetime import datetime

def read_input(day, module):
    with open(f"input/input{day}.txt") as file:
        read_input = getattr(module, "read_input", None)
        if read_input:
            return read_input(file).rstrip("\r\n")
        else:
            return [ line.rstrip("\n") for line in file.readlines()]
 
if __name__ == '__main__' :
    
    days = range(1,26)
    for day in days:
        module = locals()[f"day{day:02d}"]
        input = read_input(day,module)

        for i in [1,2]:
            fun = getattr(module, f"solve{i}")
            start = datetime.now()
            solution = fun(input)
            end = datetime.now()
            diff = (end - start).microseconds
            print(f"Day{day} Solution{i}: {solution}, execution time: {diff}µs")

