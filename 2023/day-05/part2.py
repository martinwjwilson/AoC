from map import Map, MapRow
from seed import Seed


def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def get_list_of_seeds(seed_input: [str]) -> dict:
    _list_of_seeds = {}
    i = 0
    while i < len(seed_input):
        _list_of_seeds[int(seed_input[i])] = int(seed_input[i + 1])
        i += 2
    return _list_of_seeds


def get_list_of_maps(map_input: [str]) -> list[Map]:
    # remove empty lines from the input
    map_input = list(filter(None, map_input))
    _list_of_maps = []
    _current_map = None
    for i, row in enumerate(map_input):
        if row[0].isdigit():
            map_row = create_map_row(row)
            # If there is no current map to append to, create one
            if not _current_map:
                _current_map = Map()
            _current_map.rows.append(map_row)
            if i != len(map_input) - 1:
                # if it's not the last line we want to check the next line rather than adding the map to the list
                continue
        # if it's not a digit, or if it was, but it's the last line, add the map to the list
        if _current_map:  # make sure it's not None
            _list_of_maps.append(_current_map)
            _current_map = None
    return _list_of_maps


def create_map_row(map_input: str) -> MapRow:
    destination_range_start, source_range_start, range_length = map_input.split(' ')
    return MapRow(destination_range_start=int(destination_range_start),
                  source_range_start=int(source_range_start),
                  range_length=int(range_length))


def get_lowest_seed_number(seed_input, map_input) -> int:
    """
    For each seed, we want to convert it through each map and keep track of the lowest number after conversion
    :param seed_input:
    :param map_input:
    :return:
    """
    current_lowest_seed_number = None
    for current_seed_key in seed_input:
        print(f"The current seed key is {current_seed_key}")
        i = current_seed_key
        while i < current_seed_key + seed_input[current_seed_key]:
            converted_seed_number = i
            # convert the seed through each map
            for current_map in map_input:
                converted_seed_number = current_map.convert_number(input_number=converted_seed_number)
            # if the lowest seed number is none, then set it to the current converted seed
            if not current_lowest_seed_number:
                current_lowest_seed_number = converted_seed_number
            # else if the current seed number is lower than the lowest seed number, replace it
            if converted_seed_number < current_lowest_seed_number:
                current_lowest_seed_number = converted_seed_number
            i += 1
    return current_lowest_seed_number


if __name__ == '__main__':
    puzzle_input = get_input()
    puzzle_input_seeds = puzzle_input[0:1][0].split(": ")[1].split()
    puzzle_input_maps = puzzle_input[2:]
    # get list of seeds
    seed_ranges = get_list_of_seeds(seed_input=puzzle_input_seeds)
    # get list of maps
    maps = get_list_of_maps(map_input=puzzle_input_maps)
    # get the lowest seed number
    lowest_seed_number = get_lowest_seed_number(seed_input=seed_ranges, map_input=maps)
    print(f"The lowest number after conversion is: {lowest_seed_number}")
