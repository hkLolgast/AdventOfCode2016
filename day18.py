def parse_input(file = 'day18.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day18example.txt')

def format_input(inp):
    return [c == '^' for c in inp[0]]

def solve(inp, part, debug=False):
    rows = []
    rows.append(format_input(inp))
    max_rows = 10 if debug else 40 if part == 1 else 400000
    while len(rows) < max_rows:
        new_row = [rows[-1][1]]
        for i in range(1, len(rows[-1]) - 1):
            is_trap = rows[-1][i-1] ^ rows[-1][i+1]
            new_row.append(is_trap)
        new_row.append(rows[-1][-2])
        rows.append(new_row)
    # if debug:
    #     for row in rows:
    #         print(''.join('^' if c else '.' for c in row))
    return sum(len(row) - sum(row) for row in rows)

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
