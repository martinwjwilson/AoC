class Bank:
    def __init__(self, batteries):
        self.batteries = batteries
        self.highest_joltage = self.get_highest_joltage()

    def get_highest_joltage(self):
        highest_joltage = 0
        for index, joltage in enumerate(self.batteries):
            print(joltage)
            next_joltages = self.batteries[index+1:]
            for blah in next_joltages:
                new_temp_joltage = int(joltage + blah)
                if new_temp_joltage > highest_joltage:
                    highest_joltage = new_temp_joltage
        return highest_joltage

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
        all_highest_joltages.append(bank.highest_joltage)
    print(f"Total output: {sum(all_highest_joltages)}")
