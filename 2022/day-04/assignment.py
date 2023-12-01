class Assignment:
    def __init__(self, assignment_range: [int, int]):
        self.starting_section = assignment_range[0]
        self.ending_section = assignment_range[1]
        self.section_range = list(range(self.starting_section, self.ending_section + 1))

    def fully_contains(self, alternative_assignment_range) -> bool:
        return set(self.section_range).issuperset(set(alternative_assignment_range))

    def overlaps_at_all(self, alternative_assignment_range) -> bool:
        if set(self.section_range) & set(alternative_assignment_range):
            return True
        return False
