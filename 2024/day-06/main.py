from guard import Guard
from room import Room


def get_input() -> list[[str]]:
    # get the input from the file
    f = open('test_input.txt', 'r')
    content = f.read()
    content = content.split("\n")
    cleaned_content = []
    for row in content:
        cleaned_content.append(list(row))
    return cleaned_content


def create_room(room_input: [[str]]) -> [[str]]:
    # Use this method in future if a Room class gets used
    room_input = add_guard_to_room(room_input=room_input)
    room = Room(layout=room_input)
    return room_input


def add_guard_to_room(room_input: [[str]]) -> [any]:
    for row_index, row in enumerate(room_input):
        for character_index, character in enumerate(row):
            if character in ("<", "^", ">", "v"):
                room_input[row_index][character_index] = Guard(starting_position=[character_index, row_index],
                                                               starting_direction=character)
                break
    return room_input


def calculate_guard_path(room: [[str]], guard: Guard) -> [[str]]:
    pass


def count_guard_positions(room: [[str]]) -> int:
    number_of_positions_touched = 0
    for row in room:
        for character in row:
            if character == "X":
                number_of_positions_touched += 1
    return number_of_positions_touched


def part_one_solution() -> int:
    puzzle_input = get_input()
    room = create_room(room_input=puzzle_input)
    calculate_guard_path(room=room)
    return count_guard_positions(room=room)


if __name__ == '__main__':
    # Try using match case statements
    print(part_one_solution())
