class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_invalid_ids(self):
        full_range_of_integers = self.get_full_range_as_integers()
        _all_invalid_ids = []
        for _int in full_range_of_integers:
            value_as_string = str(_int)
            if self.id_is_invalid(value_as_string):
                _all_invalid_ids.append(_int)
        return _all_invalid_ids

    def id_is_invalid(self, _id):
        # [1,2,3,1,2,3,1,2,3]
        is_valid = True
        print(f"ID: {_id} -- Length = {len(_id)}")
        # multiply the length of the sub id by the current index you're checking to check against other sections
        for index in range(0, len(_id) - 1):
            # Create sub array
            sub_array = _id[0:index + 1]
            print(f"Sub array: {sub_array}")
            # Check the next sub array
            for sub_index in range(0, len(_id),len(sub_array)):
                print(f"Sub sub array: {_id[sub_index:sub_index + len(sub_array)]}")
            print("")
        return is_valid

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
