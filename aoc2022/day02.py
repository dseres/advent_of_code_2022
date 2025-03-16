from enum import IntEnum

class RockPaperScissor(IntEnum):
    ROCK=1
    PAPER=2
    SCISSOR=3
    A=1
    B=2
    C=3
    X=1
    Y=2
    Z=3

def next_value(a):
    next_value = a + 1
    if next_value == 4:
        next_value = 1
    return next_value

def is_won(a,b):
    return next_value(a) == b

def is_draft(a,b):
    return a == b

def is_loosed(a,b):
    return not is_won(a,b) and not is_draft(a,b)

def read_input_lines():
    file = open("input/input2.txt")
    return file.readlines()

def parse_input(lines):
    guide = []
    for line in lines:
        values = line.strip().split(' ')
        value1 = RockPaperScissor[values[0]]
        value2 = RockPaperScissor[values[1]]
        guide.append([ value1, value2 ])
    return guide

def solve1(input):
    points2 = 0
    guide = parse_input(input)
    for party in guide:
        [a,b] =party
        if is_won(a, b):
            points2 += 6
        elif is_draft(a,b):
            points2 += 3
        points2 += b
    return points2

def solve2(input):
    points2 = 0
    guide = parse_input(input)
    for party in guide:
        [a,b] =party
        if b == RockPaperScissor.Z:
            points2 += 6 + next_value(a)
        elif b == RockPaperScissor.Y:
            points2 += 3 + a
        else:
            points2 += next_value(next_value(a))
    return points2

   
    
