from guard import Guard


class Room:
    def __init__(self, layout:[[str]]):
        self.layout = layout
        self.guard = Guard(starting_position=self.get_guard_starting_coordinates(),
                           starting_direction=self.get_guard_starting_direction())

    def get_guard_starting_coordinates(self) -> [int]:
        for row_index, row in enumerate(self.layout):
            for character_index, character in enumerate(row):
                if character in ("<", "^", ">", "v"):
                    return [character_index, row_index]

    def get_guard_starting_direction(self) -> str:
        for row_index, row in enumerate(self.layout):
            for character_index, character in enumerate(row):
                if character in ("<", "^", ">", "v"):
                    return character

    def add_guard_to_room(self):
        self.layout[self.guard.current_y][self.guard.current_x] = self.guard
