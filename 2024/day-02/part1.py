from ftplib import print_line

from report import Report

def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def create_reports(puzzle_input: [str]):
    reports = []
    for row in puzzle_input:
        levels = row.split(" ")
        reports.append(Report(levels=list(map(int, levels))))
        print(levels)
    return reports


if __name__ == '__main__':
    puzzle_input = get_input()
    reports = create_reports(puzzle_input=puzzle_input)
    number_of_safe_reports = 0
    for report in reports:
        if report.is_safe():
            number_of_safe_reports += 1
    print(f"There are {number_of_safe_reports} safe reports")
