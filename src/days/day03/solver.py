from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


class Day03Solver(Solver):
    data: int

    def initialize(self, file_path: str):
        self.data = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> int:
        input = load_text_file(file_path)
        return int(input[0])

    @abstractmethod
    def solve(self) -> int:
        ...
