from src.shared.controller import Controller
from src.days.day05.solver import Day05Solver


AnswerType = int


class Day05PartASolver(Day05Solver):
    def get_value_increment(self, jump_offset: int) -> int:
        return 1


class Day05PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 5, "a")

    def new_solver(self):
        return Day05PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day05/inputs/sample01.txt", 5)]

    def file_path(self) -> str:
        return "src/days/day05/inputs/main.txt"


if __name__ == "__main__":
    controller = Day05PartAController()
    controller.run()
