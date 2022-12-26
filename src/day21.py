from sympy import sympify, solve

DAY = 21


def parse_input(inp: list[str]) -> dict[str]:
    monke = {}
    for line in inp:
        yells = line.split(": ")
        if len(yells[1].split()) > 2:
            monke[yells[0]] = yells[1]
        else:
            monke[yells[0]] = int(yells[1])
    
    return monke


def part1(inp: list[str]) -> int:
    monke = parse_input(inp)
    
    while type(monke["root"]) != int:
        for k, v in monke.items():
            if type(v) == int:
                continue

            match v.split():
                case [x, '+', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] + monke[y]
                case [x, '*', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] * monke[y]
                case [x, '/', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] // monke[y]
                case [x, '-', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] - monke[y]
    
    return monke['root']


def part2(inp: list[str]) -> int:
    monke = parse_input(inp)

    monke['humn'] = "NOPE"
    monke['root'] = f"{monke['root'].split()[0]} {monke['root'].split()[2]}"

    ok = False
    while not ok:
        ok = True
        for k, v in monke.items():
            if type(v) == int or k == 'humn':
                continue

            match v.split():
                case [x, '+', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] + monke[y]
                        ok = False
                case [x, '*', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] * monke[y]
                        ok = False
                case [x, '/', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] // monke[y]
                        ok = False
                case [x, '-', y]:
                    if type(monke[x]) == int and type(monke[y]) == int:
                        monke[k] = monke[x] - monke[y]
                        ok = False

    for eq in monke['root'].split():
        if type(monke[eq]) == int:
            continue

        ok = False
        while not ok:
            ok = True
            redone = ""

            for m in monke[eq].split():
                if m in ('+', '/', '*', '-', '(', ')') or m == 'humn':
                    redone += f"{m} "
                    continue
                
                if m in monke:
                    redone += f" ( {monke[m]} ) "
                    ok = False
                else:
                    redone += f"{m} "
            monke[eq] = redone
    
    equation = f"{monke[monke['root'].split()[0]]} = {monke[monke['root'].split()[1]]}".replace("humn", "x")
    
    return solve(sympify("Eq(" + equation.replace("=", ",") + ")"))[0]


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
