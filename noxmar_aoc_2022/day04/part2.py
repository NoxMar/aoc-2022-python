from typing import TextIO
from sys import stdin

from noxmar_aoc_2022.day04.part1 import ranges_from_file


def solution(input_file: TextIO) -> int:
    return sum(r1.overlaps(r2) for r1, r2 in ranges_from_file(input_file))


if __name__ == "__main__":
    print(solution(stdin))
