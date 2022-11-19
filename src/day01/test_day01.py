import src.day01.part01 as part01
import src.day01.part02 as part02

class TestDay02:
  def test_part01(self):
    result = part01.get_part_one_result("src/day01/input.txt")
    assert result == 1049

  def test_part02(self):
    result = part02.get_part_two_result("src/day01/input.txt")
    assert result == 1508