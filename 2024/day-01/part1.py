def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def clean_puzzle_input(puzzle_input: [str]):
    left_side_values = []
    right_side_values = []
    for row in puzzle_input:
        left_side, right_side = row.split("  ")
        left_side_values.append(left_side.strip())
        right_side_values.append(right_side.strip())
    left_side_values.sort()
    right_side_values.sort()
    return [left_side_values, right_side_values]


def calculate_difference_between_puzzle_sides(left_side_input, right_side_input):
    list_of_differences = []
    for x, element in enumerate(left_side_input):
        left_side_int = int(element)
        right_side_int = int(right_side_input[x])
        difference_between_elements = left_side_int - right_side_int
        list_of_differences.append(abs(difference_between_elements))
    return list_of_differences


if __name__ == '__main__':
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
    all_differences = calculate_difference_between_puzzle_sides(left_side_input=cleaned_puzzle_input[0],
                                                                right_side_input=cleaned_puzzle_input[1])
    print(sum(all_differences))
