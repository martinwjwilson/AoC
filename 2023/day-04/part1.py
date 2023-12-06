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


if __name__ == '__main__':
    raw_scratchies = get_input()
    sorted_scratchies = sort_scratchies(scratchies_to_sort=raw_scratchies)
    total_points = 0
    for card in sorted_scratchies:
        total_points += card.value
    print(f"The total is: {total_points}")
