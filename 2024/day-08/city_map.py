class CityMap:
    def __init__(self, map_layout):
        self.map_layout = map_layout
        self.antinote_map_layout = self.create_map_of_antinodes()

    def create_map_of_antinodes(self) -> [[str]]:
        # TODO: Create a mep of antinodes from the current map layout
        # Create a blank map
        # Go through the current map, and for each letter, check every following letter
        # If the letters match, plot an antinode if it's within the map limits
        return self.map_layout

    def number_of_antinodes(self) -> int:
        number_of_antinodes = 0
        for row in self.antinote_map_layout:
            for current_element in row:
                if current_element == "#":
                    number_of_antinodes += 1
        return number_of_antinodes
