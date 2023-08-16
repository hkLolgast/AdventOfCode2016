from AoCHelpers import optimization

def parse_input(file = 'day22.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day22example.txt')

def format_input(inp):
    disks = []
    for line in inp[2:]:
        s = line.split()
        size, used, available = list(map(lambda s: int(s.rstrip('T')), s[1:4]))
        x = int(s[0].split('-')[1][1:])
        y = int(s[0].split('-')[2][1:])
        disks.append(((x, y), size, used, available))
    return disks

# class DataMover(optimization.BranchAndBound):
#     def __init__(self, disks, **kwargs):
#         self.disks = {loc: (size, used, available) for loc, size, used, available in disks}


def solve(inp, part, debug=False):
    disks = format_input(inp)
    if part == 1:
        pairs = 0
        for disk1 in disks:
            if disk1[2] == 0:
                continue
            for disk2 in disks:
                if disk1 is disk2:
                    continue
                if disk2[3] >= disk1[2]:
                    pairs += 1

        return pairs
    else:
        max_x = max(disk[0][0] for disk in disks)
        max_y = max(disk[0][1] for disk in disks)
        for y in range(0,  max_y + 1):
            s = ''
            for x in range(0,  max_x + 1):
                for disk in disks:
                    if disk[0] == (x, y):
                        if disk[2] <= 20:
                            s += '_'
                        elif disk[2] > 100:
                            s += '#'
                        else:
                            s += '.'
                        break
            print(s)
        return None

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
