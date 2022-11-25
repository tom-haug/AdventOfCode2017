from src.shared.file_loading import load_text_file
from aocd import submit
from src.day02.common import Solver

class PartASolver(Solver):
  def calc_row_result(self, values: list[int]) -> int:
    largest = max(values)
    smallest = min(values)
    return largest - smallest

def get_part_one_result(file_name: str):
  solver = PartASolver(file_name)
  return solver.solve()

if __name__ == "__main__":
  result = get_part_one_result('src/day02/input.txt')
  # submit(result, part="a", day=2, year=2017)
  print(result)