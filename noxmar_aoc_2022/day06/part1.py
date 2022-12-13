from typing import Optional, TextIO, Generator, TypeVar, Generic, no_type_check
from collections import Counter
from sys import stdin


K = TypeVar("K")


class CounterWithDiscard(Generic[K], Counter[K]):
    def discard(self, value: K) -> None:
        if value not in self:
            return
        self.subtract(value)
        if self[value] == 0:
            del self[value]


def find_first_x_different(s: str, min_length: int = 4) -> Optional[int]:
    chars_to_add = (s[idx] for idx in range(min_length, len(s)))
    chars_to_remove = (s[idx] for idx in range(len(s) - min_length))

    seen_rolling = CounterWithDiscard(s[:min_length])

    if len(seen_rolling) == min_length:
        return 0

    for idx, (to_add, to_discard) in enumerate(zip(chars_to_add, chars_to_remove), 1):
        seen_rolling.discard(to_discard)
        seen_rolling.update(to_add)
        if len(seen_rolling) == min_length:
            return idx + min_length
    return None


def solution(
    source: TextIO, min_length: int = 4
) -> Generator[Optional[int], None, None]:
    for line in (li.rstrip() for li in source):
        yield find_first_x_different(line, min_length)


if __name__ == "__main__":
    for sol in solution(stdin):
        print(sol)
