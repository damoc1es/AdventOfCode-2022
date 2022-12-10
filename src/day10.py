import numpy as np
from copy import deepcopy

DAY = 10


def part1(inp: list[str]) -> int:
    s = cycle = i = 0
    X = 1
    in_exec = None
    
    while i < len(inp) or in_exec:
        cycle += 1

        if i < len(inp) and not in_exec:
            line = inp[i]
            if line != 'noop':
                _, V = line.split()
                V = int(V)
                in_exec = (V, cycle+1)
            i += 1
        
        if cycle in (20, 60, 100, 140, 180, 220):
            s += X*cycle

        if in_exec:
            if in_exec[1] == cycle:
                X += in_exec[0]
                in_exec = None

    return s


def part2(inp: list[str]) -> str:
    cycle = i = 0
    X = 1
    in_exec = None
    sprite = ""
    output = []

    while i < len(inp) or in_exec:
        cycle += 1
        
        if i < len(inp) and not in_exec:
            line = inp[i]
            if line != 'noop':
                _, V = line.split()
                V = int(V)
                in_exec = (V, cycle+1)
            i += 1
        
        if X-1 <= len(sprite) <= X+1:
            sprite += '⬜'
        else: sprite += '⬛'

        if len(sprite) == 40:
            output.append(sprite)
            sprite = ""

        if in_exec:
            if in_exec[1] == cycle:
                X += in_exec[0]
                in_exec = None

    return str(np.array(output))


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: \n{part2(input_str)}")
