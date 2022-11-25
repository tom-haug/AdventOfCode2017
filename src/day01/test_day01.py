
from src.day01.a import Day01PartAController, Day01PartASolver
from src.day01.b import Day01PartBController, Day01PartBSolver
from src.shared.base_test import BaseTest
from src.shared.controller import Controller, Solver


class TestDay02(BaseTest): 
  def get_controller_a(self) -> Controller:
    return Day01PartAController()

  def get_controller_b(self) -> Controller:
    return Day01PartBController()

  def get_solver_a(self) -> Solver:
    return Day01PartASolver()

  def get_solver_b(self) -> Solver:
    return Day01PartBSolver()