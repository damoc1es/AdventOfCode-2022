DAY = 8


def part1(inp: list[str]) -> int:
    mat = []
    for line in inp:
        mat.append([int(x) for x in line])

    k = (len(mat)-1)*2 + (len(mat[0])-1)*2;
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[0])-1):
            ok = True
            for t in range(i):
                if mat[t][j] >= mat[i][j]:
                    ok = False; break
            if ok:
                k += 1
                continue

            ok = True
            for t in range(j):
                if mat[i][t] >= mat[i][j]:
                    ok = False; break
            if ok:
                k += 1
                continue

            ok = True
            for t in range(j+1, len(mat[0])):
                if mat[i][t] >= mat[i][j]:
                    ok = False; break
            if ok:
                k += 1
                continue

            ok = True
            for t in range(i+1, len(mat)):
                if mat[t][j] >= mat[i][j]:
                    ok = False; break
            if ok: k += 1

    return k


def part2(inp: list[str]) -> int:
    mat = []
    for line in inp:
        mat.append([int(x) for x in line])

    possible = []
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[0])-1):
            k1 = k2 = k3 = k4 = 0

            for t in range(i)[::-1]:
                if mat[t][j] >= mat[i][j]:
                    k1 += 1
                    break
                k1 += 1

            for t in range(j)[::-1]:
                if mat[i][t] >= mat[i][j]:
                    k2 += 1
                    break
                k2 += 1

            for t in range(j+1, len(mat[0])):
                if mat[i][t] >= mat[i][j]:
                    k3 += 1
                    break
                k3 += 1

            for t in range(i+1, len(mat)):
                if mat[t][j] >= mat[i][j]:
                    k4 += 1
                    break
                k4 += 1
            
            possible.append(k1 * k2 * k3 * k4)

    return max(possible)


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
