from enum import Enum

class Guard:
    def __init__(self, starting_position: [int], starting_direction: str):
        self.current_x = starting_position[0]
        self.current_y = starting_position[1]
        self.current_direction = starting_direction

    def rotate_clockwise(self):
        current_direction = self.current_direction
        match current_direction:
            case Direction.NORTH.value:
                self.current_direction = Direction.EAST.value
            case Direction.EAST.value:
                self.current_direction = Direction.SOUTH.value
            case Direction.SOUTH.value:
                self.current_direction = Direction.WEST.value
            case Direction.WEST.value:
                self.current_direction = Direction.NORTH.value


class Direction(Enum):
    NORTH = "^"
    EAST = ">"
    SOUTH = "v"
    WEST = "<"
