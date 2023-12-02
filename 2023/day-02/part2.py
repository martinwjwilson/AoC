from game import Game

# get the input from the file
f = open('input.txt', 'r')
content = f.read()
input_lines = content.split("\n")

# turn each line into a game
games = []
for count, line in enumerate(input_lines, start=1):
    input_string = line.split(":")[1].strip()
    game = Game(game_number=count, rounds_string=input_string)
    games.append(game)

# calculate the total power
total_game_power = 0
for game in games:
    total_game_power += game.total_power

print(f"The final number is: {total_game_power}")
