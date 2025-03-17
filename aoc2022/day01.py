class Elf:
    def __init__(self, items) -> None:
        self.calories = sum(items)

def parse_input(lines):
    items = []
    elfs = []
    for line in lines:
        if line == '':
            e = Elf(items)
            elfs.append(e)
            items = []
        else:
            items.append(int(line))
    if len(items)> 0:
        e = Elf(items)
        elfs.append(e)       
    return elfs

def solve1(input):
    elfs = parse_input(input)
    elfs.sort( key= lambda elf: elf.calories, reverse = True )
    return elfs[0].calories

def solve2(input):
    elfs = parse_input(input)
    elfs.sort( key= lambda elf: elf.calories, reverse = True )
    return elfs[0].calories + elfs[1].calories + elfs[2].calories
   
    
