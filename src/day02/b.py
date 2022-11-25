from src.shared.file_loading import load_text_file
from aocd import submit

def get_part_two_result(file_name: str):
  input = load_text_file(file_name)
  checksum_values: list[int] = []
  for line in input:
    values = [int(value) for value in line.split('\t')]
    (largest, smallest) = get_divisible_numbers(values)
    quotient = int(largest / smallest)
    checksum_values.append(quotient)
  return sum(checksum_values)

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