import re
import inspect


class Monkey:
    monkey_re = re.compile("Monkey (\\d+):")
    items_re = re.compile("\\s*Starting items: (.*)")
    operation_re = re.compile("\\s*Operation: (.*)")
    test_re = re.compile("\\s*Test: divisible by (.*)")
    if_true_re = re.compile("\\s*If true: throw to monkey (.*)")
    if_false_re = re.compile("\\s*If false: throw to monkey (.*)")

    def __init__(self):
        self.id = 0
        self.items: [int] = []
        self.operation = lambda x: x
        self.divisor = 1
        self.monkey_true = 0
        self.monkey_false = 0
        self.counter = 0

    def parse(self, lines):
        m = self.monkey_re.match(lines[0])
        self.id = int(m.group(1))

        m = self.items_re.match(lines[1])
        self.items = [int(v) for v in m.group(1).split(', ')]

        m = self.operation_re.match(lines[2])
        match m.group(1).split():
            case ["new", "=", "old", "+", n]:
                self.operation = lambda x: x + int(n)
            case ["new", "=", "old", "*", "old"]:
                self.operation = lambda x: x * x
            case ["new", "=", "old", "*", n]:
                self.operation = lambda x: x * int(n)

        m = self.test_re.match(lines[3])
        self.divisor = int(m.group(1))

        m = self.if_true_re.match(lines[4])
        self.monkey_true = int(m.group(1))

        m = self.if_false_re.match(lines[5])
        self.monkey_false = int(m.group(1))

    def __str__(self):
        return "Monkey(id=%d, items=[%s], %s, divisor=%d, monkey_true=%d, monkey_false=%d, counter=%d" % (self.id, ", ".join([str(i) for i in self.items]), inspect.getsource(self.operation).strip(), self.divisor, self.monkey_true, self.monkey_false, self.counter)

    def take_turn(self):
        result = []
        for item in self.items:
            item = self.operation(item)
            item = item // 3
            if item % self.divisor == 0:
                result.append((self.monkey_true, item))
            else:
                result.append((self.monkey_false, item))
        self.counter += len(self.items)
        self.items = []
        return result


class Game:
    def __init__(self):
        self.monkeys: [Monkey] = []

    def parse(self, input: str):
        lines = input.splitlines()
        for i in range(0, len(lines), 7):
            m = Monkey()
            m.parse(lines[i:i+7])
            print(m)
            self.monkeys.append(m)

    def take_turn(self):
        for monkey in self.monkeys:
            passing = monkey.take_turn()
            for (m, item) in passing:
                self.monkeys[m].items.append(item)

    def solve1(self):
        for _ in range(20):
            self.take_turn()
        for m in self.monkeys:
            print(m)
        counters = [ m.counter for m in self.monkeys]
        counters.sort(reverse=True)
        return counters[0] * counters[1]

def solve1(input):
    game = Game()
    game.parse(input)
    return game.solve1()


def solve2(input):
    return 0


def read_input():

    with open("input/input11.txt") as file:
        return file.read()
