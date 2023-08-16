from collections import defaultdict

def parse_input(file = 'day06.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day06example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):

    inp = format_input(inp)
    message = ''
    for i in range(len(inp[0])):
        counts = defaultdict(int)
        for word in inp:
            counts[word[i]] += 1
        if part == 1:
            message += max(counts.keys(), key = lambda x: counts[x])
        else:
            message += min(counts.keys(), key = lambda x: counts[x])

    return message

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
