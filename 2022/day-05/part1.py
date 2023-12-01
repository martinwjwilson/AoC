from move import Move
from crate import Crate
from ship import Ship

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

# create a ship
ship = Ship(crates)

# create a list of moves
moves = []
for move_string in list_of_move_input:
    split_movement_string = move_string.split(" ")
    moves.append(Move(int(split_movement_string[1]),
                      int(split_movement_string[3]),
                      int(split_movement_string[5])))

# move all the containers
for movement in moves:
    ship.move(movement.number_of_movements,
              movement.from_stack,
              movement.to_stack)

# get the answer
answer = ship.get_top_crate_letters()
print(answer)
