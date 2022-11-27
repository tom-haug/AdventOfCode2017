from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Day04Solver(Solver):
    data: list[str]

    def initialize(self, file_path: str) -> None:
        self.data = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str):
        input = load_text_file(file_path)
        return input

    def solve(self) -> AnswerType:
        lines = self.data
        valid_count = 0
        for line in lines:
            words = line.split(" ")

            formatted_words = [self.word_formatter(word) for word in words]

            unique_words = set(formatted_words)
            if len(formatted_words) == len(unique_words):
                valid_count += 1
        return valid_count

    @abstractmethod
    def word_formatter(self, word: str) -> str:
        ...
