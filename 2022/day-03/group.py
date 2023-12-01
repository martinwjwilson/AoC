class Group:
    def __init__(self, bags):
        self.bags = bags
        self.badge = self.badge_item()

    # I want to be physically sick looking at this...
    def badge_item(self) -> int:
        previous_bag_contents = None
        matched_contents = []
        for bag in self.bags:
            if previous_bag_contents is not None:
                for item in bag.contents:
                    if item in previous_bag_contents:
                        matched_contents.append(item)
                previous_bag_contents = matched_contents
                matched_contents = []
            else:
                previous_bag_contents = bag.contents
        return previous_bag_contents[0]
