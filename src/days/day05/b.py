from src.shared.controller import Controller
from src.days.day05.solver import Day05Solver


AnswerType = int


class Day05PartBSolver(Day05Solver):
    def solve(self) -> AnswerType:
        return -1


class Day05PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 5, 'b')

    def new_solver(self):
        return Day05PartBSolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [('src/days/day05/inputs/sample01.txt', -1)]

    def file_path(self) -> str:
        return 'src/days/day05/inputs/main.txt'


if __name__ == "__main__":
    controller = Day05PartBController()
    controller.run()
