PART_TEMPLATE = """
from src.shared.controller import Controller
from src.day{day_string}.solver import Day{day_string}Solver

class Day{day_string}Part{part_upper}Solver(Day{day_string}Solver):
  ...


class Day{day_string}Part{part_upper}Controller(Controller):
  def __init__(self):
    super().__init__({year}, {day_int}, '{part}')

  def new_solver(self):
    return Day{day_string}Part{part_upper}Solver()

  def sample_files(self) -> list[(str, int)]:
      return []

  def file_path(self) -> str:
      return 'src/day{day_string}/input.txt'


if __name__ == "__main__":
  controller = Day{day_string}Part{part_upper}Controller()
  controller.run()
"""
