# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
lines = content.split("\n")

total = 0

for line in lines:
    current_line_digits = []
    for character in line:
        if character.isdigit():
            current_line_digits.append(character)
    total = total + int(current_line_digits[0] + current_line_digits[-1])
    print(f"The line digits are {current_line_digits}\n")

print(f"The total is {total}")
