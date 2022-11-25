from abc import ABC, abstractclassmethod

from src.shared.controller import Controller, Solver

class BaseTest(ABC):
  @abstractclassmethod
  def get_controller_a(self) -> Controller:
    ...

  @abstractclassmethod
  def get_controller_b(self) -> Controller:
    ...
  
  @abstractclassmethod
  def get_solver_a(self) -> Solver:
    ...

  @abstractclassmethod
  def get_solver_b(self) -> Solver:
    ...


  def test_part01(self):
    controller = self.get_controller_a()
    tests = controller.sample_files()
    for (file, expected_result) in tests:
      solver = self.get_solver_a()
      solver.initialize(file)
      result = solver.solve()
      assert result == expected_result
 
  def test_part02(self): 
    controller = self.get_controller_b()
    tests = controller.sample_files()
    for (file, expected_result) in tests:
      solver = self.get_solver_b()
      solver.initialize(file)
      result = solver.solve()
      assert result == expected_result