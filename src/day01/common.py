def get_repeat_digits(items: list[int], next_digit_offset: int) -> int:
  repeat_digits: list[int] = []
  for idx, digit in enumerate(items):
    next_idx = idx + next_digit_offset
    
    if next_idx > len(items) - 1:
      next_idx -= len(items)

    if digit == items[next_idx]:
      repeat_digits.append(digit)
  return repeat_digits  