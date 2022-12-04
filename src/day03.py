import numpy as np
from copy import deepcopy

DAY = 3


def part1(inp: str) -> int:
    common = []

    for line in inp:
        l1 = line[:len(line)//2]
        l2 = line[len(line)//2:]
        
        for c in l1:
            if c in l2:
                common.append(c)
                break

    s = 0
    for c in common:
        if c.islower():
            s += (ord(c)-ord('a')+1)

        if c.isupper():
            s += (ord(c)-ord('A')+27)

    return s


def part2(inp: str) -> int:
    common = []

    for i in range(0, len(inp), 3):
        l1 = inp[i]
        l2 = inp[i+1]
        l3 = inp[i+2]
        
        for c in l1:
            if c in l2 and c in l3:
                common.append(c)
                break

    s = 0
    for c in common:
        if c.islower():
            s += (ord(c)-ord('a')+1)

        if c.isupper():
            s += (ord(c)-ord('A')+27)

    return s


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input0{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
