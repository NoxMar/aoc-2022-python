import os

from noxmar_aoc_2022.day04 import part1, part2

this_dir = os.path.dirname(os.path.abspath(__file__))


def test_part1_data_from_problem_statement():
    test_data = open(this_dir + "/test-data-day-04.txt", "r")
    assert part1.solution(test_data) == 2


def test_part2_data_from_problem_statement():
    test_data = open(this_dir + "/test-data-day-04.txt", "r")
    assert part2.solution(test_data) == 4
