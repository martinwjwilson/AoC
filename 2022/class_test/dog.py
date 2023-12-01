class Dog:
    def __init__(self, toys):
        self.toys = toys

    def remove_toy(self):
        self.toys.pop()
