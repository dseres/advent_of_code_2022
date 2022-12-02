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

def is_won(a,b):
    next_value = a + 1
    if next_value == 4:
        next_value = 1
    return next_value == b

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
    points1 = 0
    points2 = 0
    guide = parse_input(input)
    #print(guide)
    for party in guide:
        [a,b] =party
        #print(party)
        if is_won(a, b):
            points2 += 6
            #print(6)
        elif is_draft(a,b):
            points1 += 3
            points2 += 3
            #print(3)
        else:
            points1 += 6
            #print(0)
        points1 += a
        points2 += b
        #print(int(b))
    return points2

def solve2(input):
    return 0
   
    
