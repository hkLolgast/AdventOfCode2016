import itertools

def parse_input(file = 'day21.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day21example.txt')

def format_input(inp):
    ops = []
    for line in inp:
        s = line.split()
        command = ' '.join(s[:2])
        if line.startswith('rotate based'):
            ops.append((command, s[-1]))
        elif line.startswith('rotate'):
            ops.append((command, int(s[2])))
        elif 'letter' in line:
            ops.append((command, s[2], s[-1]))
        else:
            ops.append((command, int(s[2]), int(s[-1])))
    return ops

def solve(inp, part, debug=False):
    if part == 2 and debug:
        return None
    if part == 1:
        if debug:
            passwords = [list('abcde')]
        else:
            passwords = [list('abcdefgh')]
    else:
        passwords = itertools.permutations('abcdefgh', 8)
    ops = format_input(inp)
    for original_password in passwords:
        password = list(original_password[:])
        for command, *args in ops:
            scrambled = password[:]
            if command == 'swap position':
                scrambled[args[0]] = password[args[1]]
                scrambled[args[1]] = password[args[0]]
            elif command == 'swap letter':
                scrambled[password.index(args[0])] = args[1]
                scrambled[password.index(args[1])] = args[0]
            elif command == 'rotate left':
                scrambled = scrambled[args[0]:] + scrambled[:args[0]]
            elif command == 'rotate right':
                scrambled = scrambled[-args[0]:] + scrambled[:-args[0]]
            elif command == 'rotate based':
                amount = scrambled.index(args[0]) + 1
                if amount >= 5:
                    amount += 1
                amount %= len(scrambled)
                scrambled = scrambled[-amount:] + scrambled[:-amount]
            elif command == 'reverse positions':
                # print(scrambled, scrambled[args[1]:args[0]-1:-1], (args[1],args[0]-1,-1))
                scrambled = scrambled[:args[0]] + scrambled[args[1]:(args[0]-1) if args[0] > 0 else None:-1] + scrambled[args[1]+1:]
            elif command == 'move position':
                c = scrambled.pop(args[0])
                scrambled.insert(args[1], c)
            else:
                raise ValueError(command)
            password = scrambled
        # if debug:
        #     print(''.join(password))

        if part == 1:
            return ''.join(password)
        elif ''.join(password) == 'fbgdceah':
            return ''.join(original_password)

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
