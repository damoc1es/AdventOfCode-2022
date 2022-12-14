import numpy as np
from copy import deepcopy

DAY = 14


SAND_START = (0, 500)
def parse_input(inp: list[str]) -> tuple[list[list[int]], int]:
    Map = [[0 for _ in range(1000)] for _ in range(1000)]
    max_x = 0

    for line in inp:
        coords = line.split(' -> ')
        
        for i in range(len(coords)-1):
            y1, x1 = [int(t) for t in coords[i].split(',')]
            y2, x2 = [int(t) for t in coords[i+1].split(',')]
            
            max_x = max(max_x, x1, x2)
            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2)+1):
                    Map[x1][j] = -1
            else:
                for j in range(min(x1, x2), max(x1, x2)+1):
                    Map[j][y1] = -1
    
    Map[SAND_START[0]][SAND_START[1]] = 2

    return Map, max_x


def part1(inp: list[str]) -> int:
    Map, max_x = parse_input(inp)

    i = 0
    while True:
        i += 1
        c = SAND_START

        ok = False
        while not ok:
            ok = True

            abyss = True
            for j in range(c[0],max_x+1):
                if Map[j][c[1]] == -1:
                    abyss = False
            if abyss:
                return i-1

            if Map[c[0]+1][c[1]] == 0:
                ok = False
                c = (c[0]+1, c[1])
            elif Map[c[0]+1][c[1]-1] == 0:
                ok = False
                c = (c[0]+1, c[1]-1)
            elif Map[c[0]+1][c[1]+1] == 0:
                ok = False
                c = (c[0]+1, c[1]+1)

        Map[c[0]][c[1]] = 1


def part2(inp: list[str]) -> int:
    Map, max_x = parse_input(inp)

    for i in range(1000):
        Map[max_x+2][i] = -1

    i = 0
    while True:
        i += 1
        c = SAND_START

        ok = False
        while not ok:
            ok = True

            if Map[c[0]+1][c[1]] == 0:
                ok = False
                c = (c[0]+1, c[1])
            elif Map[c[0]+1][c[1]-1] == 0:
                ok = False
                c = (c[0]+1, c[1]-1)
            elif Map[c[0]+1][c[1]+1] == 0:
                ok = False
                c = (c[0]+1, c[1]+1)
        
        if c == SAND_START:
            return i
        
        Map[c[0]][c[1]] = 1


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
