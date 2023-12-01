class Bag:
    def __init__(self, content_string: str):
        self.contents = self.convert_content_string(content_string)
        self.first_compartment = self.contents[:int(len(self.contents)/2)]
        self.second_compartment = self.contents[int(len(self.contents)/2):]
        self.duplicated_item = self.find_matching_elements()

    def convert_content_string(self, content_string: str) -> [int]:
        content_numbers = []
        for letter in content_string:
            content_numbers.append(self.convert_letter_to_int(letter))
        return content_numbers

    def find_matching_elements(self) -> int:
        for number in self.first_compartment:
            if number in self.second_compartment:
                return number

    @staticmethod
    def convert_letter_to_int(letter: str) -> int:
        # write a unit test for this where a gives 1, b gives 2, and a capital
        amount_to_subtract = 0
        if letter.isupper():
            amount_to_subtract = 38
        else:
            amount_to_subtract = 96
        return ord(letter) - amount_to_subtract
