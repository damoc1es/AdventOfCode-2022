import numpy as np
from copy import deepcopy

DAY = 18


def neighbors(x: int, y: int, z: int) -> list[tuple]:
    return [(x-1, y, z), (x, y-1, z), (x, y, z-1),
            (x+1, y, z), (x, y+1, z), (x, y, z+1)]


def part1(inp: list[str]) -> int:
    cubes = set()
    for line in inp:
        cubes.add(tuple(int(t) for t in line.split(',')))

    connected = [0 for _ in range(len(cubes))]

    for i, (x, y, z) in enumerate(cubes):
        for cube2 in neighbors(x, y, z):
            if cube2 in cubes:
                connected[i] += 1

    return sum([6-connected[i] for i in range(len(connected))])


def part2(inp: list[str]) -> int:
    cubes = set()
    coords = set()

    for line in inp:
        p = tuple(int(t) for t in line.split(','))
        cubes.add(p)
        coords |= {p[0], p[1], p[2]}

    dim = (min(coords)-1, max(coords)+2)
    flood = [[[0 for _ in range(dim[0], dim[1]+1)] for _ in range(dim[0], dim[1]+1)] for _ in range(dim[0], dim[1]+1)]
    
    def M(i: int, j: int, k: int) -> int:
        return flood[i-dim[0]][j-dim[0]][k-dim[0]]

    def setM(i: int, j: int, k: int) -> None:
        flood[i-dim[0]][j-dim[0]][k-dim[0]] = 1

    def valid(x: int, y: int, z: int) -> bool:
        return (dim[0] <= x < dim[1]) and (dim[0] <= y < dim[1]) and (dim[0] <= z < dim[1])

    S = [(dim[1]-1, dim[1]-1, dim[1]-1)]

    while len(S) > 0:
        p = S.pop()
        setM(*p)
        for p2 in neighbors(*p):
            if valid(*p2) and not p2 in cubes and M(*p2) == 0 and M not in S:
                S.append(p2)
    
    connected = [0 for _ in range(len(cubes))]
    for i, (x, y, z) in enumerate(cubes):
        for cube2 in neighbors(x, y, z):
            if M(*cube2) == 0 or cube2 in cubes:
                connected[i] += 1

    return sum([6-connected[i] for i in range(len(connected))])


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
