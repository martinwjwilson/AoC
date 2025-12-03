class Instruction:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

def get_input() -> list[str]:
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")

def process_input(_instructions):
    processed_instructions = []
    for instruction in _instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        processed_instructions.append(Instruction(direction, distance))
    return processed_instructions

def process_instruction(instruction, dial_position):
    hits, new_pos = count_zero_hits(dial_position, instruction.direction, instruction.distance)
    return new_pos, hits

def count_zero_hits(start_pos, direction, distance):
    inc = 1 if direction == "R" else -1
    pos = start_pos
    hits = 0

    for _ in range(distance):
        pos = (pos + inc) % 100
        if pos == 0:
            hits += 1

    return hits, pos

def handle_overturn(combination_value):
    times_passed_zero = 0
    while combination_value < 0 or combination_value > 99:
        if combination_value < 0:
            combination_value = combination_value + 100
            times_passed_zero += 1
        elif combination_value > 99:
            combination_value = combination_value - 100
            times_passed_zero += 1
    return combination_value, times_passed_zero

def part_one_solution(_instructions, dial_position):
    times_pointing_at_zero = 0
    for instruction in _instructions:
        new_pos, hits = process_instruction(instruction, dial_position)
        times_pointing_at_zero += hits
        dial_position = new_pos
    return times_pointing_at_zero

if __name__ == "__main__":
    initial_dial_position = 50
    unfiltered_input = get_input()
    instructions = process_input(unfiltered_input)
    final_dial_position = part_one_solution(instructions, initial_dial_position)
    print(f"The final password: {final_dial_position}")
