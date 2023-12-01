digit_names = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
lines = content.split("\n")

total = 0

for line in lines:
    current_line_digits = []
    for i in range(len(line)):
        current_character = line[i]
        if current_character.isdigit():
            current_line_digits.append(current_character)
        else:
            for j in range(i, len(line) + 1):
                if i != j and line[i:j] in digit_names:
                    print(f"The current substring is: {line[i:j]}. I is {i} and J is {j}")
                    print(f"The index of that substring is {digit_names.index(line[i:j]) + 1}")
                    current_line_digits.append(str(digit_names.index(line[i:j]) + 1))
                    break
    total = total + int(current_line_digits[0] + current_line_digits[-1])
    print(f"The line digits are {current_line_digits}\n")

print(f"The total is {total}")
