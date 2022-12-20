import numpy as np
from copy import deepcopy
from collections import deque

DAY = 20


def mix(initial: list[tuple], times: int) -> list:
    dq = deque(initial)
    
    for _ in range(times):
        for c in initial:
            i = dq.index(c)
            dq.remove(c)
            dq.rotate(-c[1])
            dq.insert(i, c)
    
    return [c[1] for c in dq]


def part1(inp: list[str]) -> int:
    initial = list(enumerate([int(t) for t in inp]))

    encrypted = mix(initial, 1)
    
    index0 = encrypted.index(0)
    grove_coords = [index0+1000, index0+2000, index0+3000]

    return sum([encrypted[coord % len(initial)] for coord in grove_coords])


def part2(inp: list[str]) -> int:
    decryption_key = 811589153
    initial = list(enumerate([int(t) * decryption_key for t in inp]))
    
    encrypted = mix(initial, 10)
    
    index0 = encrypted.index(0)
    grove_coords = [index0+1000, index0+2000, index0+3000]

    return sum([encrypted[coord % len(initial)] for coord in grove_coords])


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
