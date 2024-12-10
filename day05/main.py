from copy import deepcopy
FILE_PATH = 'data.txt'

def read_data(file_path):
    initial = []
    instructions = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('move'):
                instructions.append(line.strip())
            elif line.startswith('['):
                for stack_number, i in enumerate(range(0, len(line), 4)):
                    cargo = line[i+1]
                    if stack_number >= len(initial):
                        initial.append([])

                    if cargo == ' ':
                        continue
                    initial[stack_number].insert(0, cargo)


    return initial, instructions


def try_get_index(list, index):
    try:
        return list[index]
    except IndexError:
        return None



class CargoArea:
    def __init__(self, initial_state=[]):
        self.stacks = deepcopy(initial_state)

    def __str__(self):
        max_cargo_height = max((len(stack) for stack in self.stacks))
        result = []
        for index in range(max_cargo_height, -1, -1):
            row_data = (try_get_index(stack, index) for stack in self.stacks)
            result.append(' '.join([f'[{cargo}]' if cargo else '   ' for cargo in row_data]))

        result.append(' '.join([f' {i+1} ' for i in range(len(self.stacks))]))
        return '\n'.join(result)
        

    def move(self, instruction, multimover=False):
        _, amount, _, from_stack, _, to_stack = instruction.split()
        amount = int(amount)
        from_stack = int(from_stack) - 1
        to_stack = int(to_stack) - 1
        stack = self.stacks[from_stack]
        if multimover:
            self.stacks[to_stack].extend(stack[-amount:])
        else:
            self.stacks[to_stack].extend(stack[:-amount-1:-1])
        self.stacks[from_stack] = stack[:-amount]

    def get_top_stack_word(self):
        return ''.join([stack[-1] for stack in self.stacks])

initial_state, instructions = read_data(FILE_PATH)

# Part 1
cargo_area = CargoArea(initial_state)
print(cargo_area)
for instruction in instructions:
    cargo_area.move(instruction)
print(cargo_area)
print(cargo_area.get_top_stack_word())

# Part 2
cargo_area = CargoArea(initial_state)
print(cargo_area)
for instruction in instructions:
    cargo_area.move(instruction, True)
print(cargo_area)
print(cargo_area.get_top_stack_word())