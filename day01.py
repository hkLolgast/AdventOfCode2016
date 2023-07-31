def parse_input(file = 'day01.txt'):
    with open(file) as f:
        s = f.readline().split(', ')
    return s

def parse_example():
    return parse_input('day01example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    inp = format_input(inp)
    direction = 0
    loc = [0, 0]
    seen = set()
    for command in inp:
        turn = command[0]
        amount = int(command[1:])
        if turn == 'L':
            direction -= 1
        elif turn == 'R':
            direction += 1
        else:
            print(f'Trouble parsing command {command}')
        direction %= 4

        for i in range(amount):
            if direction == 0:
                loc[0] += 1
            elif direction == 1:
                loc[1] += 1
            elif direction == 2:
                loc[0] -= 1
            else:
                loc[1] -= 1
            if tuple(loc) in seen and part == 2:
                return abs(loc[0]) + abs(loc[1])
            seen.add(tuple(loc))
    if part == 1:
        return abs(loc[0]) + abs(loc[1])

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
    
