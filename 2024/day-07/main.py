from equation import Equation


def get_input() -> list[[str]]:
    # get the input from the file
    f = open('test_input.txt', 'r')
    content = f.read()
    return content.split("\n")


def part_one_solution() -> int:
    puzzle_input = get_input()
    print(puzzle_input)
    equations = []
    for raw_equation in puzzle_input:
        test_value, equation_values = raw_equation.split(": ")
        test_value = int(test_value)
        equation_values = equation_values.strip().split(" ")
        equation_values = [int(x) for x in equation_values]
        print(f"Test value: {test_value} ... Equation values: {equation_values}")
        equations.append(Equation(test_value=test_value,
                                  values=equation_values))
    return 0


if __name__ == '__main__':
    print(part_one_solution())
