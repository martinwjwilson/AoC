class WordSearch:
    def __init__(self, grid: [[str]], word_to_search_for: str):
        self.grid = grid
        self.word_to_search_for = word_to_search_for

    def number_of_occurrences(self) -> int:
        """
        When calculating the number of times a word comes up,
        Search for the first letter of the word. When a match appears,
        Check the directions where the word could possibly fit
        :return:
        """
        word_count = 0
        for row_index, row in enumerate(self.grid):
            for column_index, column in enumerate(row):
                word_count += self._word_found_at_position(row_index=row_index, column_index=column_index)
        return word_count

    def _word_found_at_position(self, row_index: int, column_index: int) -> int:
        safe_directions = self._get_safe_directions(row_index=row_index, column_index=column_index)
        return self._number_of_words_exist_in_directions(row_index=row_index,
                                                         column_index=column_index,
                                                         directions=safe_directions)

    def _get_safe_directions(self, row_index: int, column_index: int):
        # Depending on the current position, it would only be possible to find the word in certain directions
        # Calculating this stops searching in directions that would be impossible
        safe_directions = []
        word_length = len(self.word_to_search_for)
        grid_width = len(self.grid[0])
        grid_height = len(self.grid)
        if self._north_is_safe(word_length=word_length, row_index=row_index):
            safe_directions.append("N")
            if self._east_is_safe(word_length=word_length, column_index=column_index, grid_width=grid_width):
                safe_directions.append("NE")
            if self._west_is_safe(word_length=word_length, column_index=column_index):
                safe_directions.append("NW")
        if self._east_is_safe(word_length=word_length, column_index=column_index, grid_width=grid_width):
            safe_directions.append("E")
        if self._south_is_safe(word_length=word_length, row_index=row_index, grid_height=grid_height):
            safe_directions.append("S")
            if self._east_is_safe(word_length=word_length, column_index=column_index, grid_width=grid_width):
                safe_directions.append("SE")
            if self._west_is_safe(word_length=word_length, column_index=column_index):
                safe_directions.append("SW")
        if self._west_is_safe(word_length=word_length, column_index=column_index):
            safe_directions.append("W")
        return safe_directions

    @staticmethod
    def _north_is_safe(word_length: int, row_index: int) -> bool:
        return row_index >= word_length - 1

    @staticmethod
    def _east_is_safe(word_length: int, column_index: int, grid_width: int) -> bool:
        return column_index <= grid_width - word_length

    @staticmethod
    def _south_is_safe(word_length: int, row_index: int, grid_height: int) -> bool:
        return row_index <= grid_height - word_length

    @staticmethod
    def _west_is_safe(word_length: int, column_index: int) -> bool:
        return column_index >= word_length - 1

    def _number_of_words_exist_in_directions(self, row_index: int, column_index: int, directions: [str]) -> int:
        number_of_words = 0
        for direction in directions:
            # TODO: Change the directions to an enum
            match direction:
                case "N":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=0,
                                                                          y_direction=-1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "NE":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=1,
                                                                          y_direction=-1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "E":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=1,
                                                                          y_direction=0)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "SE":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=1,
                                                                          y_direction=1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "S":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=0,
                                                                          y_direction=1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "SW":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=-1,
                                                                          y_direction=1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "W":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=-1,
                                                                          y_direction=0)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
                case "NW":
                    word_to_check = self._get_word_from_grid_in_direction(row_index=row_index,
                                                                          column_index=column_index,
                                                                          x_direction=-1,
                                                                          y_direction=-1)
                    if self.word_to_search_for == word_to_check:
                        number_of_words += 1
        return number_of_words

    # TODO: Move index into a class or struct
    # TODO: Move direction into a class or struct
    def _get_word_from_grid_in_direction(self, row_index: int, column_index: int, x_direction: int,
                                         y_direction: int) -> str:
        word_in_direction = ""
        current_x = column_index
        current_y = row_index
        print(f"current x: {column_index}, current y: {row_index}")
        for x in self.word_to_search_for:
            word_in_direction += self.grid[current_y][current_x]
            current_x += x_direction
            current_y += y_direction
        return word_in_direction
