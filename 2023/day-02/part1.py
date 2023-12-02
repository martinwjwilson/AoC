from game import Game

# highest valid cube numbers
highest_red = 12
highest_green = 13
highest_blue = 14

# get the input from the file
f = open('input.txt', 'r')
content = f.read()
input_lines = content.split("\n")

# turn each line into a game
games = []
for count, line in enumerate(input_lines, start=1):
    input_string = line.split(":")[1].strip()
    game = Game(game_number=count, rounds_string=input_string)
    game.convert_input_string()
    games.append(game)

# check which games are valid and add their numbers together
total_game_numbers = 0
for game in games:
    if game.is_valid(max_red=highest_red, max_green=highest_green, max_blue=highest_blue):
        total_game_numbers += game.number

print(f"The final number is: {total_game_numbers}")
