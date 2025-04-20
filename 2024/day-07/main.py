from equation import Equation


def get_input() -> list[[str]]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")


def convert_input_to_equations(puzzle_input):
    equations = []
    for raw_equation in puzzle_input:
        test_value, equation_values = raw_equation.split(": ")
        test_value = int(test_value)
        equation_values = equation_values.strip().split(" ")
        equation_values = [int(x) for x in equation_values]
        print(f"Test value: {test_value} ... Equation values: {equation_values}")
        equations.append(Equation(test_value=test_value,
                                  values=equation_values))
    return equations


def filter_equations(equations: [Equation]) -> [Equation]:
    true_equations = []
    for equation in equations:
        if equation.is_true():
            true_equations.append(equation)
    return true_equations


def true_equations_test_value_sum(equations: [Equation]) -> int:
    total_value = 0
    for equation in equations:
        total_value += equation.test_value
    return total_value


def part_one_solution() -> int:
    puzzle_input = get_input()
    equations = convert_input_to_equations(puzzle_input=puzzle_input)
    true_equations = filter_equations(equations=equations)
    return true_equations_test_value_sum(equations=true_equations)


if __name__ == '__main__':
    print(part_one_solution())
