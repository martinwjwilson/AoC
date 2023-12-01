class Tree:
    def __init__(self, height: int, x_coordinate, y_coordinate):
        self.height = height
        self.x = x_coordinate
        self.y = y_coordinate
        self.scenic_score = 0

    def set_scenic_score(self, n, s, e, w):
        self.scenic_score = n * s * e * w
