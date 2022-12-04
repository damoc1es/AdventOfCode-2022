import numpy as np
from copy import deepcopy

DAY = 4


def part1(inp: str) -> int:
    k = 0

    for line in inp:
        x, y = line.split(',')
        a, b = [int(t) for t in x.split('-')]
        c, d = [int(t) for t in y.split('-')]

        if a <= c and d <= b:
            k += 1
        elif c <= a and b <= d:
            k += 1

    return k


def part2(inp: str) -> int:
    k = 0

    for line in inp:
        x, y = line.split(',')
        a, b = [int(t) for t in x.split('-')]
        c, d = [int(t) for t in y.split('-')]

        if c <= a <= d or c <= b <= d:
            k += 1
        elif a <= c <= b or a <= d <= b:
            k += 1

    return k


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input0{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
