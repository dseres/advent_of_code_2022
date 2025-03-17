class Cpu:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.x_of_cycle = [1]

    def process_instructions(self, input:str):
        for line in input.splitlines():
            self.process_instruction(line.strip())
            
    def process_instruction(self, instr: str):
        match instr.split():
            case ['noop']:
                self.x_of_cycle.append(self.x)
            case ['addx', param]:
                self.x_of_cycle.append(self.x)
                self.x += int(param)
                self.x_of_cycle.append(self.x)
        #print(len(self.x_of_cycle), instr, self.x, self.x_of_cycle)

    def render(self):
        pic = ""
        for line in range(6):
            for pos in range(40):
                cycle = line * 40 + pos
                x_during_cycle = self.x_of_cycle[cycle]
                if x_during_cycle - 1 <= pos <= x_during_cycle + 1:
                    pic += "#"
                else:
                    pic += "."
            pic += "\n"
        return pic.strip()
        
def solve1(input):
    cpu = Cpu()
    cpu.process_instructions(input)
    return sum( [ cpu.x_of_cycle[i-1]*i for i in [20, 60, 100, 140, 180, 220] ] )

def solve2(input):
    cpu = Cpu()
    cpu.process_instructions(input)
    return "\n" + cpu.render()

def read_input(file):
    return file.read()
