class Choice:
    def __init__(self, wins_against, loses_against, value):
        self.wins_against = wins_against
        self.loses_against = loses_against
        self.value = value


class Rock(Choice):
    def __init__(self):
        super().__init__(Scissors, Paper, 1)


class Paper(Choice):
    def __init__(self):
        super().__init__(Rock, Scissors, 2)


class Scissors(Choice):
    def __init__(self):
        super().__init__(Paper, Rock, 3)


def calculate_round_winner(your_choice: Choice, opponent_choice: Choice):
    if type(your_choice) == type(opponent_choice):
        return outcome_values["draw"]
    elif your_choice.wins_against == type(opponent_choice):
        return outcome_values["win"]
    elif your_choice.loses_against == type(opponent_choice):
        return outcome_values["loss"]


def calculate_your_choice(opponent_choice: Choice, outcome: str) -> Choice:
    if outcome == "Lose":
        return opponent_choice.wins_against()
    if outcome == "Draw":
        return opponent_choice
    if outcome == "Win":
        return opponent_choice.loses_against()


def convert_moves(choice: str) -> Choice:
    if choice in ("A", "X"):
        return Rock()
    elif choice in ("B", "Y"):
        return Paper()
    return Scissors()


def convert_to_outcome(letter: str) -> str:
    if letter == "X":
        return "Lose"
    if letter == "Y":
        return "Draw"
    return "Win"


# Constants
outcome_values = {"loss": 0,
                  "draw": 3,
                  "win": 6}

# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
list_of_rounds = content.split("\n")

total_score = 0
for current_round in list_of_rounds:
    expected_outcome = convert_to_outcome(current_round[2])
    opponent_choice = convert_moves(current_round[0])
    your_choice = calculate_your_choice(opponent_choice, expected_outcome)
    total_score += (calculate_round_winner(your_choice, opponent_choice) + your_choice.value)

print(total_score)
