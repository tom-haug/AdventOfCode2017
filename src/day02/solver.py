from abc import abstractclassmethod
from src.day02.controller import Solver
from src.shared.file_loading import load_text_file

class Day02Solver(Solver):
  data: list[list[int]]

  def initialize(self, file_path: str):
    self.data = self.__load_data_structures(file_path)

  def __load_data_structures(self, file_path: str):
    input = load_text_file(file_path)
    return [[int(value) for value in line.split('\t')] for line in input]

  def solve(self):
    row_values: list[int] = []
    for row in self.data:
      row_value = self.calc_row_result(row)
      row_values.append(row_value)
    final_result = sum(row_values)
    return final_result

  @abstractclassmethod
  def calc_row_result(self, values: list[int]) -> int:
    pass
