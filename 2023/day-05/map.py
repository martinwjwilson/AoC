class Map:
    def __init__(self):
        self.rows: list[MapRow] = []

    def convert_number(self, input_number: int) -> int:
        input_was_updated = False
        # create a range
        for i in self.rows:
            # check if input_number is in the range
            if ((i.source_range_start <= input_number <= (i.source_range_start + i.range_length)) and
                    not input_was_updated):
                # if it is then convert it through the map
                difference = input_number - i.source_range_start
                input_number = i.destination_range_start + difference
                input_was_updated = True
        # return the answer
        print(f"Getting returned is: {input_number}\n")
        return input_number


class MapRow:
    def __init__(self, destination_range_start: int, source_range_start: int, range_length: int):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length
