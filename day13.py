from AoCHelpers import optimization

def parse_input(file = 'day13.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day13example.txt')

def format_input(inp):
    return int(inp[0])

def is_open(location, number):
    x, y = location
    if x < 0 or y < 0:
        return False
    v = x*x + 3*x + 2*x*y + y + y*y + number
    binary = bin(v)[2:]
    return binary.count('1') % 2 == 0

def solve(inp, part, debug=False):
    if debug:
        target_location = (7, 4)
    else:
        target_location = (31, 39)
    pathfinder = optimization.Pathfinder(None, (1, 1), target_location)
    pathfinder.neighbors = optimization.ORTHOGONAL
    fav_number = format_input(inp)
    pathfinder.is_valid_location = lambda location: is_open(location, fav_number)

    if part == 1:
        return pathfinder.get_minimal_path()
    pathfinder.max_steps = 50
    try:
        pathfinder.get_minimal_path()
    except ValueError as e:
        return int(str(e).split()[7][1:])

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
