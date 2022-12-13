from typing import TextIO, Generator, Optional
from sys import stdin
from noxmar_aoc_2022.day06 import part1


def solution(
    source: TextIO, min_length: int = 14
) -> Generator[Optional[int], None, None]:
    return part1.solution(source, min_length)


if __name__ == "__main__":
    for sol in solution(stdin):
        print(sol)
