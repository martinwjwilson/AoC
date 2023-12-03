from gear import Gear
from engine_part import EnginePart

# get the input from the file
f = open('test_input.txt', 'r')
content = f.read()
engine_schematic = content.split("\n")


def create_list_of_potential_gears() -> list:
    gears = []
    # Create a list of numbers and gears
    for line_number, line in enumerate(engine_schematic):
        for character_number, character in enumerate(line):
            # Potential gear
            if character == "*":
                gear = Gear(x_coordinate=character_number, y_coordinate=line_number)
                gears.append(gear)
    return gears


def create_list_of_engine_parts() -> list[EnginePart]:
    engine_parts = []
    for line_number, line in enumerate(engine_schematic):
        creating_part = False
        current_part_number = ""
        current_part_start_coordinate = 0
        for character_number, character in enumerate(line):
            # Potential engine part
            if character.isdigit():
                current_part_number += character
                if not creating_part:
                    creating_part = True
                    current_part_start_coordinate = character_number
                # if the next character isn't a digit, or it's the end of the line, finalise the current part
                if (not line[character_number + 1].isdigit()) or character_number == len(line) - 1:
                    current_part_end_coordinate = character_number
                    engine_part = EnginePart(value=int(current_part_number),
                                             x_start=current_part_start_coordinate,
                                             x_end=current_part_end_coordinate,
                                             y_coordinate=line_number)
                    engine_parts.append(engine_part)
                    # reset for next part
                    creating_part = False
                    current_part_number = ""
                    current_part_start_coordinate = 0
    return engine_parts


if __name__ == '__main__':
    potential_gears = create_list_of_potential_gears()
    print(f"There are {len(potential_gears)} potential gears")
    potential_engine_parts = create_list_of_engine_parts()
    print(f"There are {len(potential_engine_parts)} engine parts")
