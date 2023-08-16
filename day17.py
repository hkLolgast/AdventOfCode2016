import hashlib
from AoCHelpers import optimization

def parse_input(file = 'day17.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day17example.txt')

def format_input(inp):
    return inp[0]

class Pathfinder(optimization.BranchAndBound):
    def get_valid_moves(self, state):
        inp, loc = state
        hash = hashlib.md5(inp.encode('utf-8')).hexdigest()
        for i in range(4):
            if loc == (3, 3):
                break
            if hash[i] in 'bcdef':
                move = 'UDLR'[i]
                if loc[0] > 0 and move == 'L':
                    yield move
                elif loc[0] < 3 and move == 'R':
                    yield move
                elif loc[1] > 0 and move == 'U':
                    yield move
                elif loc[1] < 3 and move == 'D':
                    yield move

    def apply_move(self, state, move):
        inp, loc = state
        inp += move
        if move == 'U':
            loc = (loc[0], loc[1] - 1)
        elif move == 'D':
            loc = (loc[0], loc[1] + 1)
        elif move == 'L':
            loc = (loc[0] - 1, loc[1])
        else:
            loc = (loc[0] + 1, loc[1])
        return inp, loc

    def is_finished(self, state):
        return state[1] == (3, 3)
    
    def get_state_hash(self, state):
        return state

def solve(inp, part, debug=False):
    inp = format_input(inp)
    pathfinder = Pathfinder(starting_state = (inp, (0, 0)), find_all_solutions = part == 2)

    sols = pathfinder.get_minimal_path()
    if part == 1:
        return sols[1][0][len(inp):]
    else:
        # if debug:
        #     print(sols)
        return sols[-1][0]


def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
