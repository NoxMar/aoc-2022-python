from typing import Iterable, Callable, Iterable, TextIO
from collections import deque
from sys import stdin

from noxmar_aoc_2022.day05 import part1
from noxmar_aoc_2022.day05.part1 import T, MoveInstruction


def perform_move(stacks: Iterable[T], instruction: MoveInstruction):
    to_extend = reversed(
        [stacks[instruction.from_idx].pop() for _ in range(instruction.count)]
    )
    stacks[instruction.to_idx].extend(to_extend)


def solution(
    source: TextIO,
    stack_factory: Callable[[], T] = deque,
    move_performer: Callable[[Iterable[T], MoveInstruction], None] = perform_move,
) -> str:
    return part1.solution(
        source, stack_factory=stack_factory, move_performer=move_performer
    )


if __name__ == "__main__":
    print(solution(stdin))
