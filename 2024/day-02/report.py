class Report:
    def __init__(self, levels: [int]):
        self.levels = levels

    def is_safe(self) -> bool:
        return (self.levels_are_increasing_safely(levels=self.levels.copy())
                or self.levels_are_decreasing_safely(levels=self.levels.copy()))

    def levels_are_increasing_safely(self, levels: [int]) -> bool:
        levels_increased, index_failed_at = self.levels_increasing_in_order(levels=levels)
        safe_initial_distance = self.levels_increasing_with_safe_distance(levels=levels)
        if not levels_increased or not safe_initial_distance:
            levels_with_current_index_popped = levels.copy()
            levels_with_current_index_popped.pop(index_failed_at)
            levels_with_previous_index_popped = levels.copy()
            levels_with_previous_index_popped.pop(index_failed_at-1)
            increasing_with_current_pop = self.levels_increasing_in_order(levels=levels_with_current_index_popped)[0]
            increasing_with_previous_pop = self.levels_increasing_in_order(levels=levels_with_previous_index_popped)[0]
            print("hola")
            if increasing_with_current_pop:
                increasing_with_safe_distance = self.levels_increasing_with_safe_distance(
                    levels=levels_with_current_index_popped)
                if increasing_with_safe_distance:
                    return True
            if increasing_with_previous_pop:
                print("got here")
                increasing_with_safe_distance = self.levels_increasing_with_safe_distance(
                    levels=levels_with_previous_index_popped)
                if increasing_with_safe_distance:
                    return True
            return False
        return True

    def levels_are_decreasing_safely(self, levels: [int]) -> bool:
        levels_increased, index_failed_at = self.levels_decreasing_in_order(levels=levels)
        safe_initial_distance = self.levels_decreasing_with_safe_distance(levels=levels)
        if not levels_increased or not safe_initial_distance:
            levels_with_current_index_popped = levels.copy()
            levels_with_current_index_popped.pop(index_failed_at)
            levels_with_previous_index_popped = levels.copy()
            levels_with_previous_index_popped.pop(index_failed_at - 1)
            decreasing_with_current_pop = self.levels_decreasing_in_order(levels=levels_with_current_index_popped)[0]
            decreasing_with_previous_pop = self.levels_decreasing_in_order(levels=levels_with_previous_index_popped)[0]
            if decreasing_with_current_pop:
                decreasing_with_safe_distance = self.levels_decreasing_with_safe_distance(
                    levels=levels_with_current_index_popped)
                if decreasing_with_safe_distance:
                    return True
            if decreasing_with_previous_pop:
                decreasing_with_safe_distance = self.levels_decreasing_with_safe_distance(
                    levels=levels_with_previous_index_popped)
                if decreasing_with_safe_distance:
                    return True
            return False
        return True

    @staticmethod
    def levels_increasing_in_order(levels: [int]):
        for index, level in enumerate(levels):
            if index > 0:
                previous_level = levels[index-1]
                if level <= previous_level:
                    return False, index
        return True, 0

    @staticmethod
    def levels_decreasing_in_order(levels: [int]):
        for index, level in enumerate(levels):
            if index > 0:
                previous_level = levels[index-1]
                if level >= previous_level:
                    return False, index
        return True, 0

    def levels_increasing_with_safe_distance(self, levels: [int]) -> bool:
        for index, level in enumerate(levels):
            if index > 0:
                if not self.difference_in_levels_is_safe(first_level=level, second_level=levels[index-1]):
                    return False
        return True

    def levels_decreasing_with_safe_distance(self, levels: [int]) -> bool:
        for index, level in enumerate(levels):
            if index > 0:
                if not self.difference_in_levels_is_safe(first_level=level, second_level=levels[index-1]):
                    return False
        return True

    @staticmethod
    def difference_in_levels_is_safe(first_level: int, second_level: int) -> bool:
        return 0 < abs(first_level - second_level) < 4
