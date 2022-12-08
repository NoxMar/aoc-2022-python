from typing import Generator, TextIO

from enum import IntEnum
from sys import stdin


class Shape(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(IntEnum):
    Loss = 0
    Draw = 3
    Win = 6


opponent_choice_code = {"A": Shape.Rock, "B": Shape.Paper, "C": Shape.Scissors}
my_choice_code = {"X": Shape.Rock, "Y": Shape.Paper, "Z": Shape.Scissors}


def get_outcome(opponent_choice: Shape, my_choice: Shape) -> Outcome:
    if my_choice == opponent_choice:
        return Outcome.Draw

    if my_choice == Shape.Rock:
        return Outcome.Win if opponent_choice == Shape.Scissors else Outcome.Loss
    elif my_choice == Shape.Paper:
        return Outcome.Win if opponent_choice == Shape.Rock else Outcome.Loss
    else:
        return Outcome.Win if opponent_choice == Shape.Paper else Outcome.Loss


def score_game(opponent_choice: Shape, my_choice: Shape) -> int:
    outcome = get_outcome(opponent_choice, my_choice)
    return my_choice.value + outcome.value


def rps_games(
    input_file: TextIO,
) -> Generator[tuple[Shape, Shape], None, None]:
    for line in input_file:
        line = line.rstrip()
        opponent_choice, my_choice = line.split(" ")
        yield opponent_choice_code[opponent_choice], my_choice_code[my_choice]


def solution(input_file: TextIO) -> int:
    games = rps_games(input_file)
    return sum(score_game(*g) for g in games)


if __name__ == "__main__":
    print(solution(stdin))
