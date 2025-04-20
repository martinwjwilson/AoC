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


def calculate_the_magic_number(left_side_input, right_side_input: [str]) -> int:
    magic_number = 0
    for element in left_side_input:
        number_of_occurences = 0
        for right_element in right_side_input:
            if element == right_element:
                number_of_occurences += 1
        magic_number += number_of_occurences * int(element)
    return magic_number


if __name__ == '__main__':
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
    magic_number = calculate_the_magic_number(left_side_input=cleaned_puzzle_input[0],
                                              right_side_input=cleaned_puzzle_input[1])
    print(magic_number)
