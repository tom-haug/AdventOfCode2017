from src.day03.a import Day03PartAController
from src.day03.b import Day03PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay03(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day03PartAController()

    def get_controller_b(self) -> Controller:
        return Day03PartBController()
