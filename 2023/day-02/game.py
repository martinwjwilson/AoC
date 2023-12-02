class Game:
    def __init__(self, game_number: int, rounds_string: str):
        self.rounds_string = rounds_string
        self.number = game_number
        self.rounds = []
        self.minimum_red = 0
        self.minimum_green = 0
        self.minimum_blue = 0

    def convert_input_string(self):
        print(f"The string for game {self.number}: {self.rounds_string}")
        list_of_rounds = [x.strip() for x in self.rounds_string.split(';')]
        for current_round in list_of_rounds:
            current_round_squares = [x.strip() for x in current_round.split(',')]
            converted_squares = {}
            for square in current_round_squares:
                square_number, square_colour = square.split(" ")
                converted_squares[square_colour] = int(square_number)
            # After each round, add the dictionary of converted squares
            self.rounds.append(converted_squares)

    def is_valid(self, max_red: int, max_green: int, max_blue: int) -> bool:
        for current_round in self.rounds:
            if "red" in current_round:
                if current_round["red"] > max_red:
                    return False
            if "green" in current_round:
                if current_round["green"] > max_green:
                    return False
            if "blue" in current_round:
                if current_round["blue"] > max_blue:
                    return False
        return True

    def calculate_total_power(self) -> int:
        self.__calculate_minimum_colours()
        print(f"{self.minimum_red} {self.minimum_green} {self.minimum_blue}")
        return self.minimum_red * self.minimum_green * self.minimum_blue

    def __calculate_minimum_colours(self):
        for current_round in self.rounds:
            if "red" in current_round:
                if current_round["red"] > self.minimum_red:
                    self.minimum_red = current_round["red"]
            if "green" in current_round:
                if current_round["green"] > self.minimum_green:
                    self.minimum_green = current_round["green"]
            if "blue" in current_round:
                if current_round["blue"] > self.minimum_blue:
                    self.minimum_blue = current_round["blue"]
