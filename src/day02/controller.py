from abc import ABC, abstractclassmethod
from typing import Any
from aocd import get_data, submit
from os.path import exists

class Solver(ABC):
  @abstractclassmethod
  def initialize(self, file_path: str) -> None:
    pass

  @abstractclassmethod
  def solve(self):
    pass


class Controller(ABC):
  def __init__(self, year, day, part):
    self.year = year
    self.day = day
    self.part = part

  @abstractclassmethod
  def new_solver(self) -> Solver:
    ...

  @abstractclassmethod
  def sample_files(self) -> list[(str, Any)]:
    ...

  @abstractclassmethod
  def file_path(self) -> str:
    ...

  def __run_test_inputs(self) -> None:
    samples = self.sample_files()
    for (file_path, expected_result) in samples:
      solver = self.new_solver()
      solver.initialize(file_path)
      result = solver.solve()
      if result != expected_result:
        raise f'Test Fail: Sample {file_path}, expecting: {expected_result}, actual: {result}'
      print(f'Test Pass: File: {file_path}, result: {result}')

  def run(self) -> None:
    self.__run_test_inputs()

    solver = self.new_solver()
    file_path = self.file_path()
    self.download_if_not_exists(file_path)
    solver.initialize(file_path)
    result = solver.solve()
    print(f'Result: {result}')
    submit(result, part=self.part, day=self.day, year=self.year)

  def download_if_not_exists(self, file_path: str):
    if exists(file_path):
      return

    data = get_data(day=self.day, year = self.year)

    with open(file_path, 'w') as f:
        f.write(data)
