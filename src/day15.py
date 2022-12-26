from z3 import *

DAY = 15


def manhattan(x: tuple[int, int], y: tuple[int, int]) -> int:
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def parse_input(inp: list[str]) -> tuple[int, int, int, int]:
    output = []
    for line in inp:
        sensor, beacon = line.split(':')
        _, _, x1, y1 = sensor.split()
        _, _, _, _, x2, y2, = beacon.split()
        x1 = int(x1.split('=')[1][:-1])
        y1 = int(y1.split('=')[1])
        x2 = int(x2.split('=')[1][:-1])
        y2 = int(y2.split('=')[1])

        output.append((x1, y1, x2, y2))
    
    return output


def part1(inp: list[str]) -> int:
    target = 2000000
    
    unavailable = set()
    beacons = set()

    for x1, y1, x2, y2 in parse_input(inp):
        p1 = (x1, y1)
        p2 = (x2, y2)
        dist = manhattan(p1, p2)

        beacons.add(p2)
        
        for x in range(x1-dist, x1+dist+1):
            if manhattan(p1, (x, target)) < dist+1:
                unavailable.add((x, target))

    return len(unavailable-beacons)


# shamelessly borrowed
def part2(inp: list[str]) -> int:
    def z3_abs(x):
        return If(x >= 0, x, -x)


    s = Solver()
    
    x = Int("x")
    y = Int("y")
    
    s.add(x >= 0)
    s.add(y >= 0)
    s.add(x <= 4000000)
    s.add(y <= 4000000)
    
    for x1, y1, x2, y2 in parse_input(inp):
        dist = manhattan((x1, y1), (x2, y2))
        s.add(z3_abs(x - x1) + z3_abs(y - y1) > dist)

    s.check()
    model = s.model()
    
    return model[x].as_long() * 4000000 + model[y].as_long()


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")
    
    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
