from collections import defaultdict

def parse_input(file = 'day10.txt'):
    bots = defaultdict(lambda: {'inputs': [], 'outputs': []})
    with open(file) as f:
        for line in f:
            if line.startswith('value'):
                value = int(line.split()[1])
                bot = int(line.split()[-1])
                bots[bot]['inputs'].append(value)
            else:
                splits = line.split()
                bot = int(splits[1])
                bots[bot]['low_type'] = splits[5]
                bots[bot]['low_value'] = int(splits[6])
                bots[bot]['high_type'] = splits[-2]
                bots[bot]['high_value'] = int(splits[-1])
                

    return bots

def parse_example():
    return parse_input('day10example.txt')

def format_input(inp):
    return inp

def solve(inp, part, debug=False):
    bots = format_input(inp)
    outputs = {}
    to_check = set(bot for bot in bots if len(bots[bot]['inputs']) == 2)
    while to_check:
        new_to_check = set()
        while to_check:
            bot_number = to_check.pop()
            bot = bots[bot_number]
            assert len(bot['inputs']) == 2
            if part == 1 and 61 in bot['inputs'] and 17 in bot['inputs']:
                return bot_number
            low = min(bot['inputs'])
            high = max(bot['inputs'])
            low_value, high_value = bot['low_value'], bot['high_value']
            if bot['low_type'] == 'bot':
                bots[low_value]['inputs'].append(low)
                if len(bots[low_value]['inputs']) == 2:
                    new_to_check.add(low_value)
            else:
                assert low_value not in outputs
                outputs[low_value] = low
            
            if bot['high_type'] == 'bot':
                bots[high_value]['inputs'].append(high)
                if len(bots[high_value]['inputs']) == 2:
                    new_to_check.add(high_value)
            else:
                assert high_value not in outputs
                outputs[high_value] = high

            bot['inputs'] = []
            if debug:
                for bot in bots:
                    print(bots[bot])
                print(to_check)
                print(new_to_check)
                print()
        to_check = new_to_check
    
    print(outputs[0], outputs[1], outputs[2])
    return outputs[0] * outputs[1] * outputs[2]

def main(debug = False):
    s = ''
    for part in (1, 2):
        s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
        s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    return s.rstrip()
