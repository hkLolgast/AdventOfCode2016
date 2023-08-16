def parse_input(file = 'day16.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day16example.txt')

def format_input(inp):
    return inp[0]

def solve(inp, part, debug=False):
    data = format_input(inp)
    length = 20 if debug else (272 if part == 1 else 35651584)
    while len(data) < length:
        b = ''.join('1' if c == '0' else '0' for c in data)
        data = data + '0' + b[::-1]

    data = data[:length]
    checksum = ''
    while len(data) % 2 == 0:
        for i in range(0, len(data), 2):
            checksum += str(int(data[i] == data[i+1]))
        data = checksum
        checksum = ''
    return data

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
