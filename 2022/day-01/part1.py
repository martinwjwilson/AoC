# get the input file contents into a variable
f = open('input.txt', 'r')
content = f.read()
list_of_calories = content.split("\n")

# Split the numbers into a list of lists
list_of_elves = []
current_elf_amount = []
for amount_of_calories in list_of_calories:
    if amount_of_calories != '':
        current_elf_amount.append(int(amount_of_calories))
    else:
        list_of_elves.append(current_elf_amount)
        current_elf_amount = []

# Calculate each elf's total
list_of_elves_total_calories = []
for elf in list_of_elves:
    list_of_elves_total_calories.append(sum(elf))

# Get the highest calorie total
print(max(list_of_elves_total_calories))