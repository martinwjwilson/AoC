class Ship:
    def __init__(self, crates):
        self.crates = crates

    def move_individually(self, number_of_crates_to_move: int, from_stack: int, to_stack: int):
        for _ in range(number_of_crates_to_move):
            crate = self.crates[from_stack-1].pop()
            self.crates[to_stack-1].append(crate)

    def move_groups(self, number_of_crates_to_move: int, from_stack: int, to_stack: int):
        from_stack_index = from_stack - 1
        to_stack_index = to_stack - 1
        crates_to_add = self.crates[from_stack_index][-number_of_crates_to_move:]
        for crate in crates_to_add:
            self.crates[to_stack_index].append(crate)
        for _ in range(number_of_crates_to_move):
            self.crates[from_stack_index].pop()

    def get_top_crate_letters(self) -> str:
        final_string = ""
        for section in self.crates:
            final_string += section[-1].letter
        return final_string
