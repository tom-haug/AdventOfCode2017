from src.shared.file_loading import load_text_file
from aocd import submit

def get_part_one_result(file_name: str):
  input = load_text_file(file_name)
  checksum_values: list[int] = []
  for line in input:
    values = [int(value) for value in line.split('\t')]
    largest = max(values)
    smallest = min(values)
    diff = largest - smallest
    checksum_values.append(diff)
  return sum(checksum_values)

if __name__ == "__main__":
  result = get_part_one_result('src/day02/input.txt')
  submit(result, part="a", day=2, year=2017)
  print(result)