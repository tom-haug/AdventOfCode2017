from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


class Day05Solver(Solver):
    data: list[int]

    def initialize(self, file_path: str):
        self.data = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> list[int]:
        input = load_text_file(file_path)
        return [int(line) for line in input]

    def solve(self) -> int:
        instructions = self.data
        cur_idx = 0
        jump_count = 0

        while True:
            jump_offset = instructions[cur_idx]
            jump_count += 1
            instructions[cur_idx] += self.get_value_increment(jump_offset)
            cur_idx = cur_idx + jump_offset
            if cur_idx < 0 or cur_idx >= len(instructions):
                break

        return jump_count

    @abstractmethod
    def get_value_increment(self, jump_offset: int) -> int:
        ...
