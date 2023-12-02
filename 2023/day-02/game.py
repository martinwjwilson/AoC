class Game:
    """
    A class to represent a game.
    A game has a list of rounds played.
    rounds is a list containing a rounds of a game, with each round being a dictionary.
    Each round has the name of colours and how many there were: {"red": 3, "blue": 4}
    """

    def __init__(self, game_number: int, rounds_string: str):
        self.rounds_string = rounds_string
        self.number = game_number
        self.rounds = []
        self.total_power = 0
        self.minimum_red = 0
        self.minimum_green = 0
        self.minimum_blue = 0
        self.__setup()

    # PUBLIC METHODS

    def is_valid(self, max_red: int, max_green: int, max_blue: int) -> bool:
        """
        Checks if a game is valid and returns the result.
        A game is valid if it doesn't use more cubes than are provided for each colour.
        :param max_red: The maximum number of red cubes available
        :param max_green:The maximum number of green cubes available
        :param max_blue: The maximum number of blue cubes available
        :return bool: Whether the game is valid or not
        """
        for current_round in self.rounds:
            if ("red" in current_round and
                    current_round["red"] > max_red):
                return False
            if ("green" in current_round and
                    current_round["green"] > max_green):
                return False
            if ("blue" in current_round and
                    current_round["blue"] > max_blue):
                return False
        return True

    # PRIVATE METHODS

    def __setup(self):
        self.__convert_rounds_string()
        self.__calculate_total_power()

    def __convert_rounds_string(self):
        """
        A method to convert the puzzle input string into valid format for the other methods to use.
        :return:
        """
        list_of_rounds = [x.strip() for x in self.rounds_string.split(';')]
        for current_round in list_of_rounds:
            current_round_squares = [x.strip() for x in current_round.split(',')]
            converted_squares = {}
            for square in current_round_squares:
                square_number, square_colour = square.split(" ")
                converted_squares[square_colour] = int(square_number)
            # After each round, add the dictionary of converted squares
            self.rounds.append(converted_squares)

    def __calculate_total_power(self):
        """
        A method to calculate the total power for a game.
        This is determined by the minimum required colours for a game multiplied together.
        :return:
        """
        self.__calculate_minimum_colours()
        self.total_power = self.minimum_red * self.minimum_green * self.minimum_blue

    def __calculate_minimum_colours(self):
        """
        A method to calculate and set the minimum number of cubes required for each colour.
        For example the minimum number of red cubes needed will be determined by the
        highest use in a round.
        :return:
        """
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
                    