FILEPATH = "data/day08-1_input.txt"

MOVES = {
    'jmp': lambda position, param: (position + param, 0),
    'nop': lambda position, param: (position + 1, 0),
    'acc': lambda position, param: (position + 1, param)
}

FIXES = {
    'jmp': 'nop',
    'nop': 'jmp'
}


def run_code(a_code: list) -> int:
    current_position = 0
    visited_positions = {0}
    accumulation = 0
    while current_position < len(a_code):
        current_position, value = run_instruction_at(a_code, current_position)
        if current_position in visited_positions:
            return None
        visited_positions.add(current_position)
        accumulation += value
    return accumulation


def run_instruction_at(a_code: list, position: int) -> (int, int):
    current_instruction, current_value = a_code[position]
    return MOVES[current_instruction](position, current_value)


def mute_code(a_program: list) -> list:
    for index, (instruction, value) in enumerate(a_program):
        if instruction in ('jmp', 'nop'):
            yield a_program[:index] + [(FIXES[instruction], value)] + a_program[index + 1:]


program = [(line.strip().split()[0], int(line.strip().split()[1])) for line in open(FILEPATH, 'r').readlines()]

for code in mute_code(program):
    if acc := run_code(code):
        print(acc)
