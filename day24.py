import numpy as np
from itertools import permutations

from AoCHelpers import optimization

def parse_input(file = 'day24.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day24example.txt')

def format_input(inp):
    locs = {}
    maze = np.empty((len(inp[0]), len(inp)), dtype = bool)
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c == '#':
                maze[x, y] = False
            else:
                maze[x, y] = True
                if c != '.':
                    assert c not in locs
                    locs[int(c)] = (x, y)
    return maze, locs

def solve(inp, part, debug=False):
    maze, locs = format_input(inp)
    loc_ids = list(range(max(locs) + 1))
    distances = {}
    for i in loc_ids:
        for j in range(i+1, max(locs) + 1):
            pathfinder = optimization.Pathfinder(maze, locs[i], locs[j])
            pathfinder.neighbors = optimization.ORTHOGONAL
            distances[(i, j)] = pathfinder.get_minimal_path()[0]
            distances[(j, i)] = distances[(i, j)]
    
    shortest_dist = 10**99
    shortest_path = None
    for order in permutations(loc_ids[1:], len(loc_ids) - 1):
        dist = distances[(0, order[0])]
        if part == 2:
            dist += distances[(order[-1], 0)]
        for i, loc in enumerate(order[:-1]):
            dist += distances[(loc, order[i+1])]
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = (0,) + order
    # print(shortest_path, shortest_dist)
    return shortest_dist

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
