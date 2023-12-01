from bag import Bag

# get list of bags
f = open("input.txt")
content = f.read().split("\n")
list_of_bags = []
for line in content:
    list_of_bags.append(Bag(line))

# get the total number of duplicated items from the list of bags
total_amount = 0
for bag in list_of_bags:
    total_amount += bag.duplicated_item
print(total_amount)
