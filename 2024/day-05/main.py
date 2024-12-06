from page_ordering_rule import PageOrderingRule

def get_input() -> list[str]:
    # get the input from the file
    f = open('test_input.txt', 'r')
    content = f.read()
    return content.split("\n")

def clean_puzzle_input(puzzle_input: [str]) -> [[str]]:
    sorted_input = []
    temp_array = []
    for element in puzzle_input:
        if element == "":
            sorted_input.append(temp_array)
            temp_array = []
        else:
            temp_array.append(element)
    sorted_input.append(temp_array)
    return sorted_input

def create_all_page_ordering_rules(raw_page_ordering_rules: [str]) -> [PageOrderingRule]:
    _page_ordering_rules = []
    for rule in raw_page_ordering_rules:
        first_number, second_number = rule.split("|")
        _page_ordering_rules.append(PageOrderingRule(first_number=first_number,
                                                     second_number=second_number))
    return _page_ordering_rules


def part_one_solution():
    pass


if __name__ == '__main__':
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
    print(cleaned_puzzle_input)
    page_ordering_rules = create_all_page_ordering_rules(cleaned_puzzle_input[0])

