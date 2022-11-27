from src.days.day04.a import Day04PartAController
from src.days.day04.b import Day04PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay04(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day04PartAController()

    def get_controller_b(self) -> Controller:
        return Day04PartBController()
