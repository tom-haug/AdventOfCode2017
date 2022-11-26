from abc import ABC, abstractclassmethod
from src.shared.controller import Controller


class BaseTest(ABC):
    @abstractclassmethod
    def get_controller_a(self) -> Controller:
        ...

    @abstractclassmethod
    def get_controller_b(self) -> Controller:
        ...

    def test_part01(self):
        controller = self.get_controller_a()
        tests = controller.sample_files()
        for (file, expected_result) in tests:
            solver = controller.new_solver()
            solver.initialize(file)
            result = solver.solve()
            assert result == expected_result

    def test_part02(self):
        controller = self.get_controller_b()
        tests = controller.sample_files()
        for (file, expected_result) in tests:
            solver = controller.new_solver()
            solver.initialize(file)
            result = solver.solve()
            assert result == expected_result
