import argparse
import aocd
import os
from code_gen.file_data import FileData
from code_gen.templates.part_template import PART_TEMPLATE
from code_gen.templates.solver_template import SOLVER_TEMPLATE
from code_gen.templates.test_template import TEST_TEMPLATE


def touch_file(path: str) -> None:
    open(path, "x")


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content.strip() + "\n")


def create_files(file_data: FileData) -> None:
    if not os.path.isdir(file_data.directory):
        os.makedirs(file_data.directory)
        touch_file(file_data.src_init_file)
        write_file(file_data.input_file, aocd.get_data(year=2017, day=file_data.day))
        write_file(
          file_data.solver_file,
          SOLVER_TEMPLATE.format(day_string=file_data.day_string),
        )
        write_file(
          file_data.test_file, 
          TEST_TEMPLATE.format(day_string=file_data.day_string)
        )
        for part in ['a', 'b']:
          file_data.part = part
          write_file(
            file_data.part_file,
            PART_TEMPLATE.format(
                year=2017,
                day_int = int(file_data.day_string),
                day_string=file_data.day_string,
                part=part,
                part_upper=part.upper(),
            ),
          )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("-d", "--day", type=int, help="Day to create files for")

    return parser


if __name__ == "__main__":
    args = create_parser().parse_args()

    file_data = FileData(day=args.day, part='a')

    create_files(file_data)
