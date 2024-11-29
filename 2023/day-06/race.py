class Race:
    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance

    def calculate_number_of_ways_to_win(self) -> int:
        total = 0
        for i in range(self.time):
            speed = i
            remaining_time = self.time - i
            distance_travelled = speed * remaining_time
            if distance_travelled > self.distance:
                total += 1
        return total
