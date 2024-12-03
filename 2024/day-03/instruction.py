import re

class Instruction:
    def __init__(self, raw_instruction: str):
        self.raw_instruction = raw_instruction

    def sum_of_all_multiplications(self) -> int:
        raw_sum_instructions = self._get_all_sum_instructions()
        sum_instructions = []
        for raw_sum in raw_sum_instructions:
            sum_instructions.append(Sum(raw_sum=raw_sum))
        total_value = 0
        for sum_instruction in sum_instructions:
            total_value += sum_instruction.multiplied_value
        return total_value

    def _get_all_sum_instructions(self):
        regex_pattern = "mul\([0-9]{1,3}\,[0-9]{1,3}\)"
        regex_output = re.findall(regex_pattern, self.raw_instruction)
        print(regex_output)
        return regex_output

class Sum:
    def __init__(self, raw_sum: str):
        self.raw_sum = raw_sum
        self.x = self._get_x_of_sum()
        self.y = self._get_y_of_sum()
        self.multiplied_value = self.x * self.y

    def _get_x_of_sum(self):
        return int(self.raw_sum.split(",")[0].split("(")[1])

    def _get_y_of_sum(self):
        return int(self.raw_sum.split(",")[1].split(")")[0])
