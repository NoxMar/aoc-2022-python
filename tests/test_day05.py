import os

from noxmar_aoc_2022.day05 import part1

this_dir = os.path.dirname(os.path.abspath(__file__))


def test_part1_data_from_problem_statement():
    test_data = open(this_dir + "/test-data-day-05.txt", "r")
    assert part1.solution(test_data) == "CMZ"
