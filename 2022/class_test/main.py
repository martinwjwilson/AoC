from dog import Dog

from copy import copy

class Toy:
    def __init__(self, size):
        self.size = size


list_of_toys = []
list_of_toys.append(Toy(4))
list_of_toys.append(Toy(6))
list_of_toys.append(Toy(8))

new_list_of_toys = list_of_toys

my_dog = Dog(new_list_of_toys)
your_dog = Dog(new_list_of_toys)

p = [[0, 1, 2]] * 4
print(p)
p[0].append(3)
print(p)

# print(my_dog.toys)
# print(your_dog.toys)
# list_of_toys.pop()
# print(my_dog.toys)
# print(your_dog.toys)
