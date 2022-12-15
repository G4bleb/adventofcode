
# Used for type hinting within class
import math
import re
from typing import TypeVar

PointType = TypeVar("PointType", bound="Point")


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __str__(self) -> str:
        return str(self.tuple())

    def dist(self, other: PointType) -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Sensor(Point):
    def __init__(self, x: int, y: int, beacon: Point) -> None:
        super().__init__(x, y)
        self.beacon = beacon
        self.dist_from_beacon = self.dist(beacon)

    def in_range(self, other: Point) -> bool:
        return self.dist(other) <= self.dist_from_beacon


class Tunnels:
    def __init__(self) -> None:
        self.sensors: list[Sensor] = []
        self.occupied: set[tuple[int, int]] = set()

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)
        self.occupied.add(sensor.tuple())
        self.occupied.add(sensor.beacon.tuple())

    def get_coverage(self, y: int, min_x: int, max_x: int) -> int:
        counter = 0
        for x in range(min_x, max_x):
            if (x, y) not in self.occupied:
                for s in self.sensors:
                    if s.in_range(Point(x, y)):
                        counter += 1
                        break
        return counter


def solve1() -> None:
    pattern = re.compile(r"x=(-?\d+), y=(-?\d+)")
    t = Tunnels()

    with open('input.txt', 'r') as f:
        inpt = f.read()
    it = re.finditer(pattern, inpt)

    min_x = math.inf
    max_x = -math.inf

    for res in it:
        sensor_x, sensor_y = map(int, res.groups())
        beacon_x, beacon_y = map(int, next(it).groups())
        beacon = Point(beacon_x, beacon_y)
        sensor = Sensor(sensor_x, sensor_y, beacon)
        min_x = min(min_x, sensor.x-sensor.dist_from_beacon)
        max_x = max(max_x, sensor.x+sensor.dist_from_beacon)
        t.add_sensor(sensor)

    # print(t.get_coverage(11, min_x, max_x))
    print(t.get_coverage(2000000, min_x, max_x))


solve1()
