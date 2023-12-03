class EnginePart:
    def __init__(self, x_start: int, x_end: int, y_coordinate: int):
        self.x_start = x_start
        self.x_end = x_end
        self.y_coordinate = y_coordinate

    def is_touching_symbol(self, symbol_x: int, symbol_y: int) -> bool:
        return True
