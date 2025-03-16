class Fiber:
    def __init__(self, size):
        self.parts: [(int, int)] = [(0, 0) for i in range(size)]
        self.visited: set((int, int)) = set()

    def process_moves(self, input: str):
        for line in [line.strip() for line in input.splitlines()]:
            self.move(line)

    def move(self, instruction: str):
        match instruction.split():
            case ["U", count]:
                self.move_to_direction((0, 1), int(count))
            case ["D", count]:
                self.move_to_direction((0, -1), int(count))
            case ["L", count]:
                self.move_to_direction((-1, 0), int(count))
            case ["R", count]:
                self.move_to_direction((1, 0), int(count))

    def move_to_direction(self, direction: (int, int), count: int):
        for i in range(count):
            self.step_to_direction(direction)

    def step_to_direction(self, direction: (int, int)):
        head = self.parts[0]
        self.parts[0] = (head[0] + direction[0],
                         head[1] + direction[1])
        for i in range(len(self.parts)-1):
            self.step_part_to_direction(i, direction)
            # save last part position
        self.visited.add(self.parts[len(self.parts)-1])

    def step_part_to_direction(self, index: int, direction: (int, int)):
        prev = self.parts[index]
        current = self.parts[index+1]
        if (abs(prev[0] - current[0]) > 1 or abs(prev[1] - current[1]) > 1):
            dist_x = self.sign(prev[0] - current[0])
            dist_y = self.sign(prev[1] - current[1])
            self.parts[index+1] = (current[0] + dist_x, current[1] + dist_y)

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
