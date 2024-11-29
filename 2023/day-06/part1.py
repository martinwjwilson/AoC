from race import Race


def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def create_list_of_races(race_input: list[str]) -> list[Race]:
    times_list = [int(number) for number in race_input[0].split()[1:]]
    distance_list = [int(number) for number in race_input[1].split()[1:]]
    created_races = []
    for i in range(len(times_list)):
        created_races.append(Race(time=times_list[i], distance=distance_list[i]))
    return created_races


if __name__ == '__main__':
    # Get input
    puzzle_input = get_input()
    # Create a list of races
    races = create_list_of_races(race_input=puzzle_input)
    total = 0
    for race in races:
        number_of_ways_to_win = race.calculate_number_of_ways_to_win()
        if total:
            total *= number_of_ways_to_win
        else:
            total = number_of_ways_to_win
    print(f"The total is: {total}")
