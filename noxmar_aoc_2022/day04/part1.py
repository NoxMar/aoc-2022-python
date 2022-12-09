from typing import TextIO, Generator
import re
from sys import stdin
from dataclasses import dataclass


@dataclass
class SimpleRange:
    start: int
    end: int

    def __contains__(self, other: "SimpleRange"):
        return self.start >= other.start and self.end <= other.end


_input_regex = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def ranges_from_file(
    input_file: TextIO,
) -> Generator[tuple[SimpleRange, SimpleRange], None, None]:
    for line in input_file:
        start1, end1, start2, end2 = _input_regex.match(line).groups()
        yield SimpleRange(int(start1), int(end1)), SimpleRange(int(start2), int(end2))


def contains_symmetric(range1: SimpleRange, range2: SimpleRange) -> bool:
    return range1 in range2 or range2 in range1


def solution(input_file: TextIO) -> int:
    return sum(contains_symmetric(*r) for r in ranges_from_file(input_file))


if __name__ == "__main__":
    print(solution(stdin))
