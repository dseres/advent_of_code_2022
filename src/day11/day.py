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

    def parse(self,lines):
        m = self.monkey_re.match(lines[0])
        self.id = int(m.group(1))

        m = self.items_re.match(lines[1])
        self.items = [int(v) for v in m.group(1).split(', ')]

        m = self.operation_re.match(lines[2])
        print(m.group(1).split())
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
        return "Monkey(id=%d, items=%s, %s, divisor=%d, monkey_true=%d, monkey_false=%d" % (self.id, ", ".join([str(i) for i in self.items]), inspect.getsource(self.operation).strip(), self.divisor, self.monkey_true, self.monkey_false)


def solve1(input):
    lines = input.splitlines()
    for i in range(0,len(lines),7):
        m = Monkey()
        m.parse(lines[i:i+7])
        print(m)
    return 0


def solve2(input):
    return 0


def read_input():

    with open("input/input11.txt") as file:
        return file.read()
