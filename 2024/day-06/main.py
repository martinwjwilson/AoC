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


def create_room(room_input: [[str]]) -> Room:
    # Use this method in future if a Room class gets used
    room_input = add_guard_to_room(room_input=room_input)
    room = Room(layout=room_input)
    return room


def add_guard_to_room(room_input: [[str]]) -> [any]:
    for row_index, row in enumerate(room_input):
        for character_index, character in enumerate(row):
            if character in ("<", "^", ">", "v"):
                room_input[row_index][character_index] = Guard(starting_position=[character_index, row_index],
                                                               starting_direction=character)
                break
    return room_input


def count_guard_positions(room: Room) -> int:
    number_of_positions_touched = 0
    for row in room.layout:
        for character in row:
            if character == "X":
                number_of_positions_touched += 1
    return number_of_positions_touched


def part_one_solution() -> int:
    puzzle_input = get_input()
    room = create_room(room_input=puzzle_input)
    room.calculate_guard_path()
    return count_guard_positions(room=room)


def part_two_solution() -> int:
    puzzle_input = get_input()
    # Create a list of rooms with every possible new obstacle location
    all_rooms = []
    for row_index, row in enumerate(puzzle_input):
        for character_index, character in enumerate(row):
            if character == ".":
                print(f"Current layout before append:")
                for roww in puzzle_input:
                    print(roww)
                new_room = create_room(room_input=puzzle_input)
                new_room.layout[character_index][row_index] = "#"
                all_rooms.append(new_room)
                print(f"Current layout after append:")
                for rowww in puzzle_input:
                    print(rowww)
                print(" ")
    number_of_looping_rooms = 0
    for room in all_rooms:
        pass
        # Check if room causes a loop
        # if room.contains_infinite_loop():
        #     number_of_looping_rooms += 1

    return number_of_looping_rooms


if __name__ == '__main__':
    # Try using match case statements
    # print(part_one_solution())
    print(part_two_solution())
