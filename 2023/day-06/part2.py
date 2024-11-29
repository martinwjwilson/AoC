from race import Race


def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def create_race(race_input: list[str]) -> Race:
    # convert lists to a single number
    time_available = race_input[0].split()[1:]
    added_time = ""
    for i in time_available:
        added_time += i
    added_time = int(added_time)
    distance_available = race_input[1].split()[1:]
    added_distance = ""
    for i in distance_available:
        added_distance += i
    added_distance = int(added_distance)
    # Create the race
    return Race(time=added_time, distance=added_distance)


if __name__ == '__main__':
    # Get input
    puzzle_input = get_input()
    # Create a list of races
    race = create_race(race_input=puzzle_input)
    total = race.calculate_number_of_ways_to_win()
    print(f"The total is: {total}")
