from src.shared.controller import Controller
from src.days.day02.solver import Day02Solver


class Day02PartBSolver(Day02Solver):
    def calc_row_result(self, values: list[int]) -> int:
        (largest, smallest) = get_divisible_numbers(values)
        return int(largest / smallest)


class Day02PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 2, "b")

    def new_solver(self):
        return Day02PartBSolver()

    def sample_files(self) -> list[tuple[str, int]]:
        return [("src/days/day02/inputs/b_sample01.txt", 9)]

    def file_path(self) -> str:
        return "src/days/day02/inputs/main.txt"


def get_divisible_numbers(values: list[int]) -> tuple[int, int]:
    for idx_1, num_1 in enumerate(values):
        for num_2 in values[idx_1 + 1 :]:
            smallest = min(num_1, num_2)
            largest = max(num_1, num_2)
            is_divisible = largest % smallest == 0
            if is_divisible:
                return (largest, smallest)
    raise Exception(f"Problem - No divisible numbers in [{values}]")


if __name__ == "__main__":
    controller = Day02PartBController()
    controller.run()
