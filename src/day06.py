DAY = 6


def part1(inp: list[str]) -> int:
    line = inp[0]
    
    for i in range(len(line)-3):
        c1, c2, c3, c4 = line[i], line[i+1], line[i+2], line[i+3]

        if c1 not in (c2, c3, c4) and c2 not in (c3, c4) and c3 != c4:
            return i+4


def part2(inp: list[str]) -> int:
    line = inp[0]

    for i in range(len(line)-13):
        c = set()
        for k in range(14):
            c.add(line[i+k])

        if len(c) == 14:
            return i+14


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
