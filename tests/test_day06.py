from pytest import mark
from io import StringIO
from noxmar_aoc_2022.day06 import part1


@mark.parametrize(
    "packet,expected_start",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part1_data_from_problem_statement(packet: str, expected_start: int):
    assert tuple(part1.solution(StringIO(packet))) == (expected_start,)
