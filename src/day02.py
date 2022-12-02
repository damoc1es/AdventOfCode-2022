import numpy as np
from copy import deepcopy

DAY = 2


def part1(inp: str) -> int:
    loss, draw, won = 0, 3, 6
    d_xyz = {'X': 1, 'Y': 2, 'Z': 3}
    d_abc = { # rock paper scissors
        'A': {'X': draw, 'Y': won, 'Z': loss},
        'B': {'X': loss, 'Y': draw, 'Z': won},
        'C': {'X': won, 'Y': loss, 'Z': draw},
    }

    score = 0

    for line in inp:
        p1, p2 = line.split()
        score += d_abc[p1][p2] + d_xyz[p2]

    return score


def part2(inp: str) -> int:
    d_xyz = {'X': 0, 'Y': 3, 'Z': 6}
    d_abc = { # rock paper scissors
        'A': {'X': 3, 'Y': 1, 'Z': 2},
        'B': {'X': 1, 'Y': 2, 'Z': 3},
        'C': {'X': 2, 'Y': 3, 'Z': 1},
    }

    score = 0

    for line in inp:
        p1, p2 = line.split()
        score += d_abc[p1][p2] + d_xyz[p2]

    return score


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input0{DAY}.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
