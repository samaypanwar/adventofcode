import os
import sys

import pytest

from adventofcode.year_2015.day_10_2015 import (
    iterate,
    part_two,
    part_one,
    get_input_for_day,
)


@pytest.mark.skipif(sys.version_info > (3, 10))
@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
        ("3113322113", "132123222113"),
        ("132123222113", "111312111213322113"),
    ],
)
def test_iterate(value, expected):
    assert expected == iterate(value)


def test_part_one():
    assert part_one(get_input_for_day(2015, 10)) == 329356


@pytest.mark.skipif(
    sys.version_info >= (3, 11),
    os.getenv("CI", False),
    reason="For some reason, this test takes 23 minutes on 3.11 in Github Actions, but runs fine on earlier versions",
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 10)) == 4666278
