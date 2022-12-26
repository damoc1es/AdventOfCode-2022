DAY = 1


def part1(inp: list[str]) -> int:
    cal = 0
    maxc = -1

    for line in inp:
        if line == '':
            cal = 0
        else:
            cal += int(line)

        if cal > maxc:
            maxc = cal

    return maxc


def part2(inp: list[str]) -> int:
    cal = 0
    vec = []

    for line in inp:
        if line == '':
            vec.append(cal)
            cal = 0
        else:
            cal += int(line)

    vec.sort(reverse=True)
    return sum(vec[:3])


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
