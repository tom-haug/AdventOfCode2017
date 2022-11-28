from src.days.day06.a import Day06PartAController
from src.days.day06.b import Day06PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay06(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day06PartAController()

    def get_controller_b(self) -> Controller:
        return Day06PartBController()
