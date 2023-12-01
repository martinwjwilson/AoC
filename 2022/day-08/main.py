from tree import Tree


# Anything north of the tree is North, and the Y will be -1 of the
# When the y is +1 it will always be south
# East and west the Y coordinate will match and the x coordinate will be either < or >
def is_tree_visible(forest: [Tree], current_tree: Tree) -> bool:
    north_visible = True
    east_visible = True
    south_visible = True
    west_visible = True
    for comparison_tree in forest:
        # North
        if (comparison_tree.y < current_tree.y) and (comparison_tree.x == current_tree.x):
            if comparison_tree.height >= current_tree.height:
                north_visible = False
        # West
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x < current_tree.x):
            if comparison_tree.height >= current_tree.height:
                west_visible = False
        # East
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x > current_tree.x):
            if comparison_tree.height >= current_tree.height:
                east_visible = False
        # South
        if (comparison_tree.y > current_tree.y) and (comparison_tree.x == current_tree.x):
            if comparison_tree.height >= current_tree.height:
                south_visible = False
    if north_visible or east_visible or south_visible or west_visible:
        print(True)
        return True
    print(False)
    return False


def calculate_border_count(last_tree):
    return (last_tree.x + last_tree.y) * 2


def calculate_number_of_visible_trees(forest) -> int:
    total_number_of_visible_trees = 0
    # calculate number of trees on border as they're all visible
    total_number_of_visible_trees += calculate_border_count(forest[-1])
    maximum_x = forest[-1].x
    maximum_y = forest[-1].y
    tree_counter = 0
    for tree in forest:
        if (tree.x != 0) and (tree.y != 0) and (tree.x != maximum_x) and (tree.y != maximum_y):
            if is_tree_visible(forest, tree):
                tree_counter += 1
    return total_number_of_visible_trees + tree_counter


def calculate_scenic_scores(current_tree, forest) -> [int]:
    north_score = 0
    east_score = 0
    west_score = 0
    south_score = 0
    maximum_x = forest[-1].x
    maximum_y = forest[-1].y
    for comparison_tree in forest:
        # North
        if (comparison_tree.y < current_tree.y) and (comparison_tree.x == current_tree.x):
            if comparison_tree.y == 0:
                north_score = current_tree.y
            elif comparison_tree.height >= current_tree.height:
                north_score = current_tree.y - comparison_tree.y
        # West
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x < current_tree.x):
            if comparison_tree.x == 0:
                west_score = current_tree.x
            elif comparison_tree.height >= current_tree.height:
                west_score = current_tree.x - comparison_tree.x
        # East
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x > current_tree.x):
            if east_score == 0:
                if comparison_tree.height >= current_tree.height:
                    east_score = comparison_tree.x - current_tree.x
                elif comparison_tree.x == maximum_x:
                    east_score = maximum_x - current_tree.x
        # South
        if (comparison_tree.y > current_tree.y) and (comparison_tree.x == current_tree.x):
            if south_score == 0:
                if comparison_tree.height >= current_tree.height:
                    south_score = comparison_tree.y - current_tree.y
                elif comparison_tree.y == maximum_y:
                    south_score = maximum_y - current_tree.y
    print(f"{north_score},{west_score},{south_score},{east_score}")
    return [north_score, west_score, south_score, east_score]


def calculate_highest_scenic_score(forest) -> int:
    highest_score = 0
    for tree in forest:
        scenic_scores = calculate_scenic_scores(tree, forest)
        tree.set_scenic_score(scenic_scores[0], scenic_scores[1], scenic_scores[2], scenic_scores[3])
        if tree.scenic_score > highest_score:
            highest_score = tree.scenic_score
            print(f"The tree is {tree.x},{tree.y} with a score of {tree.scenic_score}")
    return highest_score


if __name__ == '__main__':
    f = open("input.txt")
    content = f.read().splitlines()
    print(content)

    forest = []
    y_coordinate = 0
    for row in content:
        x_coordinate = 0
        for element in row:
            # create a tree and give it coordinates
            forest.append(Tree(int(element), x_coordinate, y_coordinate))
            x_coordinate += 1
        y_coordinate += 1

    # print(f"The solution for part 1 is: {calculate_number_of_visible_trees(forest)}")
    print(f"The solution for part 2 is: {calculate_highest_scenic_score(forest)}")
