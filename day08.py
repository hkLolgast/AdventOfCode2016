import numpy as np

def parse_input(file = 'day08.txt'):
    ops = []
    with open(file) as f:
        for line in f:
            args = []
            if line.startswith('rect'):
                op = 'rect'
                arg1 = int(line[5:line.index('x')])
                arg2 = int(line[line.index('x')+1:])
            elif line.startswith('rotate column'):
                op = 'col'
                arg1 = int(line[16:line.index(' by')])
                arg2 = int(line[line.index(' by') + 4:])
            else:
                assert line.startswith('rotate row')
                op = 'row'
                arg1 = int(line[13:line.index(' by')])
                arg2 = int(line[line.index(' by') + 4:])
            ops.append((op, arg1, arg2))
    return ops

def parse_example():
    return parse_input('day08example.txt')

def format_input(inp):
    return inp

def print_screen(screen):
    for row in screen:
        l = ''
        for val in row:
            l += '#' if val else '.'
        print(l)
    print()

def solve(inp, part, debug=False):
    if part == 2:
        return None

    inp = format_input(inp)
    screen = np.zeros((6, 50))
    for op, arg1, arg2 in inp:
        if op == 'rect':
            screen[:arg2, :arg1] = 1
        elif op == 'row':
            screen[arg1, :] = np.concatenate((screen[arg1, -arg2:], screen[arg1, :-arg2]))
        else:
            screen[:, arg1] = np.concatenate((screen[-arg2:, arg1], screen[:-arg2, arg1]))
    print_screen(screen)
    return int(sum(sum(screen)))

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
