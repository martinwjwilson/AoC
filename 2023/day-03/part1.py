# get the input from the file
f = open('input.txt', 'r')
content = f.read()
engine_schematic = content.split("\n")


def is_number_touching_symbol(x_coordinate: int, y_coordinate: int) -> bool:
    # check above
    if y_coordinate > 0:
        row_above = engine_schematic[y_coordinate - 1]
        if is_symbol_in_range(row_above, x_coordinate):
            return True
    # check current row
    current_row = engine_schematic[y_coordinate]
    if is_symbol_in_range(current_row, x_coordinate):
        return True
    # check row below
    if y_coordinate < len(engine_schematic) - 1:  # -1 here because the length is 10 but y coordinate has to be < 9
        row_below = engine_schematic[y_coordinate + 1]
        if is_symbol_in_range(row_below, x_coordinate):
            return True
    return False


def is_symbol_in_range(row: str, x_coordinate) -> bool:
    x_from = x_coordinate - 1
    x_to = x_coordinate + 1
    if x_from < 0:
        x_from = x_coordinate
    if x_to > len(row) - 1:
        x_to = x_coordinate
    for i in range(x_from, x_to + 1):
        if not row[i].isdigit() and row[i] != ".":
            return True
    return False


part_numbers_touching_symbols = 0
for line_number, line in enumerate(engine_schematic):
    current_part_number = ""
    current_part_is_touching_symbol = False
    for character_number, character in enumerate(line):
        if character.isdigit():
            current_part_number += character
            if is_number_touching_symbol(x_coordinate=character_number, y_coordinate=line_number):
                current_part_is_touching_symbol = True
            # if it's the last character in a line we want to end here
            if character_number == (len(line) - 1):
                if current_part_is_touching_symbol:
                    part_numbers_touching_symbols += int(current_part_number)
                    print(f"The total part numbers is: {part_numbers_touching_symbols} and the number just added was {current_part_number}")
                break
        # if it's a period or a symbol and was touching a symbol
        # add the number and reset for next number
        else:
            if current_part_is_touching_symbol:
                part_numbers_touching_symbols += int(current_part_number)
                print(f"The total part numbers is: {part_numbers_touching_symbols} and the number just added was {current_part_number}")
            current_part_number = ""
            current_part_is_touching_symbol = False
print(f"The total is: {part_numbers_touching_symbols}")
# line 1 total is 4358
# line 2 total is 1845
# total should be 6203
