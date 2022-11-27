import math
from src.shared.controller import Controller
from src.days.day03.solver import Day03Solver


class Day03PartASolver(Day03Solver):
    def solve(self):
        target_value = self.data
        max_square = 1
        test_square = -1
        min_distance_offset = 0
        while True:
            test_square += 2
            max_square = test_square
            min_distance_offset -= 1
            if math.pow(test_square, 2) >= target_value:
                break

        max_distance = max_square - 1
        min_distance = max_square + min_distance_offset

        begin_test = int(math.pow(max_square - 2, 2) + 1)
        end_test = target_value + 1
        cur_distance = max_distance
        incr = -1
        for test_value in range(begin_test, end_test):
            cur_distance = max(cur_distance + incr, 0)
            if cur_distance in [min_distance, max_distance]:
                incr *= -1
        return cur_distance


class Day03PartAController(Controller):
    def __init__(self):
        super().__init__(2017, 3, "a")

    def new_solver(self):
        return Day03PartASolver()

    def sample_files(self) -> list[(str, int)]:
        return [
            ("src/days/day03/inputs/a_sample01.txt", 0),
            ("src/days/day03/inputs/a_sample02.txt", 3),
            ("src/days/day03/inputs/a_sample03.txt", 2),
            ("src/days/day03/inputs/a_sample04.txt", 31),
        ]

    def file_path(self) -> str:
        return "src/days/day03/inputs/main.txt"


if __name__ == "__main__":
    controller = Day03PartAController()
    controller.run()
