SOLVER_TEMPLATE = """
from abc import abstractclassmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file

class Day{day_string}Solver(Solver):
  data: list[list[int]]

  def initialize(self, file_path: str):
    self.data = self.__load_data_structures(file_path)

  def __load_data_structures(self, file_path: str):
    ...

  def solve(self):
    ...
"""
