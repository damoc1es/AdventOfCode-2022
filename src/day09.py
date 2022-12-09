import numpy as np
from copy import deepcopy

DAY = 9


def manhattan(x: tuple[int, int], y: tuple[int, int]) -> int:
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def closer(H: tuple[int, int], T: tuple[int, int]) -> tuple[int, int]:
    adj = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for t in adj:
        if T[0]+t[0] == H[0] and T[1]+t[1] == H[1]:
            return T

    if H in [(T[0]-1, T[1]-2), (T[0]-2, T[1]-1)]:
        T = (T[0]-1, T[1]-1)
    elif H in [(T[0]+1, T[1]-2), (T[0]+2, T[1]-1)]:
        T = (T[0]+1, T[1]-1)
    elif H in [(T[0]+1, T[1]+2), (T[0]+2, T[1]+1)]:
        T = (T[0]+1, T[1]+1)
    elif H in [(T[0]-1, T[1]+2), (T[0]-2, T[1]+1)]:
        T = (T[0]-1, T[1]+1)
    elif H == (T[0]-2, T[1]):
        T = (T[0]-1, T[1])
    elif H == (T[0]+2, T[1]):
        T = (T[0]+1, T[1])
    elif H == (T[0], T[1]-2):
        T = (T[0], T[1]-1)
    elif H == (T[0], T[1]+2):
        T = (T[0], T[1]+1)

    if manhattan(H, T) >= 2:
        closest = ()
        dist = float('+inf')

        for t in adj:
            p = (T[0]+t[0], T[1]+t[1])

            if manhattan(p, H) <= dist:
                dist = manhattan(p, H)
                closest = p
        return closest

    return T


def part1(inp: list[str]) -> int:
    coord = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

    H = T = (0, 0)
    
    positions = set()
    positions.add(H)

    for line in inp:
        d, step = line.split()
        step = int(step)

        for _ in range(step):
            H = (H[0]+coord[d][0], H[1]+coord[d][1])
            T = closer(H, T)
            positions.add(T)
    
    return len(positions)


def part2(inp: list[str]) -> int:
    coord = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

    rope = [(0, 0) for _ in range(10)]
    
    positions = set()
    positions.add(rope[0])

    for line in inp:
        d, step = line.split()
        step = int(step)

        for _ in range(step):
            rope[0] = (rope[0][0]+coord[d][0], rope[0][1]+coord[d][1])
            
            for i in range(1, 10):
                rope[i] = closer(rope[i-1], rope[i])
            
            positions.add(rope[9])
    
    return len(positions)


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input0{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
