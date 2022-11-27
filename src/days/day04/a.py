from src.shared.controller import Controller
from src.days.day04.solver import Day04Solver, AnswerType


class Day04PartASolver(Day04Solver):
    def word_formatter(self, word: str) -> str:
        return word


class Day04PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 4, "a")

    def new_solver(self):
        return Day04PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [
            ("src/days/day04/inputs/sample01.txt", 1),
            ("src/days/day04/inputs/sample02.txt", 0),
            ("src/days/day04/inputs/sample03.txt", 1),
        ]

    def file_path(self) -> str:
        return "src/days/day04/inputs/main.txt"


if __name__ == "__main__":
    controller = Day04PartAController()
    controller.run()
