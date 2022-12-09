from typing import TextIO, Generator, Iterator, TypeVar
from sys import stdin

from noxmar_aoc_2022.day03.part1 import common_letter, letter_to_priority

T = TypeVar("T")


def _triplewise(it: Iterator[T]) -> Generator[tuple[T, ...], None, None]:
    try:
        while True:
            yield next(it), next(it), next(it)
    except StopIteration:
        pass


def get_groups(input_file: TextIO) -> Generator[tuple[str, str, str], None, None]:
    return _triplewise(l.rstrip() for l in input_file)


def solution(input_file: TextIO) -> int:
    return sum(letter_to_priority(common_letter(g)) for g in get_groups(input_file))


if __name__ == "__main__":
    print(solution(stdin))
