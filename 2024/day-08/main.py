from city_map import CityMap


def get_input() -> list[[str]]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def part_one_solution() -> int:
    puzzle_input = get_input()
    city_map = CityMap(map_layout=puzzle_input)


if __name__ == '__main__':
    print(part_one_solution())
