import re


def parse_input(lines):
    return [ [ int(v) for v in re.split('[,-]', line)] for line in lines if len(line) > 0]


def contains(r):
    return r[0] <= r[2] and r[3] <= r[1] or r[2] <= r[0] and r[1] <= r[3]


def overlaps(r):
    return r[2] <= r[0] <= r[3] or r[2] <= r[1] <= r[3] or r[0] <= r[2] <= r[1] or r[0] <= r[3] <= r[1]


def solve1(input):
    ranges = parse_input(input)
    return len([r for r in ranges if contains(r)])


def solve2(input):
    ranges = parse_input(input)
    return len([r for r in ranges if overlaps(r)])
