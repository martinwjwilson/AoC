from scratchie import Scratchie


def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def sort_scratchies(scratchies_to_sort: list[str]) -> list[Scratchie]:
    scratchies = []
    for i in scratchies_to_sort:
        all_numbers = i.split(":")[1]
        winning_numbers, card_numbers = all_numbers.split("|")
        winning_numbers = [int(number) for number in winning_numbers.strip().split()]
        card_numbers = [int(number) for number in card_numbers.strip().split()]
        scratchies.append(Scratchie(winning_numbers=winning_numbers, numbers_on_card=card_numbers))
    return scratchies


def get_total_number_of_cards(sorted_cards: list[Scratchie]) -> int:
    total_number_of_cards = 0
    copies = []  # a list to take the number of copies from
    for card_number, card in enumerate(sorted_cards):
        # how many times the card should be checked
        number_of_times_to_check_card = 1
        if copies:
            print(f"The current popped element will be: {copies}")
            number_of_times_to_check_card += copies.pop(0)
        # the matches come from the original card multiplied by the amount of times it should be checked
        positions_to_add_to_list = card.number_of_matches() - len(copies)
        print(f"There should be {positions_to_add_to_list} positions added")
        print(f"The copies: {copies}\nnumber of times this card should be checked: {number_of_times_to_check_card}\n")
        # add missing positions
        for i in range(positions_to_add_to_list):
            copies.append(0)
        # add 1 to each copy
        for j in range(number_of_times_to_check_card):
            for k in range(card.number_of_matches()):
                copies[k] += 1
        total_number_of_cards += number_of_times_to_check_card
    return total_number_of_cards


if __name__ == '__main__':
    raw_scratchies = get_input()
    sorted_scratchies = sort_scratchies(scratchies_to_sort=raw_scratchies)
    total_cards = get_total_number_of_cards(sorted_scratchies)
    print(f"Total cards: {total_cards}")
