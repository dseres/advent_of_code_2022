import re


def read_input():
    file = open("input/input4.txt")
    return file.read()


def parse_input(input):
    return [[int(v) for v in re.split('[,-]', line)] for line in input.splitlines() if len(line) > 0]


def contains(r):
    return r[0] <= r[2] and r[3] <= r[1] or r[2] <= r[0] and r[1] <= r[3]


def overlaps(r):
    return r[2] <= r[0] <= r[3] or r[2] <= r[1] <= r[3] or r[0] <= r[2] <= r[1] or r[0] <= r[3] <= r[1]


def solve1(ranges):
    return len([r for r in ranges if contains(r)])


def solve2(ranges):
    return len([r for r in ranges if overlaps(r)])
