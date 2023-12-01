class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.parent = parent_directory
        self.directories = []
        self.files = []

    def add_directory(self, directory):
        directory.parent = self
        self.directories.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def set_directories_parents(self):
        for directory in self.directories:
            directory.parent = self

    def calculate_total_size(self) -> int:
        total_size = 0
        # check current files
        if len(self.files) > 0:
            for file in self.files:
                total_size += file.size
        # check directories
        if len(self.directories) > 0:
            for directory in self.directories:
                total = directory.calculate_total_size()
                total_size += total
        return total_size
