class Scratchie:
    def __init__(self, winning_numbers: list[int], numbers_on_card: list[int]):
        self.value = 0
        self.winning_numbers = winning_numbers
        self.numbers_on_card = numbers_on_card
        self.__calculate_value()

    def __calculate_value(self):
        total = 0
        for i in self.numbers_on_card:
            if i in self.winning_numbers:
                if total == 0:
                    total = 1
                else:
                    total = total * 2
        self.value = total
