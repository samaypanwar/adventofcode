import re
from collections import defaultdict
from typing import List, DefaultDict

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

Coord = tuple[int, int]
GridType = DefaultDict[Coord, int]
LinePositions = tuple[Coord, Coord]
Line = List[Coord]
line_pattern = re.compile(r'(\d+)')


def is_horizontal(line: LinePositions) -> bool:
    start, end = line
    return start[0] == end[0]


def is_vertical(line: LinePositions) -> bool:
    start, end = line
    return start[1] == end[1]


def is_diagonal(line: LinePositions) -> bool:
    return not is_vertical(line) and not is_horizontal(line)


def get_line(positions: LinePositions) -> Line:
    start, end = positions

    x1, y1 = start
    x2, y2 = end

    dx = bool(x2 > x1) - bool(x2 < x1)
    dy = bool(y2 > y1) - bool(y2 < y1)

    return [(x1 + n * dx, y1 + n * dy) for n in range(max(abs(x2 - x1), abs(y2 - y1)) + 1)]


def get_lines(positions_list: List[LinePositions]) -> List[Line]:
    for positions in positions_list:
        yield get_line(positions)


def count_intersections(parsed_input: List[LinePositions]) -> int:
    seen: DefaultDict[Coord, int] = defaultdict(int)

    for line in get_lines(parsed_input):
        for coord in line:
            seen[coord] += 1

    return len([value for value in seen.values() if value > 1])


def parse_input(input_data: List[str], filter_diagonal: bool = True) -> List[LinePositions]:
    lines: List[LinePositions] = []

    for line in input_data:
        x1, y1, x2, y2 = map(int, line_pattern.findall(line))
        parsed_line = ((x1, y1), (x2, y2))

        if filter_diagonal and is_diagonal(parsed_line):
            continue

        lines.append(parsed_line)

    return lines


@solution_timer(2021, 5, 1)
def part_one(input_data: List[str]):
    parsed_input = parse_input(input_data)
    answer = count_intersections(parsed_input)

    if not answer:
        raise SolutionNotFoundException(2021, 5, 1)

    return answer


@solution_timer(2021, 5, 2)
def part_two(input_data: List[str]):
    parsed_input = parse_input(input_data, filter_diagonal=False)
    answer = count_intersections(parsed_input)

    if not answer:
        raise SolutionNotFoundException(2021, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 5)
    part_one(data)
    part_two(data)
