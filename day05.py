import hashlib

def parse_input(file = 'day05.txt'):
    with open(file) as f:
        return f.readline().strip()

def parse_example():
    return parse_input('day05example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    inp = format_input(inp)
    i = 0
    password = '' if part == 1 else ['_'] * 8
    while (part == 1 and len(password) < 8) or (part == 2 and '_' in password):
        hash = hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            if part == 1:
                password += hash[5]
            else:
                try:
                    index = int(hash[5])
                    if index < len(password) and password[index] == '_':
                        password[index] = hash[6]
                        print(''.join(password))
                except ValueError:
                    pass
        i += 1
    return ''.join(password)

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
