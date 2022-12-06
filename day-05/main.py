from move import Move
from crate import Crate
from ship import Ship

from copy import deepcopy

# Split up containers and moves
f = open("input.txt")
content = f.read().split("\n")
list_of_crate_input = []
list_of_move_input = []
content_section = "crates"
for line in content:
    if line == '':
        content_section = "moves"
        continue
    if content_section == "crates":
        list_of_crate_input.append(line)
    else:
        list_of_move_input.append(line)

# create a list of crates
# This could be made better by just stripping all the brackets and then turning the string into a list?
# Could I also remove the spaces but not the blank characters? I need some blanks to tell where there aren't crates
# Can you append but to the start of a list instead to remove the need for reversing?
crates = [[] for _ in range(len(list_of_crate_input))]
row_index = 0
for crate_string in list_of_crate_input:
    stack_string_index = 1  # 1 to skip the first bracket
    current_stack_index = 0
    # don't add the numbers under the stacks
    if row_index == len(list_of_crate_input) - 1:
        break
    while stack_string_index < len(crate_string):
        if crate_string[stack_string_index] != " ":
            crates[current_stack_index].append(Crate(crate_string[stack_string_index]))
        stack_string_index += 4
        current_stack_index += 1
    row_index += 1
temp_crates = []
for stack in crates:
    stack.reverse()
    temp_crates.append(stack)
crates = temp_crates

# create a list of moves
moves = []
for move_string in list_of_move_input:
    split_movement_string = move_string.split(" ")
    moves.append(Move(int(split_movement_string[1]),
                      int(split_movement_string[3]),
                      int(split_movement_string[5])))


def move_containers(ship, movement_type: str, moves_to_execute: [Move]):
    for movement in moves_to_execute:
        if movement_type == "individual":
            ship.move_individually(movement.number_of_movements,
                                   movement.from_stack,
                                   movement.to_stack)
        else:
            ship.move_groups(movement.number_of_movements,
                             movement.from_stack,
                             movement.to_stack)


if __name__ == '__main__':
    # create the ships
    first_ship = Ship(deepcopy(crates))
    second_ship = Ship(deepcopy(crates))

    # show the answers
    # move all the containers for ship 1
    print(second_ship.crates[0])
    move_containers(first_ship, "individual", moves)
    print(first_ship.crates[0])
    print(second_ship.crates[0])
    answer_1 = first_ship.get_top_crate_letters()
    # move all the containers for ship 2
    move_containers(second_ship, "multiple", moves)
    answer_2 = second_ship.get_top_crate_letters()

    print(f"The answer for part 1: {answer_1}")
    print(f"The answer for part 2: {answer_2}")
