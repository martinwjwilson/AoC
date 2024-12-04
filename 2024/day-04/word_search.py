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
                if self._word_found_at_position():
                    word_count += 1
        return word_count

    def _word_found_at_position(self, row_index: int, column_index: int) -> bool:
        # Calculate safe directions
        return True

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
        return row_index >= grid_height - word_length

    @staticmethod
    def _west_is_safe(word_length: int, column_index: int) -> bool:
        return column_index >= word_length - 1
