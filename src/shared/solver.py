from abc import ABC, abstractclassmethod
from typing import Any


class Solver(ABC):
    @abstractclassmethod
    def initialize(self, file_path: str) -> None:
        pass

    @abstractclassmethod
    def solve(self) -> Any:
        pass
