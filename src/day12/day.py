def parse(input):
    lines = input.strip().splitlines()
    start_pos = (0,0)
    end_pos = (0,0)
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == 'S':
                lines[i]=line.replace("S", "a")
                start_pos = (i,j)
            if c == 'E':
                lines[i]=line.replace("E", "z")
                end_pos = (i,j)
    return (lines,start_pos,end_pos)

def solve1(input):
    lines,start_pos,end_pos = parse(input)
    print(lines,start_pos,end_pos)
    return 0

def solve2(input):
    return 0

def read_input():
    with open("input/input12.txt") as file:
        return file.read()
