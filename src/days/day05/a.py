from src.shared.controller import Controller
from src.days.day05.solver import Day05Solver


AnswerType = int


class Day05PartASolver(Day05Solver):
    def solve(self) -> AnswerType:
        instructions = self.data
        cur_idx = 0
        jump_count = 0

        while True:
            jump_offset = instructions[cur_idx]
            jump_count += 1
            instructions[cur_idx] += 1
            cur_idx = cur_idx + jump_offset
            if cur_idx < 0 or cur_idx >= len(instructions):
                break

        return jump_count


class Day05PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 5, 'a')

    def new_solver(self):
        return Day05PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [('src/days/day05/inputs/sample01.txt', 5)]

    def file_path(self) -> str:
        return 'src/days/day05/inputs/main.txt'


if __name__ == "__main__":
    controller = Day05PartAController()
    controller.run()

# 1056 That's not the right answer; your answer is too low.