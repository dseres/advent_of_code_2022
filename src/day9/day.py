class Fiber:
    def __init__(self, size):
        self.parts : [(int,int)] = [(0, 0) for i in range(size) ]
        self.visited: set((int, int)) = set()

    def process_moves(self, input: str):
        for line in [ line.strip() for line in input.splitlines()]:
            self.move(line)

    def move(self, instruction: str):
        match instruction.split():
            case ["U", count]:
                self.move_to_direction((1, 0), int(count))
            case ["D", count]:
                self.move_to_direction((-1, 0), int(count))
            case ["L", count]:
                self.move_to_direction((0, -1), int(count))
            case ["R", count]:
                self.move_to_direction((0, 1), int(count))

    def move_to_direction(self, direction : (int,int), count : int):
        #print(direction, count)
        for i in range(count):
            self.step_to_direction(direction)
        print(self.parts)
    
    def step_to_direction(self, direction : (int,int)):
        self.parts[0] = (self.parts[0][0] + direction[0], self.parts[0][1] + direction[1])
        for i in range(len(self.parts)-1):
            self.step_tails_to_direction(i, direction)
            # save last part position
        self.visited.add(self.parts[len(self.parts)-1])

    def step_tails_to_direction(self, index : int, direction : (int,int)):
        if (abs(self.parts[index][0] - self.parts[index+1][0]) > 1):
            dist_y = self.sign(self.parts[index][1] - self.parts[index+1][1])
            self.parts[index + 1] = ( self.parts[index + 1][0] + direction[0], self.parts[index + 1][1] + dist_y)
        elif (abs(self.parts[index][1] - self.parts[index+1][1]) > 1):
            dist_x = self.sign(self.parts[index][0] - self.parts[index+1][0])
            self.parts[index + 1] = ( self.parts[index + 1][0] + dist_x, self.parts[index + 1][1] + direction[1])

    def sign(self, v):
        if v < 0:
            return -1
        if v > 0:
            return 1
        return 0

def solve1(input):
    fiber = Fiber(2)
    fiber.process_moves(input)
    return len(fiber.visited)


def solve2(input):
    fiber = Fiber(10)
    fiber.process_moves(input)
    return len(fiber.visited)


def read_input():
    with open("input/input9.txt") as file:
        return file.read()
