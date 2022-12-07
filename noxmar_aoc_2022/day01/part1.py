from sys import stdin
from typing import Generator, TextIO


def elf_calories(input_file: TextIO) -> Generator[int, None, None]:
    current_elf_calories = 0
    for line in input_file.readlines():
        if line.isspace():
            yield current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)
    yield current_elf_calories


def solution(input_file: TextIO) -> int:
    return max(elf_calories(input_file))


if __name__ == "__main__":
    solution(stdin)
