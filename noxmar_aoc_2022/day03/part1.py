from typing import TextIO, Generator, Iterable

from sys import stdin


def get_rucksacks(input_file: TextIO) -> Generator[tuple[str, str], None, None]:
    for line in input_file:
        line = line.rstrip()
        mid_index = len(line) // 2
        yield line[:mid_index], line[mid_index:]


def common_letter(rucksack: Iterable[str]) -> str:
    rucksacks_iter = iter(rucksack)
    encountered_letters = set(next(rucksacks_iter))
    encountered_letters.intersection_update(*rucksacks_iter)
    return encountered_letters.pop()


def letter_to_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27


def solution(input_file: TextIO) -> int:
    return sum(letter_to_priority(common_letter(r)) for r in get_rucksacks(input_file))


if __name__ == "__main__":
    print(solution(stdin))
