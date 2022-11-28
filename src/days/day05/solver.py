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

    @abstractmethod
    def solve(self) -> int:
        ...
