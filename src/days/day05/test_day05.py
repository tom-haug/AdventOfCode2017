from src.days.day05.a import Day05PartAController
from src.days.day05.b import Day05PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay05(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day05PartAController()

    def get_controller_b(self) -> Controller:
        return Day05PartBController()
