from gear import Gear
from engine_part import EnginePart

# get the input from the file
f = open('input.txt', 'r')
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
                # + 2 because the length the len() is one more than the index, and another one to check the next one
                if character_number + 1 == len(line) or not line[character_number + 1].isdigit():
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


def validate_gears(gears_to_validate: list[Gear], engine_parts_to_validate: list[EnginePart]) -> list[Gear]:
    """
    For each gear, check if any of the engine parts are touching it.
    If exactly 2 are, their numbers are multiplied to make the gear's power
    :param gears_to_validate:
    :param engine_parts_to_validate:
    :return:
    """
    validated_gears = []
    for gear in gears_to_validate:
        number_of_touching_parts = 0
        potential_power = []
        for engine_part in engine_parts_to_validate:
            if gear_is_touching_engine_part(gear=gear,
                                            engine_part=engine_part):
                number_of_touching_parts += 1
                potential_power.append(engine_part.value)
        print(f"The number of touching parts for this gear is {number_of_touching_parts}")
        if number_of_touching_parts == 2:
            gear.value = potential_power[0] * potential_power[1]
            validated_gears.append(gear)
    return validated_gears


def gear_is_touching_engine_part(gear: Gear, engine_part: EnginePart) -> bool:
    y_in_range = gear.y_coordinate in range(engine_part.y_coordinate - 1, engine_part.y_coordinate + 2)
    x_in_range = gear.x_coordinate in range(engine_part.x_start - 1, engine_part.x_end + 2)
    print(f"gear y = {gear.y_coordinate}\nengine y range = {engine_part.y_coordinate - 1} to "
          f"{engine_part.y_coordinate + 1}. Y in range {y_in_range}")
    print(f"gear x = {gear.x_coordinate}\nengine x range = {engine_part.x_start} to "
          f"{engine_part.x_end}. X in range {x_in_range}\n")
    return y_in_range and x_in_range


if __name__ == '__main__':
    potential_gears = create_list_of_potential_gears()
    print(f"There are {len(potential_gears)} potential gears")
    potential_engine_parts = create_list_of_engine_parts()
    print(f"There are {len(potential_engine_parts)} engine parts")
    validated_gears = validate_gears(gears_to_validate=potential_gears,
                                     engine_parts_to_validate=potential_engine_parts)
    print(f"There are {len(validated_gears)} validated gears")
    # get the sum
    total = 0
    for gear in validated_gears:
        print(f"The gear value is {gear.value}")
        total += gear.value
    print(f"The total: {total}")
    # 75225693 too low
    # 76314915
