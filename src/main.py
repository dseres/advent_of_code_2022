import day1.day1 as day1
import day2.day2 as day2
import day3.day as day3
import day4.day as day4

if __name__ == '__main__' :
    # input = day1.read_input_lines()
    # print('Solution for day1: {} and {}'.format(day1.solve1(input), day1.solve2(input)))
    # input = day2.read_input_lines()
    # print('Solution for day2: {} and {}'.format(day2.solve1(input), day2.solve2(input)))
    # input = day3.read_input_lines()
    # print('Solution for day3: {} and {}'.format( day3.solve1(input),  day3.solve2(input)))
    input = day4.parse_input(day4.read_input())
    print('Solution for day4: {} and {}'.format( day4.solve1(input),  day4.solve2(input)))
    pass
