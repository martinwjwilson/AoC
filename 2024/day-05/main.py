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
        _page_ordering_rules.append(PageOrderingRule(first_number=int(first_number),
                                                     second_number=int(second_number)))
    return _page_ordering_rules


def create_all_pages_updates(raw_page_updates):
    _all_page_updates = []
    for page_update in raw_page_updates:
        split_page_numbers = page_update.split(",")
        split_page_numbers = [int(x) for x in split_page_numbers]
        _all_page_updates.append(split_page_numbers)
    return _all_page_updates


def part_one_solution() -> str:
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
    page_ordering_rules = create_all_page_ordering_rules(cleaned_puzzle_input[0])
    page_updates = create_all_pages_updates(raw_page_updates=cleaned_puzzle_input[1])
    correct_updates = get_all_correct_updates(ordering_rules=page_ordering_rules, page_updates=page_updates)
    return ""


def get_all_correct_updates(ordering_rules: [PageOrderingRule], page_updates: [[int]]) -> [[int]]:
    correct_updates = []
    for updates in page_updates:
        if
    return correct_updates


def page_update_is_correct(ordering_rules: [PageOrderingRule], page_updates: [int]) -> bool:
    # Go through each page and compare it against all the following pages to see if it follows all of the rules
    for index, page in enumerate(page_updates):

    return True


if __name__ == '__main__':
    print(part_one_solution())
