import numpy as np
from copy import deepcopy
from typing import Callable

DAY = 11


modulo = 1
def run_round(worries: list[int], test: Callable, func: Callable, part: int = 1) -> list[tuple]:
    sent = []
    for worry in worries:
        new = func(worry)
        
        if part == 1:
            new = new // 3

        x = test(new)
        sent.append((x, new%modulo))

    return sent


def parse_input(inp: list[str]) -> tuple[dict, dict, dict]:
    items = {}
    funcs = {}
    tests = {}
    monkeys = op = divis = monkey1 = monkey0 = 0
    global modulo

    for line in inp:
        match line.split(':'):
            case ['Starting items', numbers]:
                items[monkeys] = [int(x) for x in numbers.split(", ")]
            
            case ['Operation', operation]:
                operation = operation.split()
                if operation[3] == '+':
                    if operation[4] == 'old':
                        op = lambda x: x + x
                    else: op = lambda x, y=int(operation[4]): x + y
                elif operation[3] == '*':
                    if operation[4] == 'old':
                        op = lambda x: x * x
                    else:
                        op = lambda x, y=int(operation[4]): x * y
                funcs[monkeys] = op
                
            case ['Test', divis]:
                divis = int(divis.split()[-1])
                modulo *= divis

            case ['If true', monkey1]:
                monkey1 = int(monkey1.split()[-1])
                
            case ['If false', monkey0]:
                monkey0 = int(monkey0.split()[-1])
                tests[monkeys] = (lambda x, m1=monkey1, d=divis, m0=monkey0: m1 if x%d == 0 else m0)
                monkeys += 1
            
            case _:
                pass
    
    return items, funcs, tests


def part1(inp: list[str]) -> int:
    items, funcs, tests = parse_input(inp)
    monkeys = len(items)

    inspected = {}
    for i in range(monkeys):
        inspected[i] = 0

    for _ in range(20):
        new_items = {}
        for i in range(monkeys):
            new_items[i] = []
        
        for i in range(monkeys):
            lst_y = run_round(items[i], tests[i], funcs[i])
            inspected[i] += len(items[i])

            for y in lst_y:
                if i < y[0]:
                    items[y[0]].append(y[1])
                else: new_items[y[0]].append(y[1])

        items = new_items

    lst = sorted(inspected.values())
    return lst[-1]*lst[-2]


def part2(inp: list[str]) -> int:
    items, funcs, tests = parse_input(inp)
    monkeys = len(items)

    inspected = {}
    for i in range(monkeys):
        inspected[i] = 0

    for _ in range(10000):
        new_items = {}
        for i in range(monkeys):
            new_items[i] = []
        
        for i in range(monkeys):
            lst_y = run_round(items[i], tests[i], funcs[i], 2)
            inspected[i] += len(items[i])

            for y in lst_y:
                if i < y[0]:
                    items[y[0]].append(y[1])
                else: new_items[y[0]].append(y[1])

        items = new_items

    lst = sorted(inspected.values())
    return lst[-1]*lst[-2]


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
