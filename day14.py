import hashlib

def parse_input(file = 'day14.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day14example.txt')

def format_input(inp):
    return inp[0]

def solve(inp, part, debug=False):
    keys = set()
    potential_keys = {c: [] for c in '0123456789abcdef'}
    inp = format_input(inp)
    i = 0
    max_i = 10**99
    while len(keys) < 100 and i < max_i:
        hash = hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()
        if part == 2:
            for _ in range(2016):
                hash = hashlib.md5((hash).encode('utf-8')).hexdigest()
        indices = []
        for c in '0123456789abcdef':
            if 3 * c in hash:
                if 5 * c in hash:
                    for key in potential_keys[c][:]:
                        if i - key <= 1000:
                            keys.add(key)
                            if len(keys) >= 64:
                                max_i = min(max_i, key + 2000)
                            # if debug and part == 2:
                            #     print(key)
                        potential_keys[c].remove(key)
                indices.append((c, hash.index(3 * c)))
        if indices:
            first = sorted(indices, key = lambda ind: ind[1])[0][0]
            potential_keys[first].append(i)
                 
        i += 1
    keys = sorted(keys)
    # assert i > keys[63] + 1000
    # print(keys[64], sorted(k[0] for k in keys)[63])
    
    return keys[63]

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
