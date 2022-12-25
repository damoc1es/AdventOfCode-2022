import numpy as np
from copy import deepcopy

DAY = 25


def snafu_to_decimal(snafu: str) -> int:
    mods = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    nr = 0
    d = 1

    for c in reversed(snafu):
        nr += mods[c] * d
        d *= 5
    
    return nr


def decimal_to_snafu(nr: int) -> str:
    mods = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
    snafu = ""

    while nr > 0:
        m = nr % 5
        nr //= 5
        snafu += mods[m]

        if m > 2:
            nr += 1

    return snafu[::-1]


def part1(inp: list[str]):
    numbers = []
    for number in inp:
        numbers.append(snafu_to_decimal(number))
    
    return decimal_to_snafu(sum(numbers))


def part2(inp: list[str]):
    return None


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
