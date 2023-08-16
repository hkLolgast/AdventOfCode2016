import re

def parse_input(file = 'day09.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day09example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    inp = format_input(inp)
    pattern = re.compile('\\((\\d+)x(\\d+)\\)')
    tot = 0
    for line in inp:
        look_index = 0
        match = pattern.search(line, look_index)
        if part == 1:
            decoded = ''
            while match:
                decoded += line[look_index:match.start()]
                length, repeats = int(match[1]), int(match[2])
                decoded += line[match.end():match.end() + length] * repeats
                look_index = match.end() + length
                match = pattern.search(line, look_index)
            decoded += line[look_index:]
            # if debug:
            #     print(decoded, len(decoded))

            tot += len(decoded)
        else:
            chars = []
            matches = []
            while match:
                length, repeats = int(match[1]), int(match[2])
                matches.append((match.end(), length, repeats))
                for i in range(look_index, match.start()):
                    chars.append([i, 1])
                look_index = match.end()
                match = pattern.search(line, look_index)
            for i in range(look_index, len(line)):
                chars.append([i, 1])
            min_i = 0
            for (start, length, repeats) in matches:
                i = min_i
                c = chars[i]
                while c[0] < start + length:
                    if c[0] < start:
                        min_i += 1
                        i += 1
                        c = chars[i]
                        continue
                    c[1] *= repeats
                    i += 1
                    if i == len(chars):
                        break
                    c = chars[i]
            tot += sum(c[1] for c in chars)
            # if debug:
            #     print(sum(c[1] for c in chars))


    return tot

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
