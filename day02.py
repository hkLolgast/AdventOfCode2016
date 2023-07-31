def parse_input(file = 'day02.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day02example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    inp = format_input(inp)
    loc = [1, 1] if part == 1 else [2, 0]
    password = ''
    for line in inp:
        for c in line:
            new_loc = loc[:]
            if c == 'U':
                new_loc[0] -= 1
            elif c == 'D':
                new_loc[0] += 1
            elif c == 'L':
                new_loc[1] -= 1
            elif c == 'R':
                new_loc[1] += 1
            else:
                print(f"Couldn't parse {c}")
            if part == 1:
                if (0 <= new_loc[0] <= 2) and (0 <= new_loc[1] <= 2):
                    loc = new_loc
            else:
                if new_loc[0] in (0, 4) and new_loc[1] == 2:
                    loc = new_loc
                if new_loc[0] in (1, 3) and 1 <= new_loc[1] <= 3:
                    loc = new_loc
                if new_loc[0] == 2 and 0 <= new_loc[1] <= 4:
                    loc = new_loc
        
        if debug:
            print(loc)
        if part == 1:
            password += ['123', '456', '789'][loc[0]][loc[1]]
        else:
            password += ['  1  ', ' 234 ', '56789', ' ABC ', '  D  '][loc[0]][loc[1]]
    return password

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
