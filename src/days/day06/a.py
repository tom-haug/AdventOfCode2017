from src.shared.controller import Controller
from src.days.day06.solver import Day06Solver


AnswerType = int


class Day06PartASolver(Day06Solver):
    def get_result(
        self, bank_hashes: dict[int, int], ending_cycle_number: int, ending_hash: int
    ) -> int:
        return ending_cycle_number


class Day06PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 6, "a")

    def new_solver(self):
        return Day06PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day06/inputs/sample01.txt", 5)]

    def file_path(self) -> str:
        return "src/days/day06/inputs/main.txt"


if __name__ == "__main__":
    controller = Day06PartAController()
    controller.run()
