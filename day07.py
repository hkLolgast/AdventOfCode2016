def parse_input(file = 'day07.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day07example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):

    inp = format_input(inp)
    count = 0
    for ip in inp:
        has_abba = False
        in_hypernet = False
        abas = []
        babs = []
        for i in range(len(ip) - 4 + part):
            a = ip[i]
            if a == '[':
                in_hypernet = True
                continue
            if a == ']':
                in_hypernet = False
                continue
            b = ip[i+1]
            if b in '[]' + a:
                continue
            if part == 1 and ip[i+2] == b and ip[i+3] == a:
                if in_hypernet and part == 1:
                    break
                has_abba = True
            if part == 2 and ip[i+2] == a:
                if not in_hypernet:
                    if a + b + a in abas:
                        count += 1
                        break
                    babs.append(b + a + b)
                else:
                    if a + b + a in babs:
                        # if debug:
                        #     print(ip)
                        count += 1
                        break
                    abas.append(b + a + b)
        else:
            if part == 1:
                count += has_abba
        
    return count

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
