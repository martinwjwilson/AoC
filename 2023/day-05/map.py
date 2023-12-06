class Map:
    def __init__(self):
        self.rows: list[MapRow] = []


class MapRow:
    def __init__(self, destination_range_start, source_range_start, range_length):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length
