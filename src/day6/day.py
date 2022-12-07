def read_input():
    file = open("input/input6.txt")
    return file.read()

def solve1(input):
    return find_signal(input,4)

def solve2(input):
    return find_signal(input,14)

def find_signal(input, size):
    for i in range(0,len(input)-size):
        part = input[i:i+size]
        if not has_equal_chars(part):
            return i + size 
    return -1

def has_equal_chars(part:str) -> bool:
    for j in range(len(part)):
        for k in range(len(part)):
            if j!=k and part[j] == part[k]:
                return True
    return False
