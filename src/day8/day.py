
class Forest:

    def __init__(self, input: str):
        self.trees = [[int(c) for c in line] for line in input.splitlines()]
        self.visibles = [[0 for _ in line] for line in self.trees]

    def check_direction(self, x, y, step_x, step_y):
        self.visibles[x][y] = 1
        max = self.trees[x][y]
        x += step_x
        y += step_y
        while True:
            if max < self.trees[x][y]:
                max = self.trees[x][y]
                self.visibles[x][y] = 1
            x += step_x
            y += step_y
            if x < 0 or x >= len(self.trees) or y < 0 or y >= len(self.trees[x]):
                break

    def count_visibles_from_outside(self):
        return sum([sum(line) for line in self.visibles])

    def solve1(self):
        for x in range(len(self.trees)):
            self.check_direction(x, 0, 0, 1)
            self.check_direction(x, len(self.trees[x])-1, 0, -1)
            for y in range(1, len(self.trees)-1):
                self.check_direction(0, y, 1, 0)
                self.check_direction(len(self.trees)-1, y, -1, 0)
        return self.count_visibles_from_outside()

    def count_visibles_to_direction(self, from_x, from_y, step_x, step_y):
        x = from_x
        y = from_y
        count = 0
        while True:
            x += step_x
            y += step_y
            if x < 0 or y < 0 or len(self.trees) <= x or len(self.trees[x]) <= y:
                break
            count += 1
            if self.trees[from_x][from_y] <= self.trees[x][y]:
                break
        return count

    def count_visibles(self,x,y):
        counts = [ self.count_visibles_to_direction(x,y,step_y, step_x) for (step_x, step_y) in [(1,0),(-1,0),(0,1),(0,-1)]]
        return counts[0] * counts[1] * counts[2] * counts[3]

    def solve2(self):
        max = 0
        for x in range(len(self.trees)):
            for y in range(len(self.trees[x])):
                count = self.count_visibles(x,y)
                if max < count:
                    max = count
        return max


def read_input():
    with open("input/input8.txt") as file:
        return file.read()
