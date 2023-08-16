def parse_input(file = 'day25.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day25example.txt')

def format_input(inp):
    commands = []
    for line in inp:
        commands.append(line.split())
    return commands

def run_code(commands, starting_registers):
    registers = {key: starting_registers[key] for key in starting_registers}
    i = 0
    seen_values = {i: [] for i in range(len(commands))}
    allow_short_circuit = False
    output = []
    output_states = []
    iters = 0
    while i < len(commands):
        # if iters == 50000:
        #     print(iters, registers, output)
        #     break
        iters += 1
        command = commands[i]
        # if starting_registers['a'] == 158:
        #     print(command, registers)
        val = registers[command[1]] if command[1] in registers else eval(command[1])
        if command[0] == 'cpy':
            registers[command[2]] = val
        elif command[0] == 'inc':
            registers[command[1]] += 1
        elif command[0] == 'dec':
            registers[command[1]] -= 1
        elif command[0] == 'jnz':
            if val != 0:
                amount = registers[command[2]] if command[2] in registers else eval(command[2])
                assert amount != 0
                if command[1] in registers:
                    seen_values[i].append([registers[c] for c in 'abcd'])

                if allow_short_circuit and len(seen_values[i]) == 3:
                    diffs = [[seen_values[i][j + 1][c] - seen_values[i][j][c] for c in range(4)] for j in range(2)]
                    if diffs[0] == diffs[1]:
                        ind = 'abcd'.index(command[1])
                        repeats_left = registers[command[1]] // -diffs[0][ind]
                        assert repeats_left >= 0
                        for j in range(4):
                            registers['abcd'[j]] += diffs[0][j] * repeats_left
                        assert registers[command[1]] == 0
                        seen_values[i] = []
                    # else:
                    #     print('Unequal diffs')
                else:
                    for key in seen_values:
                        if key < i and key >= i + amount and seen_values[key]:
                            seen_values[key] = []
                    i += amount - 1
        elif command[0] == 'tgl':
            try:
                target = commands[i + val]
            except IndexError:
                i += 1
                continue
            if len(target) == 2:
                if target[0] == 'inc':
                    commands[i + val] = ['dec', target[1]]
                else:
                    commands[i + val] = ['inc', target[1]]
            else:
                if target[0] == 'jnz':
                    commands[i + val] = ['cpy', target[1], target[2]]
                else:
                    commands[i + val] = ['jnz', target[1], target[2]]
            for key in seen_values:
                seen_values[key] = []
        elif command[0] == 'out':
            if val not in (0, 1):
                return False, [val], registers
            if not output and val != 0:
                return False, [val], registers
            if output and output[-1] == val:
                return False, output + [val], registers
            output.append(val)
            state = tuple(registers[c] for c in 'abcd')
            if len(output_states) > 2 and state in output_states[1::2]:
                return True, output, registers
            output_states.append(state)
        else:
            raise ValueError(f'Unknown command {command}')
        i += 1
    return False, [], registers

def solve(inp, part, debug=False):
    if part == 2:
        return None
    
    commands = format_input(inp)
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    best_length = 0
    while True:
        # print(registers['a'])
        try:
            status, result, final_registers = run_code(commands, registers)
            if status:
                # print('Found!')
                return registers['a']
            else:
                if registers['a'] == 158 or len(result) > best_length:
                    best_length = len(result)
                # print(registers['a'], result, final_registers)
                # else:
                #     print(registers['a'])
        except AssertionError as e:
            raise
        registers['a'] += 1
        # break

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
