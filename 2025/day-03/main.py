class Bank:
    def __init__(self, batteries):
        self.batteries = batteries
        self.highest_joltage = self.get_highest_joltage()
        self.static_friction_joltage = self.get_highest_static_friction_joltage()

    def get_highest_joltage(self):
        highest_joltage = 0
        for index, joltage in enumerate(self.batteries):
            next_joltages = self.batteries[index+1:]
            for blah in next_joltages:
                new_temp_joltage = int(joltage + blah)
                if new_temp_joltage > highest_joltage:
                    highest_joltage = new_temp_joltage
        return highest_joltage

    def get_highest_static_friction_joltage(self):
        max_joltage = ""
        max_joltage_length = 12
        joltages_left = max_joltage_length - len(max_joltage)
        starting_index = 0
        for element in range(0, max_joltage_length):
            if joltages_left == 1:
                temp_array = self.batteries[starting_index:]
            else:
                temp_array = self.batteries[starting_index:-joltages_left + 1]
            highest_digit, digit_index = self.get_highest_digit_from_array(temp_array)
            max_joltage += highest_digit
            starting_index = starting_index + digit_index + 1
            joltages_left -= 1
        print(f"The max joltage is::: {max_joltage}")
        return int(max_joltage)

    # Returns the highest digit with the index it was from
    def get_highest_digit_from_array(self, array):
        print(array)
        highest_digit = 0
        digit_index = 0
        for index, element in enumerate(array):
            if int(element) > highest_digit:
                highest_digit = int(element)
                digit_index = index
        return str(highest_digit), digit_index

def get_input():
    f = open("input.txt", "r")
    content = f.read()
    return content.split("\n")

if __name__=="__main__":
    puzzle_input = get_input()
    banks = []
    for current_input in puzzle_input:
        banks.append(Bank(batteries=current_input))
    all_highest_joltages = []
    for bank in banks:
        blah = bank.static_friction_joltage
        all_highest_joltages.append(blah)
        print(f"Max voltage = {blah}")
    print(f"Total output: {sum(all_highest_joltages)}")
