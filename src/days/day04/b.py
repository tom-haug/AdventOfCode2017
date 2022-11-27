from src.shared.controller import Controller
from src.days.day04.solver import Day04Solver, AnswerType


class Day04PartBSolver(Day04Solver):
    def word_formatter(self, word: str) -> str:
        return "".join(sorted([*word]))


class Day04PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 4, "b")

    def new_solver(self):
        return Day04PartBSolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [
            ("src/days/day04/inputs/b_sample01.txt", 1),
            ("src/days/day04/inputs/b_sample02.txt", 0),
            ("src/days/day04/inputs/b_sample03.txt", 1),
            ("src/days/day04/inputs/b_sample04.txt", 1),
            ("src/days/day04/inputs/b_sample05.txt", 0),
        ]

    def file_path(self) -> str:
        return "src/days/day04/inputs/main.txt"


if __name__ == "__main__":
    controller = Day04PartBController()
    controller.run()
