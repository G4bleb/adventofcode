from typing import TypeVar

# Used for type hinting within Assignment class
AssignmentType = TypeVar("AssignmentType", bound="Assignment")


class Assignment:
    def __init__(self, start: str, end: str):
        self.start = int(start)
        self.end = int(end)

    def is_within(self, other: AssignmentType) -> bool:
        return self.start >= other.start and self.end <= other.end

    def overlaps_with(self, other: AssignmentType) -> bool:
        return not ((
            self.end < other.start
        ) or (
            self.start > other.end
        ))


def solve1():
    with open('input.txt', 'r') as f:
        total = 0
        while line := f.readline().rstrip():

            pair: list[Assignment] = []
            for str_assignment in line.split(','):
                start, end = str_assignment.split('-')
                pair.append(Assignment(start, end))

            if pair[0].is_within(pair[1]) or pair[1].is_within(pair[0]):
                total += 1

    print(total)


def solve2():
    with open('input.txt', 'r') as f:
        total = 0
        while line := f.readline().rstrip():

            pair: list[Assignment] = []
            for str_assignment in line.split(','):
                start, end = str_assignment.split('-')
                pair.append(Assignment(start, end))

            if pair[0].overlaps_with(pair[1]):
                total += 1

    print(total)


solve1()
solve2()
