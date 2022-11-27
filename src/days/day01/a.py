from src.shared.controller import Controller
from src.days.day01.solver import Day01Solver


class Day01PartASolver(Day01Solver):
    def calc_digit_offset(self, values: list[int]) -> int:
        return 1


class Day01PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 1, "a")

    def new_solver(self):
        return Day01PartASolver()

    def sample_files(self) -> list[tuple[str, int]]:
        return [
            ("src/days/day01/inputs/a_sample01.txt", 3),
            ("src/days/day01/inputs/a_sample02.txt", 4),
            ("src/days/day01/inputs/a_sample03.txt", 0),
            ("src/days/day01/inputs/a_sample04.txt", 9),
        ]

    def file_path(self) -> str:
        return "src/days/day01/inputs/main.txt"


if __name__ == "__main__":
    controller = Day01PartAController()
    controller.run()
