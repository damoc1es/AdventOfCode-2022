import numpy as np
from copy import deepcopy
from functools import cmp_to_key
import json

DAY = 13


def compare_lists(l1: list, l2: list) -> int:
    equal = True
    for i in range(min(len(l1), len(l2))):
        equal = False

        if l1[i] == l2[i]:
            continue

        if type(l1[i]) == int and type(l2[i]) == int:
            if l1[i] < l2[i]:
                return 1
            return -1

        x, y = l1[i], l2[i]
        
        if type(x) == int:
            x = [x]
        elif type(y) == int:
            y = [y]

        if compare_lists(x, y) == 0:
            equal = True
            continue
        return compare_lists(x, y)

    if len(l1) > len(l2):
        return -1
    if equal:
        return 1
    return 0


def part1(inp: list[str]) -> int:
    s = 0
    for i in range(0,len(inp),3):
        list1 = json.loads(inp[i])
        list2 = json.loads(inp[i+1])
        
        if compare_lists(list1, list2) != -1:
            s += (i//3+1)
    
    return s


def part2(inp: list[str]) -> int:
    packets = [[[2]], [[6]]]

    for line in inp:
        if line != "":
            packets.append(json.loads(line))
    
    packets.sort(key=cmp_to_key(compare_lists), reverse=True)

    p = 1
    for i, d in enumerate(packets):
        if d == [[2]] or d == [[6]]:
            p *= (i+1)
    
    return p


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")
    
    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
