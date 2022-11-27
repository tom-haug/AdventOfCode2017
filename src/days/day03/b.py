from src.shared.controller import Controller
from src.days.day03.solver import Day03Solver
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Day03PartBSolver(Day03Solver):
    def solve(self) -> int:
        target_value = self.data
        values: dict[tuple[int, int], int] = {}
        cur_x = 0
        cur_y = 0
        dir = Direction.RIGHT

        values[(cur_x, cur_y)] = 1

        while True:
            match dir:
                case Direction.LEFT:
                    cur_x -= 1
                    if (cur_x, cur_y + 1) not in values:
                        dir = Direction.DOWN
                case Direction.RIGHT:
                    cur_x += 1
                    if (cur_x, cur_y - 1) not in values:
                        dir = Direction.UP
                case Direction.UP:
                    cur_y -= 1
                    if (cur_x - 1, cur_y) not in values:
                        dir = Direction.LEFT
                case Direction.DOWN:
                    cur_y += 1
                    if (cur_x + 1, cur_y) not in values:
                        dir = Direction.RIGHT

            cur_value = 0
            # test all 8 adjacent directions
            cur_value += values.get((cur_x - 1, cur_y), 0)
            cur_value += values.get((cur_x - 1, cur_y - 1), 0)
            cur_value += values.get((cur_x - 1, cur_y + 1), 0)

            cur_value += values.get((cur_x, cur_y - 1), 0)
            cur_value += values.get((cur_x, cur_y + 1), 0)

            cur_value += values.get((cur_x + 1, cur_y), 0)
            cur_value += values.get((cur_x + 1, cur_y - 1), 0)
            cur_value += values.get((cur_x + 1, cur_y + 1), 0)

            values[(cur_x, cur_y)] = cur_value

            if cur_value > target_value:
                return cur_value


class Day03PartBController(Controller):
    def __init__(self):
        super().__init__(2017, 3, "b")

    def new_solver(self):
        return Day03PartBSolver()

    def sample_files(self) -> list[tuple[str, int]]:
        return [
            ("src/days/day03/inputs/b_sample01.txt", 4),
            ("src/days/day03/inputs/b_sample02.txt", 25),
        ]

    def file_path(self) -> str:
        return "src/days/day03/inputs/main.txt"


if __name__ == "__main__":
    controller = Day03PartBController()
    controller.run()
