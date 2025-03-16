import re
import inspect


class Monkey:
    primes = [2,3,5,7,11,13,17,19]
    modulo_factor = 1

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

        self.parse_operation(lines[2])

        m = self.test_re.match(lines[3])
        self.divisor = int(m.group(1))

        m = self.if_true_re.match(lines[4])
        self.monkey_true = int(m.group(1))

        m = self.if_false_re.match(lines[5])
        self.monkey_false = int(m.group(1))

    def parse_operation(self, line):
        m = self.operation_re.match(line)
        match m.group(1).split():
            case ["new", "=", "old", "+", n]:
                self.operation = lambda x: x + int(n)
            case ["new", "=", "old", "*", "old"]:
                self.operation = lambda x: x * x
            case ["new", "=", "old", "*", n]:
                self.operation = lambda x: x * int(n)        

    def __str__(self):
        return "Monkey(id=%d, items=[%s], %s, divisor=%d, monkey_true=%d, monkey_false=%d, counter=%d" % (self.id, ", ".join([str(i) for i in self.items]), inspect.getsource(self.operation).strip(), self.divisor, self.monkey_true, self.monkey_false, self.counter)

    def take_turn(self, divide_by_3 ):
        result = [ self.compute_item(item, divide_by_3) for item in self.items]
        self.counter += len(self.items)
        self.items = []
        return result

    def compute_item(self, item, divide_by_3):
        item = self.operation(item)
        if divide_by_3:
            item = item // 3
        item = item % self.modulo_factor
        if item % self.divisor == 0:
            return (self.monkey_true, item)
        else:
            return (self.monkey_false, item)

class Game:
    def __init__(self):
        self.monkeys: [Monkey] = []

    def parse(self, input: str):
        lines = input.splitlines()
        for i in range(0, len(lines), 7):
            m = Monkey()
            m.parse(lines[i:i+7])
            self.monkeys.append(m)
        self.compute_modulo()
        

    def take_turn(self, divide_by_3=True):
        for monkey in self.monkeys:
            passing = monkey.take_turn(divide_by_3)
            for (m, item) in passing:
                self.monkeys[m].items.append(item)

    def compute_modulo(self):
        Monkey.modulo_factor = 1
        for m in self.monkeys:
            Monkey.modulo_factor *= m.divisor
        
    def solve1(self):
        for _ in range(20):
            self.take_turn()
        counters = [m.counter for m in self.monkeys]
        counters.sort(reverse=True)
        return counters[0] * counters[1]

    def solve2(self):
        for i in range(10000):
            self.take_turn(divide_by_3=False)
        counters = [m.counter for m in self.monkeys]
        counters.sort(reverse=True)
        return counters[0] * counters[1]


def solve1(input):
    game = Game()
    game.parse(input)
    return game.solve1()


def solve2(input):
    game = Game()
    game.parse(input)
    return game.solve2()


def read_input():

    with open("input/input11.txt") as file:
        return file.read()
