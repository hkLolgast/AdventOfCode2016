def parse_input(file = 'day03.txt'):
    with open(file) as f:
        s = map(lambda l: tuple(map(int, l.split())), f.readlines())
    
    return list(s)

def parse_example():
    return parse_input('day03example.txt')

def format_input(inp):
    return inp

def is_valid_triangle(triangle):
    sorted_triangle = sorted(triangle)
    return sorted_triangle[0] + sorted_triangle[1] > sorted_triangle[2]

def solve(inp, part, debug=False):
    inp = format_input(inp)
    tot = 0
    if part == 1:
        for triangle in inp:
            tot += is_valid_triangle(triangle)
        return tot
    
    for i in range(0, len(inp), 3):
        r1, r2, r3 = inp[i], inp[i+1], inp[i+2]
        for j in range(3):
            t = (r1[j], r2[j], r3[j])
            tot += is_valid_triangle(t)
    return tot

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
