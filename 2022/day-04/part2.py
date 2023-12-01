from assignment import Assignment

# get list of assignments
f = open("input.txt")
content = f.read().split("\n")
list_of_assignment_pairs = []
for line in content:
    clean_assignment_pair = []
    assignment_pair = line.split(",")
    for assignment in assignment_pair:
        assignment_range = [int(x) for x in assignment.split("-")]
        clean_assignment_pair.append(Assignment(assignment_range))
    list_of_assignment_pairs.append(clean_assignment_pair)

# check if each of the assignment pairs overlap
number_of_overlaps = 0
for assignment_pair in list_of_assignment_pairs:
    if assignment_pair[0].overlaps_at_all(assignment_pair[1].section_range) or \
       assignment_pair[1].overlaps_at_all(assignment_pair[0].section_range):
        number_of_overlaps += 1

print(number_of_overlaps)
