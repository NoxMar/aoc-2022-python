from typing import Generator, Iterator, TextIO, Iterable, Callable, TypeVar

from dataclasses import dataclass
from collections import deque
from itertools import chain
import re
from sys import stdin

# This solution generally assumes that create names consist of ONE letter (as per
# string.isalpha) since that was the case for the test data and my puzzle input,
# however I can't find that specified anywhere in the problem statement.

T = TypeVar("T", bound=Iterable)


def tokenize_line(line: str) -> Generator[str, None, None]:
    token_start_indexes = range(0, len(line), 4)
    return (line[si : si + 3].strip("[]") for si in token_start_indexes)


def place_initial_line(
    stacks: list[T],
    line_tokens: Iterator[str],
    stack_factory: Callable[[], T] = deque,
) -> None:
    boxes = ((idx, token) for idx, token in enumerate(line_tokens) if token.isalpha())
    for idx, content in boxes:
        if idx >= len(stacks):
            stacks.extend(stack_factory() for _ in range(idx - len(stacks) + 1))
        stacks[idx].appendleft(content)


def initial_state_from_file(
    source: TextIO, stack_factory: Callable[[], T] = deque
) -> tuple[T, ...]:
    stacks: list[T] = []
    for line in source:
        line = line.rstrip()
        if any(c.isdigit() for c in line):  # stack numbering line
            next(source)  # skipping empty separator line
            break
        place_initial_line(stacks, tokenize_line(line), stack_factory=stack_factory)
    return stacks


@dataclass
class MoveInstruction:
    from_idx: int
    to_idx: int
    count: int


def preform_move(stacks: Iterable[T], instruction: MoveInstruction):
    for _ in range(instruction.count):
        stacks[instruction.to_idx].append(stacks[instruction.from_idx].pop())


_move_instruction_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_instruction(line: str) -> MoveInstruction:
    groups = _move_instruction_regex.match(line).groups()
    count, from_idx, to_idx = int(groups[0]), int(groups[1]) - 1, int(groups[2]) - 1
    return MoveInstruction(from_idx, to_idx, count)


def solution(
    source: TextIO,
    stack_factory: Callable[[], T] = deque,
    move_performer: Callable[[Iterable[T], MoveInstruction], None] = preform_move,
) -> str:
    stacks = initial_state_from_file(source, stack_factory=stack_factory)
    for instruction in (parse_instruction(line) for line in source):
        move_performer(stacks, instruction)
    return "".join(s[-1] if s else " " for s in stacks)


if __name__ == "__main__":
    print(solution(stdin))
