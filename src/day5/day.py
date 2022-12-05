import re

class Instruction:
    def __init__(self, count:int, stack_from:int, stack_to:int):
        self.count : int = count
        self.stack_from : int = stack_from
        self.stack_to : int = stack_to
    def __repr__(self):
        return "'move %d from %d to %d'" % (self.count, self.stack_from, self.stack_to)
    def __str__(self):
        return "'move %d from %d to %d'" % (self.count, self.stack_from, self.stack_to)
    def __eq__(self, other):
        return self.count == other.count and self.stack_from == other.stack_from and self.stack_to == other.stack_to

class Stacks:

    def __init__(self, input:str):
        self.stacks = False
        self.instructions = []
        self.parse_input(input)

    def parse_input(self,input:str):
        stack_pattern = re.compile('^(\\[[A-Z]\\]|   )( (\\[[A-Z]\\]|   ))*$')
        instruction_pattern = re.compile('^move (\\d) from (\\d) to (\\d)$')
        for line in input.splitlines():
            if len(line)>0:
                if stack_pattern.match(line):
                    self.add_stack_values(line)
                else: 
                    match = instruction_pattern.findall(line)
                    if match:
                        self.instructions.append( Instruction(*[int(v) for v in match[0]]))
            
    def add_stack_values(self,line:str):
        groups = [ line[i:i+3].strip() for i in range(0,len(line),4)]
        if not self.stacks:
            self.stacks = [ [] for i in range(len(groups))]
        for i,v in enumerate(groups):
            if len(v)==3:
                self.stacks[i].insert(0,v[1])

def read_input():
    file = open("input/input5.txt")
    return file.read()

def solve1(ranges):
    return 0


def solve2(ranges):
    return 0
