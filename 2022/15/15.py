
# Used for type hinting within class
import math
import re
from typing import TypeVar

PointType = TypeVar("PointType", bound="Point")


class Point:
    @classmethod
    def get_minmax_from_input(cls) -> None:
        cls.max_x = 0
        cls.min_x = 0
        cls.max_y = 0
        cls.min_y = 0

        pattern = re.compile(r"x=(-?\d+), y=(-?\d+)")
        with open('input.txt', 'r') as f:
            inpt = f.read()
        it = re.finditer(pattern, inpt)
        for res in it:
            x, y = map(int, res.groups())
            cls.max_x = max(cls.max_x, x)
            cls.min_x = min(cls.min_x, x)
            cls.max_y = max(cls.max_y, y)
            cls.min_y = min(cls.min_y, y)

    def __init__(self, x: int, y: int, scaling: bool = False) -> None:
        if scaling:
            self.x = x - Point.min_x
            self.y = y - Point.min_y
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f"({self.x + Point.min_x},{self.y + Point.min_y})"

    def dist(self, other: PointType) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Sensor(Point):
    def __init__(self, x: int, y: int, beacon: Point, scaling: bool = False) -> None:
        super().__init__(x, y, scaling)
        self.beacon = beacon
        self.dist_from_beacon = self.dist(beacon)

    def in_range(self, other: Point) -> bool:
        return self.dist(other) <= self.dist_from_beacon


class Tunnels:
    def __init__(self) -> None:
        height = Point.max_y - Point.min_y + 1
        width = Point.max_x - Point.min_x + 1

        self.mat: list[list[str]] = []
        for _ in range(height):
            self.mat.append(['.']*width)

        self.sensors: list[Sensor] = []

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)
        self.mat[sensor.y][sensor.x] = 'S'
        self.mat[sensor.beacon.y][sensor.beacon.x] = 'B'

    def build_coverage(self):
        for y in range(len(self.mat)):
            for x in range(len(self.mat[0])):
                if self.mat[y][x] == '.':
                    for s in self.sensors:
                        if s.in_range(Point(x, y)):
                            self.mat[y][x] = '#'
                            break

    def __str__(self) -> str:
        s = ""
        for row in self.mat:
            s += "".join(row) + "\n"
        return s


def solve1() -> None:
    pattern = re.compile(r"x=(-?\d+), y=(-?\d+)")
    Point.get_minmax_from_input()
    t = Tunnels()
    with open('input.txt', 'r') as f:
        inpt = f.read()
    it = re.finditer(pattern, inpt)
    for res in it:
        sensor_x, sensor_y = map(int, res.groups())
        beacon_x, beacon_y = map(int, next(it).groups())
        beacon = Point(beacon_x, beacon_y, scaling=True)
        sensor = Sensor(sensor_x, sensor_y, beacon, scaling=True)
        t.add_sensor(sensor)
    # print(t)
    t.build_coverage()
    # print(t)
    print(t.mat[2000000 - Point.min_y].count('#'))


solve1()
