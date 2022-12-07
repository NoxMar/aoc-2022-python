from sys import stdin
from typing import TextIO
import heapq

from .part1 import elf_calories


def solution(input_file: TextIO) -> list[int]:
    return sum(heapq.nlargest(3, elf_calories(input_file)))


if __name__ == "__main__":
    solution(stdin)
