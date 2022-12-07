import numpy as np
from copy import deepcopy

DAY = 7


def size_of_dir(dir_dict: dict, path: str) -> int:
    size = 0
    for t in dir_dict[path]:
        if t[0] != 'dir':
            size += int(t[0])
        else:
            if path != '/':
                size += size_of_dir(dir_dict, path+f"/{t[1]}")
            else: size += size_of_dir(dir_dict, path+t[1])

    return size


def part1(inp: list[str]) -> int:
    dir_dict = {}
    path = ""
    for i in range(len(inp)):
        line = inp[i]

        st = line.split()
        if st[1] == "cd":
            if line == "$ cd /":
                path = "/"
            elif line == "$ cd ..":
                path = path[:path.rfind('/')]
            else:
                if path != "/":
                    path += "/"
                path += st[2]
        elif line == "$ ls":
            i += 1
            lst = []
            st = inp[i].split()
            while i != len(inp) and st[0] != '$':
                lst.append((st[0], st[1]))

                i += 1
                if  i != len(inp):
                    st = inp[i].split()

            dir_dict[path] = lst;

    all_size = 0
    for key in dir_dict:
        K = size_of_dir(dir_dict, key)
        if K < 100000:
            all_size += K

    return all_size


def part2(inp: list[str]) -> int:
    dir_dict = {}
    path = ""
    for i in range(len(inp)):
        line = inp[i]

        st = line.split()
        if st[1] == "cd":
            if line == "$ cd /":
                path = "/"
            elif line == "$ cd ..":
                path = path[:path.rfind('/')]
            else:
                if path != "/":
                    path += "/"
                path += st[2]
        elif line == "$ ls":
            i += 1
            lst = []
            st = inp[i].split()
            while i != len(inp) and st[0] != '$':
                lst.append((st[0], st[1]))

                i += 1
                if  i != len(inp):
                    st = inp[i].split()

            dir_dict[path] = lst;

    dir_all = {}
    for key in dir_dict:
        dir_all[key] = size_of_dir(dir_dict, key)

    needed_space = 30000000
    used_space = 70000000-dir_all["/"]

    possible = []

    for d in dir_all:
        if used_space + dir_all[d] >= needed_space:
            possible.append(dir_all[d])

    return min(possible)


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input0{DAY}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
