from abc import abstractclassmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


class Day01Solver(Solver):
    data: list[int]

    def initialize(self, file_path: str):
        self.data = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str):
        input = load_text_file(file_path)
        return [int(char) for char in input[0]]

    def solve(self):
        digit_offset = self.calc_digit_offset(self.data)
        repeat_digits = get_repeat_digits(self.data, digit_offset)
        return sum(repeat_digits)

    @abstractclassmethod
    def calc_digit_offset(self, values: list[int]) -> int:
        pass


def get_repeat_digits(items: list[int], next_digit_offset: int) -> int:
    repeat_digits: list[int] = []
    for idx, digit in enumerate(items):
        next_idx = idx + next_digit_offset

        if next_idx > len(items) - 1:
            next_idx -= len(items)

        if digit == items[next_idx]:
            repeat_digits.append(digit)
    return repeat_digits
