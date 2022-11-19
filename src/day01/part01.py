from src.shared.file_loading import load_text_file
from src.day01.common import get_repeat_digits

def get_part_one_result(file_name: str):
  contents = load_text_file(file_name)
  list = [int(char) for char in contents[0]]
  repeat_digits = get_repeat_digits(list, 1)
  return sum(repeat_digits)

if __name__ == "__main__":
  result = get_part_one_result('src/day01/input.txt')
  print(result)