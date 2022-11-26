import dataclasses
from typing import Literal, Union


@dataclasses.dataclass
class FileData(object):
    """Dataclass to handle any directory/file names
    to be used when bootstrapping files
    """

    day: int
    part: Union[Literal["a"], Literal["b"]]

    @property
    def day_string(self) -> str:
        return f"{self.day:02d}"

    @property
    def directory(self) -> str:
        return f"src/day{self.day_string}"

    @property
    def input_file(self) -> str:
        return f"{self.directory}/input.txt"

    @property
    def part_file(self) -> str:
        return f"{self.directory}/{self.part}.py"

    @property
    def solver_file(self) -> str:
        return f"{self.directory}/solver.py"

    @property
    def test_file(self) -> str:
        return f"{self.directory}/test_day{self.day_string}.py"

    @property
    def src_init_file(self) -> str:
        return self._init_file(self.directory)

    def _init_file(self, directory: str) -> str:
        return f"{directory}/__init__.py"