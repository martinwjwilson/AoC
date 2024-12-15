from enum import Enum


class Guard:
    def __init__(self, starting_position: [int], starting_direction: str):
        self.current_x = starting_position[0]
        self.current_y = starting_position[1]
        self.current_direction = Direction(starting_direction)

    def rotate_clockwise(self):
        match self.current_direction:
            case Direction.NORTH:
                self.current_direction = Direction.EAST
            case Direction.EAST:
                self.current_direction = Direction.SOUTH
            case Direction.SOUTH:
                self.current_direction = Direction.WEST
            case Direction.WEST:
                self.current_direction = Direction.NORTH


class Direction(Enum):
    NORTH = "^"
    EAST = ">"
    SOUTH = "v"
    WEST = "<"
