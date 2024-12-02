from calendar import different_locale
from itertools import count


class Report:
    def __init__(self, levels: [int]):
        self.levels = levels

    def is_safe(self) -> bool:
        return (self.all_levels_are_increasing_safely(levels=self.levels.copy(), is_a_retest=False)
                or self.all_levels_are_decreasing_safely(levels=self.levels.copy(), is_a_retest=False))

    def all_levels_are_increasing_safely(self, levels: [int], is_a_retest: bool) -> bool:
        for index, level in enumerate(levels):
            previous_level = levels[index-1]
            if index > 0:
                if (level <= previous_level
                        or not self.difference_in_levels_is_safe(first_level=level,
                                                                 second_level=previous_level)):
                    if is_a_retest:
                        return False
                    else:
                        if index != len(levels) - 1:
                            levels.pop(index-1)
                            return self.all_levels_are_increasing_safely(levels=levels, is_a_retest=True)
        return True

    def all_levels_are_decreasing_safely(self, levels: [int], is_a_retest: bool) -> bool:
        for index, level in enumerate(levels):
            previous_level = levels[index-1]
            if index > 0:
                if (level >= previous_level
                        or not self.difference_in_levels_is_safe(first_level=level,
                                                                 second_level=previous_level)):
                    if is_a_retest:
                        return False
                    else:
                        if index != len(levels) - 1:
                            levels.pop(index)
                            return self.all_levels_are_decreasing_safely(levels=levels, is_a_retest=True)
        return True

    @staticmethod
    def difference_in_levels_is_safe(first_level: int, second_level: int) -> bool:
        # print(f"first level: {first_level} minus {second_level}: {0 < abs(first_level - second_level) < 4}")
        return 0 < abs(first_level - second_level) < 4
