import re

class Instruction:
    sum_regex_pattern = "mul\([0-9]{1,3}\,[0-9]{1,3}\)"
    do_regex_pattern = "do\(\)"
    dont_regex_pattern = "don\'t\(\)"

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

    def sum_of_enabled_multiplications(self):
        raw_instructions = self._get_all_instructions()
        converted_instructions = []
        for raw_instruction in raw_instructions:
            if raw_instruction.startswith("mul"):
                converted_instructions.append(Sum(raw_sum=raw_instruction))
            else:
                converted_instructions.append(raw_instruction)
        filtered_sums = self._filter_out_disabled_sums(instructions=converted_instructions)
        total_value = 0
        for sum_instruction in filtered_sums:
            total_value += sum_instruction.multiplied_value
        return total_value


    def _get_all_sum_instructions(self):
        regex_output = re.findall(self.sum_regex_pattern, self.raw_instruction)
        return regex_output

    def _get_all_instructions(self) -> [str]:
        regex_pattern = f"{self.sum_regex_pattern}|{self.do_regex_pattern}|{self.dont_regex_pattern}"
        return re.findall(regex_pattern, self.raw_instruction)

    def _filter_out_disabled_sums(self, instructions):
        enabled_sums = []
        should_add_sum = True
        for instruction in instructions:
            if type(instruction) == str:
                if instruction.startswith("don"):
                    should_add_sum = False
                if instruction.startswith("do("):
                    should_add_sum = True
            if type(instruction) == Sum and should_add_sum:
                enabled_sums.append(instruction)
        return enabled_sums

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
