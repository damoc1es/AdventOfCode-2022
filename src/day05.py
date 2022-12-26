import numpy as np

DAY = 5


def part1(inp: list[str]) -> str:
    mat = []
    i = 0
    for line in inp:
        if line == '':
            break
        mat.append(list(inp[i]))
        i += 1
    inp = inp[i+1:]
    
    p = [[]]
    for row in np.fliplr(np.array(mat).transpose()).tolist():
        if row[0] != ' ':
            p.append([])
            for c in row[1:]:
                if c != ' ':
                    p[-1].append(c)

    for line in inp:
        _, c, _, pos1, _, pos2 = line.split()
        c, pos1, pos2 = [int(t) for t in (c, pos1, pos2)]

        for _ in range(c):
            p[pos2].append(p[pos1].pop())

    p = p[1:]
    sol = ""
    for pack in p:
        sol += pack[-1]

    return sol


def part2(inp: list[str]) -> str:
    mat = []
    i = 0
    for line in inp:
        if line == '':
            break
        mat.append(list(inp[i]))
        i += 1
    inp = inp[i+1:]
    
    p = [[]]
    for row in np.fliplr(np.array(mat).transpose()).tolist():
        if row[0] != ' ':
            p.append([])
            for c in row[1:]:
                if c != ' ':
                    p[-1].append(c)

    for line in inp:
        _, c, _, pos1, _, pos2 = line.split()
        c, pos1, pos2 = [int(t) for t in (c, pos1, pos2)]
        
        aux = []
        for _ in range(c):
            aux.append(p[pos1].pop())
        for _ in range(c):
            p[pos2].append(aux.pop())
    
    p = p[1:]
    sol = ""
    for pack in p:
        sol += pack[-1]
    return sol


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip('\n') for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
