from group import Group
from bag import Bag

# Open input file
f = open("input.txt")
content = f.read().split("\n")

# get list of bags
list_of_bags = []
for line in content:
    list_of_bags.append(Bag(line))

# get a list of groups
list_of_groups = []
next_bag_index = 0
while next_bag_index < len(list_of_bags):
    bags = list_of_bags[next_bag_index:next_bag_index+3]
    list_of_groups.append(Group(bags))
    next_bag_index += 3

# get sum of group badges
group_badge_total = 0
for group in list_of_groups:
    group_badge_total += group.badge
print(group_badge_total)
