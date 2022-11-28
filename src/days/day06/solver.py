from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


class Day06Solver(Solver):
    data: list[int]

    def initialize(self, file_path: str):
        self.data = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> list[int]:
        input = load_text_file(file_path)
        return [int(value) for value in input[0].split("\t")]

    def solve(self) -> int:
        banks = self.data
        bank_hashes: dict[int, int] = dict()

        cur_hash = self.get_hash(banks)
        reallocation_cycle = 0
        while reallocation_cycle == 0 or cur_hash not in bank_hashes:
            bank_hashes[cur_hash] = reallocation_cycle
            reallocation_cycle += 1

            max_bank = self.get_max_bank(banks)
            reallocation = banks[max_bank]
            banks[max_bank] = 0
            cur_bank = max_bank
            while reallocation > 0:
                cur_bank += 1
                if cur_bank >= len(banks):
                    cur_bank = 0
                banks[cur_bank] += 1
                reallocation -= 1
            cur_hash = self.get_hash(banks)
        result = self.get_result(bank_hashes, reallocation_cycle, cur_hash)
        return result

    def get_max_bank(self, banks: list[int]) -> int:
        max_value = max(banks)
        max_index = banks.index(max_value)
        return max_index

    def get_hash(self, banks: list[int]) -> int:
        tup = tuple(banks)
        return hash(tup)

    @abstractmethod
    def get_result(
        self, bank_hashes: dict[int, int], ending_cycle_number: int, ending_hash: int
    ) -> int:
        ...
