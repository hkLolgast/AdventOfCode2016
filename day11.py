from copy import deepcopy

from AoCHelpers import optimization

def parse_input(file = 'day11.txt'):
    floors = []
    with open(file) as f:
        for line in f:
            floor = [[], []]
            if 'nothing relevant' in line:
                floors.append(floor)
                continue
            words = line.split()
            for i, word in enumerate(words):
                if 'microchip' in word or 'generator' in word:
                    continue
                if '-compatible' in word:
                    floor[1].append(word[:word.index('-')])
                elif 'generator' in words[i+1]:
                    floor[0].append(word)
            floors.append(floor)

    return [0, floors]

def parse_example():
    return parse_input('day11example.txt')

def format_input(inp):
    return inp

class ChipMover(optimization.BranchAndBound):
    def get_valid_moves(self, state):
        # if self.current_step == 2:
        #     print(f'Getting valid moves for state {state}')
        elevator_floor, floors = state
        current_gens, current_chips = floors[elevator_floor]
        potential_moves = []
        pair_seen = False
        for i1 in range(len(current_gens + current_chips)):
            if i1 < len(current_gens):
                move = [('gen', current_gens[i1])]
            else:
                move = [('chip', current_chips[i1 - len(current_gens)])]
            potential_moves.append(move)
            for i2 in range(i1 + 1, len(current_gens + current_chips)):
                if i2 < len(current_gens):
                    potential_moves.append(move + [('gen', current_gens[i2])])
                else:
                    chip_type = current_chips[i2 - len(current_gens)]
                    if chip_type == move[0][1]:
                        if pair_seen:
                            continue
                        else:
                            pair_seen = True
                    potential_moves.append(move + [('chip', chip_type)])
        
        # pair_seen = False
        # for contents in potential_moves[:]:
        #     if len(contents) == 1:
        #         continue
        #     if contents[0][0] == 'gen' and contents[1][0] == 'chip' and contents[0][1] == contents[1][1]:
        #         if pair_seen:
        #             potential_moves.remove(contents)
        #         else:
        #             pair_seen = True

        if elevator_floor > 0 and len(move) == 1:
            for move in potential_moves:
                if self.is_valid_move([elevator_floor, -1] + move, floors):
                    yield [-1] + move
        if elevator_floor < 3:
            for move in potential_moves:
                if self.is_valid_move([elevator_floor, 1] + move, floors):
                    yield [1] + move  

    def apply_move(self, state, move):
        elevator_floor, floors = deepcopy(state)
        elevator_move, *contents = move
        new_floors = []
        for i, floor in enumerate(floors):
            new_floors.append(floor)
            if elevator_floor + elevator_move == i:
                for t, v in contents:
                    if t == 'gen':
                        new_floors[-1][0].append(v)
                    else:
                        new_floors[-1][1].append(v)
            elif elevator_floor == i:
                for t, v in contents:
                    if t == 'gen':
                        new_floors[-1][0].remove(v)
                    else:
                        new_floors[-1][1].remove(v)
        return [elevator_floor + elevator_move, new_floors]
    
    def get_state_hash(self, state):
        elevator, floors = state
        hash = [elevator]
        for floor in floors:
            hash.append((tuple(sorted(floor[0])), tuple(sorted(floor[1]))))
        return tuple(hash)
    
    def is_valid_move(self, move, floors):
        current, change, *contents = move
        current_gens, current_chips = deepcopy(floors[current])
        new_gens = current_gens[:]
        new_chips = current_chips[:]
        for t, v in contents:
            if t == 'gen':
                new_gens.remove(v)
            else:
                new_chips.remove(v)
        if not self.has_sufficient_shielding(new_gens, new_chips):
            return False
        to_gens, to_chips = floors[current + change]
        new_gens = to_gens[:]
        new_chips = to_chips[:]
        for t, v in contents:
            if t == 'gen':
                new_gens.append(v)
            else:
                new_chips.append(v)
        return self.has_sufficient_shielding(new_gens, new_chips)

    def has_sufficient_shielding(self, gens, chips):
        if len(gens) == 0:
            return True
        for chip_type in chips:
            if chip_type not in gens:
                return False
        return True
    
    def score_state(self, state):
        score = 0
        for i, floor in enumerate(state[1]):
            score += i * (len(floor[0]) + len(floor[1]))
        return score

def solve(inp, part, debug=False):
    # if part == 2:
    #     return None
    starting_state = format_input(inp)
    if part == 2 and not debug:
        starting_state[1][0][0].extend(('elerium', 'dilithium'))
        starting_state[1][0][1].extend(('elerium', 'dilithium'))
    floors = [[[], []]] * 3
    floors.append([[], []])
    for floor in starting_state[1]:
        for gen in floor[0]:
            floors[-1][0].append(gen)
        for chip in floor[1]:
            floors[-1][1].append(chip)
    solved_state = [3, floors]
    optimizer = ChipMover(starting_state, solved_state, states_to_keep = 25000)
    return optimizer.get_minimal_path()

def main(debug = False):
    s = ''
    try:
        for part in (1, 2):
            s += f'Part {part} example: {solve(parse_example(), part, True)}\n'
            s += f'Part {part} actual : {solve(parse_input(), part, debug)}\n'
    except:
        print(s)
        raise
    return s.rstrip()
