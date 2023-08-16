def parse_input(file = 'day19.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day19example.txt')

def format_input(inp):
    return list(range(1, int(inp[0]) + 1))

def solve(inp, part, debug=False):
    people = format_input(inp)
    max_people = len(people)
    i = 0
    while len(people) > 1:
        if part == 1:
            new_people = people[::2]
            if len(people) % 2 == 1:
                new_people = new_people[1:]
        elif debug:
            to_remove = (i + len(people) // 2) % len(people)
            if to_remove < i:
                i -= 1
            new_people = people[:to_remove] + people[to_remove + 1:]
            i += 1
            if i >= len(people):
                i = 0
        else:
            if len(people) <= 2:
                return people[0]
            elif len(people) == 3:
                return people[-1]
            first_keep = len(people) // 2 + 1 + (len(people) % 2 == 0)
            new_people = (2 * people)[first_keep:len(people) + len(people) // 2:3]

            if len(new_people) * 3 < len(people):
                missing = people[len(people) // 2 - 1]
                new_people.append(missing)

            min_ind = new_people.index(min(new_people))
            new_people = new_people[min_ind:] + new_people[:min_ind]
        people = new_people
    return people[0]

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
