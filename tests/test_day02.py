import os

from noxmar_aoc_2022.day02 import part1
from noxmar_aoc_2022.day02 import part2


this_dir = os.path.dirname(os.path.abspath(__file__))


def test_part1_data_from_problem_statement():
    test_data = open(this_dir + "/test-data-day-02.txt", "r")
    assert part1.solution(test_data) == 15


def test_part2_data_from_problem_statement():
    test_data = open(this_dir + "/test-data-day-02.txt", "r")
    assert part2.solution(test_data) == 12
