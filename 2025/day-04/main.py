grid_width = 0
grid_height = 0

def get_input():
    f = open("input.txt", "r")
    content = f.read()
    return content.split("\n")

def element_is_in_corner(_row_index, _element_index):
    return ((_row_index == 0 and _element_index == 0) or # top left
            (_row_index == 0 and _element_index == grid_width-1) or # top right
            (_row_index == grid_height-1 and _element_index == 0) or # bottom left
            (_row_index == grid_height-1 and _element_index == grid_width-1)) # bottom right

def roll_can_be_accessed(row_index, element_index, puzzle_input):
    pass

def get_sub_array_above():
    pass

def get_sub_array_middle():
    pass

def get_sub_array_below():
    pass

if __name__=="__main__":
    puzzle_input = get_input()
    grid_width = len(puzzle_input[0])
    grid_height = len(puzzle_input)
    number_of_accessible_rolls = 4
    for row_index, current_row in enumerate(puzzle_input):
        for element_index, element in enumerate(current_row):
            # Skip the corners as they automatically pass
            if element_is_in_corner(row_index, element_index):
                continue

            if roll_can_be_accessed(row_index, element_index, puzzle_input):
                number_of_accessible_rolls += 1