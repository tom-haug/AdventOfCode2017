from src.shared.controller import Controller
from src.days.day02.solver import Day02Solver


class Day02PartASolver(Day02Solver):
    def calc_row_result(self, values: list[int]) -> int:
        largest = max(values)
        smallest = min(values)
        return largest - smallest


class Day02PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 2, "a")

    def new_solver(self):
        return Day02PartASolver()

    def sample_files(self) -> list[(str, int)]:
        return [("src/days/day02/inputs/a_sample01.txt", 18)]

    def file_path(self) -> str:
        return "src/days/02/dayinputs/main.txt"


if __name__ == "__main__":
    controller = Day02PartAController()
    controller.run()
