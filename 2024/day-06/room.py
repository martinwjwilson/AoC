from guard import Guard, Direction


class Room:
    def __init__(self, layout: [[str]], additional_obstacle_coordinates: tuple[int, int]=None):
        self.layout = layout
        self.guard = self.locate_guard()
        if additional_obstacle_coordinates is not None:
            self.add_additional_obstacle(row=additional_obstacle_coordinates[0],
                                         column=additional_obstacle_coordinates[1])

    def locate_guard(self) -> Guard:
        for row_index, row in enumerate(self.layout):
            for character_index, character in enumerate(row):
                if type(character) == Guard:
                    return character

    def add_guard_to_room(self):
        self.layout[self.guard.current_y][self.guard.current_x] = self.guard

    def add_additional_obstacle(self, row, column):
        self.layout[row][column] = "#"

    def calculate_guard_path(self):
        current_move = 0
        while True:
            print(f"Current move: {current_move}")
            print(f"Current layout:")
            for row in self.layout:
                print(row)
            print(" ")
            if self.guard_next_move_is_off_board():
                self.mark_current_position()
                return
            self.move_guard()
            current_move += 1

    def guard_next_move_is_off_board(self) -> bool:
        if self.guard.current_direction == Direction.NORTH:
            if self.guard.current_y == 0:
                return True
        if self.guard.current_direction == Direction.WEST:
            if self.guard.current_x == 0:
                return True
        if self.guard.current_direction == Direction.EAST:
            current_row = self.layout[self.guard.current_y]
            if self.guard.current_x == len(current_row) - 1:
                return True
        if self.guard.current_direction == Direction.SOUTH:
            if self.guard.current_y == len(self.layout) - 1:
                return True
        return False

    def move_guard(self):
        self.mark_current_position()
        if self.guard.current_direction == Direction.NORTH:
            if self.guard_next_position_is_clear():
                self.layout[self.guard.current_y - 1][self.guard.current_x] = self.guard
                self.guard.current_y = self.guard.current_y - 1
                self.guard.current_x = self.guard.current_x
            else:
                self.guard.rotate_clockwise()
                return
        if self.guard.current_direction == Direction.WEST:
            if self.guard_next_position_is_clear():
                self.layout[self.guard.current_y][self.guard.current_x - 1] = self.guard
                self.guard.current_y = self.guard.current_y
                self.guard.current_x = self.guard.current_x - 1
            else:
                self.guard.rotate_clockwise()
                return
        if self.guard.current_direction == Direction.EAST:
            if self.guard_next_position_is_clear():
                self.layout[self.guard.current_y][self.guard.current_x + 1] = self.guard
                self.guard.current_y = self.guard.current_y
                self.guard.current_x = self.guard.current_x + 1
            else:
                self.guard.rotate_clockwise()
                return
        if self.guard.current_direction == Direction.SOUTH:
            if self.guard_next_position_is_clear():
                self.layout[self.guard.current_y + 1][self.guard.current_x] = self.guard
                self.guard.current_y = self.guard.current_y + 1
                self.guard.current_x = self.guard.current_x
            else:
                self.guard.rotate_clockwise()
                return

    def guard_next_position_is_clear(self) -> bool:
        if self.guard.current_direction == Direction.NORTH:
            if self.layout[self.guard.current_y - 1][self.guard.current_x] != "#":
                return True
        if self.guard.current_direction == Direction.WEST:
            if self.layout[self.guard.current_y][self.guard.current_x - 1] != "#":
                return True
        if self.guard.current_direction == Direction.EAST:
            if self.layout[self.guard.current_y][self.guard.current_x + 1] != "#":
                return True
        if self.guard.current_direction == Direction.SOUTH:
            if self.layout[self.guard.current_y + 1][self.guard.current_x] != "#":
                return True
        return False

    def mark_current_position(self):
        self.layout[self.guard.current_y][self.guard.current_x] = "X"

    def contains_infinite_loop(self) -> bool:
        current_move = 0
        while current_move < 80000:
            if self.guard_next_move_is_off_board():
                self.mark_current_position()
                return False
            self.move_guard()
            current_move += 1
        return True
