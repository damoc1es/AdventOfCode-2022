# u/DrunkHacker
from collections import namedtuple, defaultdict
import heapq

DAY = 16


def parse_input(inp: list[str]) -> tuple[dict[str, int], dict[str, list[str]]]:
    adj = {}
    valves = {}

    for line in inp:
        valve, tunnels = line.split('; ')
        
        valve, rate = valve.split(" has flow rate=")
        valve = valve.split()[1]
        rate = int(rate)

        _, _, _, _, *tunnels = tunnels.split()
        tunnels = [x.split(',')[0] for x in tunnels]
        
        adj[valve] = tunnels
        valves[valve] = rate
    
    return valves, adj


def floyd_warshall(valves: dict[str, int], adj: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    dist = {a: {b: float("+inf") for b in valves} for a in valves}

    for u in valves:
        dist[u][u] = 0
        for v in adj[u]:
            dist[u][v] = 1
    
    for k in valves:
        for i in valves:
            for j in valves:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


State = namedtuple("State", "flow,p1,t1,p2,t2,closed")
State.time = lambda s: min(s.t1, s.t2)


def human_states(valves: dict[str, int], dist: dict[str, dict[str, int]], s: State) -> list[State]:
    if s.time() != s.t1:
        return [s]

    if valves[s.p1] and s.p1 in s.closed:
        return [s._replace(
            flow = s.flow - (29-s.time()) * valves[s.p1],
            t1 = s.t1 + 1,
            closed = s.closed - {s.p1},
        )]

    new_states = [s._replace(
            p1 = dest,
            t1 = s.t1 + dist[s.p1][dest],
        ) for dest in s.closed]

    if not new_states:
        return [s._replace(t1=30)]
    
    return new_states


def elephant_states(valves: dict[str, int], dist: dict[str, dict[str, int]], states: list[State]) -> list[State]:
    new_states = []

    for s in states:
        if s.time() != s.t2:
            new_states.append(s)
        
        elif valves[s.p2] and s.p2 in s.closed:
            new_states.append(s._replace(
                flow = s.flow - (29 - s.time()) * valves[s.p2],
                t2 = s.t2 + 1,
                closed = s.closed - {s.p2},
            ))
        
        else:
            new_states.extend([s._replace(
                p2 = dest,
                t2 = s.t2 + dist[s.p2][dest],
            ) for dest in s.closed])

    if not new_states:
        return [s._replace(t2=30) for s in states]
    
    return new_states


def part1(inp: list[str]) -> int:
    valves, adj = parse_input(inp)
    dist = floyd_warshall(valves, adj)

    pq = []
    heapq.heappush(pq, State(0, 'AA', 0, 'AA', 30, set(filter(lambda k: valves[k], valves))))

    best, best_for_time = 0, defaultdict(int)

    while pq:
        cur = heapq.heappop(pq)
        best = min(cur.flow, best)
        best_for_time[cur.time()] = min(best_for_time[cur.time()], cur.flow)

        if cur.time() < 30 and cur.closed and (cur.time() < 10 or 1.5 * cur.flow <= best_for_time[cur.time()]):
            for s in human_states(valves, dist, cur):
                heapq.heappush(pq, s)

    return -best


def part2(inp: list[str]) -> int:
    valves, adj = parse_input(inp)
    dist = floyd_warshall(valves, adj)

    pq = []
    heapq.heappush(pq, State(0, 'AA', 4, 'AA', 4, set(filter(lambda k: valves[k], valves))))
    
    best, best_for_time = 0, defaultdict(int)

    while pq:
        cur = heapq.heappop(pq)
        best = min(cur.flow, best)
        best_for_time[cur.time()] = min(best_for_time[cur.time()], cur.flow)

        if cur.time() < 30 and cur.closed:
            if cur.time() < 12 or 1.25 * cur.flow <= best_for_time[cur.time()]:
                h_states = human_states(valves, dist, cur)
                e_states = elephant_states(valves, dist, h_states)

                for s in e_states:
                    heapq.heappush(pq, s)
    
    return -best


def read_input_file(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf8') as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == '__main__':
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
