from abc import ABC, abstractclassmethod


class Solver(ABC):
    @abstractclassmethod
    def initialize(self, file_path: str) -> None:
        pass

    @abstractclassmethod
    def solve(self):
        pass
