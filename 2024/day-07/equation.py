from copy import deepcopy


class Equation:
    def __init__(self, test_value: int, values: [int]):
        self.test_value = test_value
        self.values = values

    def is_true(self) -> bool:
        return self.test_value in self.calculate_all_equation_possibilities()

    def calculate_all_equation_possibilities(self) -> [int]:
        parent_nodes = []
        for value in self.values:
            temp_parent_notes = []
            if not parent_nodes:
                parent_nodes.append(value)
            else:
                for node in parent_nodes:
                    first_node, second_node, third_node = self.perform_all_operations_on_node(current_node=node,
                                                                                              value=value)
                    temp_parent_notes.extend([first_node, second_node, third_node])
                parent_nodes = deepcopy(temp_parent_notes)
        return parent_nodes

    @staticmethod
    def perform_plus_and_multiplication_operations_on_node(current_node, value) -> tuple[int, int]:
        first_answer = current_node + value
        second_answer = current_node * value
        return first_answer, second_answer

    @staticmethod
    def perform_all_operations_on_node(current_node, value) -> tuple[int, int, int]:
        first_answer = current_node + value
        second_answer = current_node * value
        third_answer = int(str(current_node) + str(value))
        return first_answer, second_answer, third_answer
