from command import Command
from directory import Directory
from file import File


def get_list_of_commands(input_list: [str]):
    list_of_commands = []
    for string in input_list:
        if string[0] == "$":
            list_of_commands.append(string)
    return list_of_commands


def get_list_of_directory_elements(input_list: [str]):
    list_of_directory_elements = []
    current_group = []
    for string in input_list:
        # if the string isn't a command
        if string[0] != "$":
            print(string)
            string_elements = string.split(" ")
            if string_elements[0] == "dir":
                current_group.append(Directory(string_elements[1]))
            else:
                current_group.append(File(string_elements[1],
                                          int(string_elements[0])))
        else:
            # if it's a command then add current group if it's not empty
            if current_group:
                list_of_directory_elements.append(current_group)
            # reset the current group
            current_group = []
    # if the last command wasn't a command then the group will need to be added separately
    if len(current_group) > 0:
        list_of_directory_elements.append(current_group)
    return list_of_directory_elements


def create_elements_in_directory(parent_directory: Directory, list_of_elements):
    for element in list_of_elements:
        if type(element) == File:
            parent_directory.add_file(element)
        else:
            parent_directory.add_directory(element)


def calculate_directory_size(directory: Directory):
    total = 0
    if directory.calculate_total_size() < 100000:
        total += directory.calculate_total_size()
    if len(directory.directories) > 0:
        for child_directory in directory.directories:
            other_total = calculate_directory_size(child_directory)
            total += other_total
    return total


def get_list_of_possible_directories(directory: Directory):
    possible_directories = []
    if directory.calculate_total_size() > 3636666:
        possible_directories.append(directory)
    if len(directory.directories) > 0:
        for child_directory in directory.directories:
            returned_directories = get_list_of_possible_directories(child_directory)
            for returned_directory in returned_directories:
                possible_directories.append(returned_directory)
    return possible_directories


if __name__ == '__main__':
    # open input file
    f = open("input.txt")
    content = f.read().split("\n")

    # get a list of commands to be executed
    commands = []
    command_strings = get_list_of_commands(content)
    print(command_strings)
    for command_string in command_strings:
        command_string_list = command_string.split(" ")
        if len(command_string_list) > 2:
            commands.append(Command(command_string_list[1],
                                    command_string_list[2]))
        else:
            commands.append(Command(command_string_list[1]))

    # get a list of files and directories, these will occur after an `ls` command
    # get a better name for this
    directory_elements = get_list_of_directory_elements(content)
    print(directory_elements)

    # go through the commands and create the directory tree
    # we create the root directory since we have to start with one
    directory_tree = [Directory("/")]
    current_directory = directory_tree[0]
    directory_element_index = 0  # record which group the `ls` command is referencing
    for command in commands:
        if command.command_operation == "ls":
            create_elements_in_directory(current_directory, directory_elements[directory_element_index])
            directory_element_index += 1
        elif command.command_operation == "cd":
            if command.command_argument == "/":
                current_directory = directory_tree[0]
            elif command.command_argument == "..":
                # print(current_directory.name)
                current_directory = current_directory.parent
            else:
                for directory in current_directory.directories:
                    if directory.name == command.command_argument:
                        current_directory = directory

    part_one = calculate_directory_size(directory_tree[0])
    print(part_one)

    print(f"Current free space is: {70000000 - directory_tree[0].calculate_total_size()}")
    print(f"Current free space needed: {30000000 - 26363334}")
    possible_directories = get_list_of_possible_directories(directory_tree[0])
    print(f"There are {len(possible_directories)} possible directories")
    smallest_directory = None
    for each_directory in possible_directories:
        if smallest_directory is None:
            smallest_directory = each_directory
            print("Changed this")
        elif each_directory.calculate_total_size() < smallest_directory.calculate_total_size():
            smallest_directory = each_directory
            print("Got here")
    part_two = smallest_directory.calculate_total_size()
    print(part_two)
