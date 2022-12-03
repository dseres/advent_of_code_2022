def read_input_lines():
    file = open("input/input3.txt")
    return map(lambda line: line.strip(), file.readlines())


def get_priority(c):
    if ord('a') <= ord(c) <= ord('z'):
        return 1 + ord(c) - ord('a')
    elif ord('A') <= ord(c) <= ord('Z'):
        return 27 + ord(c) - ord('A')

def split(str):
    size = len(str)
    assert ( size % 2 == 0)
    part1 = str[0:size//2]
    part2 = str[size//2:size]
    return [part1,part2]

def get_priority_for_line(str):
    [part1 ,part2] = split(str)
    assert (len(part1) == len(part2))
    for c1 in part1:
        for c2 in part2:
            if c1 == c2:
                return get_priority(c1)

def solve1(lines):
    return sum( map( lambda line: get_priority_for_line(line), lines))

def solve2(input):
    return 0
