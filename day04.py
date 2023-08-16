from string import ascii_lowercase

def parse_input(file = 'day04.txt'):
    rooms = []
    with open(file) as f:
        for line in f.readlines():
            bracket = line.index('[')
            checksum = line[bracket+1:bracket+6]
            for i in range(bracket, 0, -1):
                if line[i] == '-':
                    name = line[:i]
                    number = line[i+1:bracket]
                    break
            rooms.append((name, int(number), checksum))
    return rooms

def parse_example():
    return parse_input('day04example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    rooms = format_input(inp)
    tot = 0
    for name, id, checksum in rooms:
        counts = {}
        for c in set(name):
            if c == '-':
                continue
            counts[c] = name.count(c)
        check = ''.join(sorted(counts.keys(), key = lambda c: (-counts[c], c)))[:5]
        # if debug:
        #     print(check, checksum)
        if check == checksum:
            tot += id
            if part == 2:
                decrypted_name = ''
                for c in name:
                    if c == '-':
                        decrypted_name += ' '
                        continue
                    new_ind = (ascii_lowercase.index(c) + id) % 26
                    decrypted_name += ascii_lowercase[new_ind]
                if 'north' in decrypted_name or debug:
                    print(decrypted_name, id)

    return tot

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
