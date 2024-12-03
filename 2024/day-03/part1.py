from instruction import Instruction

def get_input() -> list[str]:
    # get the input from the file
    f = open('input.txt', 'r')
    content = f.read()
    return content.split("\n")

def clean_puzzle_input(puzzle_input: [str]):
    final_puzzle_input = ""
    for line in puzzle_input:
        final_puzzle_input += line
    return final_puzzle_input


if __name__ == '__main__':
    puzzle_input = get_input()
    cleaned_puzzle_input = clean_puzzle_input(puzzle_input=puzzle_input)
    instruction = Instruction(raw_instruction=cleaned_puzzle_input)
    sum_of_all_multiplications = instruction.sum_of_all_multiplications()
    print(sum_of_all_multiplications)
