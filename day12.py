def parse_input(file = 'day12.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day12example.txt')

def format_input(inp):
    commands = []
    for line in inp:
        commands.append(line.split())
    return commands

def solve(inp, part, debug=False):
    if part == 2:
        return None

    commands = format_input(inp)
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0
    while i < len(commands):
        command = commands[i]
        val = registers[command[1]] if command[1] in registers else eval(command[1])
        if command[0] == 'cpy':
            registers[command[2]] = val
        elif command[0] == 'inc':
            registers[command[1]] += 1
        elif command[0] == 'dec':
            registers[command[1]] -= 1
        elif command[0] == 'jnz':
            if val != 0:
                i += eval(command[2]) - 1
        else:
            raise ValueError
        i += 1
        
    return registers['a']

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
