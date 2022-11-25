from aocd import submit
from src.day02.common import Solver

class PartBSolver(Solver):
  def calc_row_result(self, values: list[int]) -> int:
    (largest, smallest) = get_divisible_numbers(values)
    return int(largest / smallest)

def get_part_two_result(file_name: str):
  solver = PartBSolver(file_name)
  return solver.solve()

def get_divisible_numbers(values: list[int]) -> tuple[int, int]:
  for idx_1, num_1 in enumerate(values):
    for num_2 in values[idx_1 + 1:]:
      smallest = min(num_1, num_2)
      largest = max(num_1, num_2)
      is_divisible = largest % smallest == 0
      if is_divisible:
        return (largest, smallest)
  raise f"Problem - No divisible numbers in [{values}]"

if __name__ == "__main__":
  result = get_part_two_result('src/day02/input.txt')
  # submit(result, part="b", day=2, year=2017)
  print(result)