#!/usr/bin/python3

from typing import List, Tuple


class Line:
    def __init__(self, file_line: str) -> None:
        start, end = file_line.split(' -> ')
        self.x1, self.y1 = [int(coord) for coord in start.split(',')]
        self.x2, self.y2 = [int(coord) for coord in end.split(',')]

    # https://stackoverflow.com/questions/25837544/get-all-points-of-a-straight-line-in-python
    def get_points(self) -> Tuple[int, int]:
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        points = []
        issteep = abs(y2-y1) > abs(x2-x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2-y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points


class Diagram:
    def __init__(self) -> None:
        self.lines: List[Line] = []
        self.width = 0
        self.height = 0

    def add_line(self, line: Line) -> None:
        self.lines.append(line)
        self.width = max(self.width, line.x1, line.x2)
        self.height = max(self.height, line.y1, line.y2)

    def create_diagram(self) -> None:
        self.value: List[List[int]] = []
        for _ in range(self.height + 1):
            self.value.append([0]*(self.width + 1))
        for line in self.lines:
            for point in line.get_points():
                self.value[point[1]][point[0]] += 1

    def get_number_of_intersections(self) -> int:
        count = 0
        for line in self.value:
            for intersection in line:
                if intersection > 1:
                    count += 1
        return count


def solve1():
    diagram = Diagram()
    with open('input.txt', 'r') as f:
        for file_line in f:
            line = Line(file_line)
            if line.x1 == line.x2 or line.y1 == line.y2:
                diagram.add_line(line)
        diagram.create_diagram()
        print(diagram.get_number_of_intersections())


def solve2():
    diagram = Diagram()
    with open('input.txt', 'r') as f:
        for file_line in f:
            line = Line(file_line)
            diagram.add_line(line)
        diagram.create_diagram()
        print(diagram.get_number_of_intersections())


solve1()
solve2()
