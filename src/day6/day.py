import re


def read_input():
    file = open("input/input6.txt")
    return file.read()

def solve1(input):
    for i in range(0,len(input)-4):
        part = input[i:i+4]
        equals = False
        for j in range(len(part)):
            for k in range(len(part)):
                if j!=k and part[j] == part[k]:
                    equals = True
        if not equals:
            return i + 4 
    return -1


def solve2(input):
    return 0
