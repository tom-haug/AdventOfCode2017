from abc import ABC, abstractclassmethod
import argparse
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

        if len(samples) == 0:
            raise Exception(
                f"No sample files setup. Add these to: {self.__class__.__name__}"
            )

        for (file_path, expected_result) in samples:
            solver = self.new_solver()
            solver.initialize(file_path)
            result = solver.solve()
            if result != expected_result:
                raise Exception(
                    f"Test Fail: Sample {file_path}, expecting: {expected_result}, actual: {result}"
                )
            print(f"Test Pass: File: {file_path}, result: {result}")

    def run(self) -> None:
        self.__run_test_inputs()

        solver = self.new_solver()
        file_path = self.file_path()
        self.download_if_not_exists(file_path)
        solver.initialize(file_path)
        result = solver.solve()
        print(f"Result: {result}")
        self.try_submit(result)

    def download_if_not_exists(self, file_path: str):
        if exists(file_path):
            return

        data = get_data(day=self.day, year=self.year)

        with open(file_path, "w") as f:
            f.write(data)

    def try_submit(self, result):
        args = create_parser().parse_args()
        do_submit = args.submit
        if do_submit:
            submit(result, part=self.part, day=self.day, year=self.year)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("-s", "--submit", type=int, help="Submit result if tests pass")

    return parser
