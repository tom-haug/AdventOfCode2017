from src.shared.controller import Controller
from src.days.day06.solver import Day06Solver


AnswerType = int


class Day06PartBSolver(Day06Solver):
    def get_result(self, bank_hashes: dict[int, int], ending_cycle_number: int, ending_hash: int) -> int:
        return ending_cycle_number - bank_hashes[ending_hash]


class Day06PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 6, 'b')

    def new_solver(self):
        return Day06PartBSolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [('src/days/day06/inputs/sample01.txt', 4)]

    def file_path(self) -> str:
        return 'src/days/day06/inputs/main.txt'


if __name__ == "__main__":
    controller = Day06PartBController()
    controller.run()
