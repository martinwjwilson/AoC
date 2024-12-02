class Report:
    def __init__(self, levels: [int]):
        self.levels = levels

    def is_safe(self) -> bool:
        return self.all_levels_are_increasing_safely() or self.all_levels_are_decreasing_safely()

    def all_levels_are_increasing_safely(self) -> bool:
        for index, level in enumerate(self.levels):
            if index > 0:
                if level <= self.levels[index - 1] or not (0 < abs(level - self.levels[index - 1]) < 4):
                    return False
        return True

    def all_levels_are_decreasing_safely(self) -> bool:
        for index, level in enumerate(self.levels):
            if index > 0:
                if level >= self.levels[index - 1] or not (0 < abs(level - self.levels[index - 1]) < 4):
                    return False
        return True
