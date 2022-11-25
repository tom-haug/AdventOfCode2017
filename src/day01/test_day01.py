import src.day01.a as a
import src.day01.b as b

class TestDay02:
  def test_part01(self):
    result = a.get_part_one_result("src/day01/input.txt")
    assert result == 1049

  def test_part02(self):
    result = b.get_part_two_result("src/day01/input.txt")
    assert result == 1508