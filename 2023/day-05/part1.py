from map import Map, MapRow
from seed import Seed


def get_input() -> list[str]:
    # get the input from the file
    f = open('test_input.txt', 'r')
    content = f.read()
    return content.split("\n")


def get_list_of_seeds(seed_input: [str]) -> list[Seed]:
    _list_of_seeds = []
    for seed_number in seed_input:
        _list_of_seeds.append(Seed(number=int(seed_number)))
    return _list_of_seeds


def get_list_of_maps(map_input: [str]) -> list[Map]:
    # remove empty lines from the input
    map_input = list(filter(None, map_input))
    print(map_input)
    _list_of_maps = []
    _current_map = None
    for i, m in enumerate(map_input):
        if m[0].isdigit():
            map_row = create_map_row(m)
            if not _current_map:
                _current_map = Map()
                _current_map.rows.append(map_row)
            if i != len(map_input) - 1:  # if it's the last line
                continue
        # if it's not a digit, or if it was, but it's the last line, add the map to the list
        if _current_map:  # make sure it's not None
            _list_of_maps.append(_current_map)
            _current_map = None
    return _list_of_maps


def create_map_row(map_input: str) -> MapRow:
    destination_range_start, source_range_start, range_length = map_input.split(' ')
    return MapRow(destination_range_start=destination_range_start,
                  source_range_start=source_range_start,
                  range_length=range_length)


def get_lowest_seed_number(seed_input, map_input) -> int:
    return 0


if __name__ == '__main__':
    puzzle_input = get_input()
    puzzle_input_seeds = puzzle_input[0:1][0].split(": ")[1].split()
    puzzle_input_maps = puzzle_input[2:]
    # get list of seeds
    seeds = get_list_of_seeds(seed_input=puzzle_input_seeds)
    # get list of maps
    maps = get_list_of_maps(map_input=puzzle_input_maps)
    # get the lowest seed number
    lowest_seed_number = get_lowest_seed_number(seed_input=seeds, map_input=maps)
    print(f"The lowest number is: {lowest_seed_number}")
