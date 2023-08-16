def parse_input(file = 'day20.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day20example.txt')

def format_input(inp):
    ls = []
    for line in inp:
        start, end = line.split('-')
        ls.append((int(start), int(end)))
    return ls

def solve(inp, part, debug=False):
    inp = format_input(inp)
    inp = sorted(inp)
    blacklist = []
    current = list(inp[0])
    for start, end in inp[1:]:
        if start <= current[1] + 1:
            current[1] = max(current[1], end)
        else:
            blacklist.append(current)
            current = [start, end]
    blacklist.append(current)
    if part == 1:
        return blacklist[0][1] + 1
    else:
        if debug:
            print(blacklist)
        allowed = 0
        for i, item in enumerate(blacklist[:-1]):
            allowed += blacklist[i + 1][0] - item[1] - 1
            if debug:
                print(blacklist[i+1], item)
        if debug:
            max_allowed = 9
        else:
            max_allowed = 4294967295
        allowed += max_allowed - blacklist[-1][1]
    return allowed
def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
