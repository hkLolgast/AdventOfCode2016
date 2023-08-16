def parse_input(file = 'day15.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day15example.txt')

def format_input(inp):
    disks = []
    for line in inp:
        s = line.split()
        disks.append((int(s[3]), int(s[-1][:-1])))
    return disks

def solve(inp, part, debug=False):
    disks = format_input(inp)
    if part == 2:
        disks.append((11, 0))
    t = 0
    while True:
        for i, (positions, starting) in enumerate(disks):
            if (t + i + 1 + starting) % positions != 0:
                break
        else:
            return t
        t += 1
    return None

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
