from typing import TextIO, Generator
from sys import stdin

from noxmar_aoc_2022.day02.part1 import (
    Outcome,
    Shape,
    get_outcome,
    opponent_choice_code,
    score_game,
)

outcome_code = {"X": Outcome.Loss, "Y": Outcome.Draw, "Z": Outcome.Win}

choice_for_outcome = {(op, get_outcome(op, my)): my for op in Shape for my in Shape}


def rps_guide_rows(input_file: TextIO) -> Generator[tuple[Shape, Outcome], None, None]:
    for line in input_file:
        line = line.rstrip()
        opponent_choice, desired_outcome = line.split(" ")
        yield opponent_choice_code[opponent_choice], outcome_code[desired_outcome]


def score_for_guide_row(opponent_choice: Shape, desired_outcome: Outcome) -> int:
    my_choice = choice_for_outcome[(opponent_choice, desired_outcome)]
    return score_game(opponent_choice, my_choice)


def solution(input_file: TextIO) -> int:
    return sum(score_for_guide_row(*gr) for gr in rps_guide_rows(input_file))


if __name__ == "__main__":
    print(solution(stdin))
