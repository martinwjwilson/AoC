class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_invalid_ids(self):
        full_range_of_integers = self.get_full_range_as_integers()
        _all_invalid_ids = []
        for _int in full_range_of_integers:
            value_as_string = str(_int)
            if len(value_as_string) % 2 == 0: # Check string can be split in half
                firstpart, secondpart = (value_as_string[:len(value_as_string) // 2],
                                         value_as_string[len(value_as_string) // 2:])
                if firstpart == secondpart:
                    _all_invalid_ids.append(_int)
        return _all_invalid_ids


    def get_full_range_as_integers(self):
        return list(range(self.start, self.end + 1))

def get_input() -> list[str]:
    f = open('input.txt', 'r')
    content = f.read()
    return content.split(",")

def process_input(input):
    ranges = []
    for line in input:
        start, end = line.split("-")
        ranges.append(Range(start=int(start), end=int(end)))
    return ranges

if __name__ == "__main__":
    unfiltered_input = get_input()
    ranges = process_input(unfiltered_input)
    all_invalid_id_sums = []
    for _range in ranges:
        invalid_ids = _range.get_invalid_ids()
        all_invalid_id_sums.append(sum(invalid_ids))
    print(sum(all_invalid_id_sums))
