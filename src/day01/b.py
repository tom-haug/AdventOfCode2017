from src.shared.controller import Controller
from src.day01.solver import Day01Solver


class Day01PartBSolver(Day01Solver):
    def calc_digit_offset(self, values: list[int]) -> int:
        return int(len(values) / 2)


class Day01PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 1, "b")

    def new_solver(self):
        return Day01PartBSolver()

    def sample_files(self) -> list[(str, int)]:
        return [
            ("src/day01/input_b_sample01.txt", 6),
            ("src/day01/input_b_sample02.txt", 0),
            ("src/day01/input_b_sample03.txt", 4),
            ("src/day01/input_b_sample04.txt", 12),
            ("src/day01/input_b_sample05.txt", 4),
        ]

    def file_path(self) -> str:
        return "src/day01/input.txt"


if __name__ == "__main__":
    controller = Day01PartBController()
    controller.run()
