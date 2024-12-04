def get_input() -> list[str]:
    # get the input from the file
    f = open('test_input.txt', 'r')
    content = f.read()
    return content.split("\n")


def clean_puzzle_input(puzzle_input: [str]):
    return


if __name__ == '__main__':
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
