from word_search import WordSearch


def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


if __name__ == '__main__':
    puzzle_input = get_input()
    word_search = WordSearch(grid=puzzle_input, word_to_search_for="XMAS")
    print(word_search.number_of_occurrences())
