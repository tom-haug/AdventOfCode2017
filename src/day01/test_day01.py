from src.day01.a import Day01PartAController
from src.day01.b import Day01PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay02(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day01PartAController()

    def get_controller_b(self) -> Controller:
        return Day01PartBController()
