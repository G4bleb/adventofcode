import re
from itertools import pairwise


class Point:
    @classmethod
    def get_minmax_from_input(cls) -> None:
        cls.max_x = 500
        cls.min_x = 500
        cls.max_y = 0
        cls.min_y = 0

        pattern = re.compile(r"(\d+),(\d+)")
        with open('input.txt', 'r') as f:
            inpt = f.read()
        it = re.finditer(pattern, inpt)
        for res in it:
            x, y = map(int, res.groups())
            cls.max_x = max(cls.max_x, x)
            cls.min_x = min(cls.min_x, x)
            cls.max_y = max(cls.max_y, y)
            # cls.min_y = min(cls.min_y, y)

    def __init__(self, x: int, y: int, scaling: bool = False) -> None:
        if scaling:
            self.x = x - Point.min_x
            self.y = y - Point.min_y
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f"({self.x + Point.min_x},{self.y + Point.min_y})"


class Cave:
    def __init__(self) -> None:
        height = Point.max_y - Point.min_y + 1
        width = Point.max_x - Point.min_x + 1

        self.mat: list[list[str]] = []
        for _ in range(height):
            self.mat.append(['.']*width)

    def trace_wall(self, wall: str) -> None:
        points: list[Point] = [
            Point(int(p[0]), int(p[1]), scaling=True)
            for p in [pair.split(',') for pair in wall.split(" -> ")]
        ]
        for start, end in pairwise(points):
            curr = Point(start.x, start.y)
            if start.x == end.x:
                while curr.y < end.y:
                    self.mat[curr.y][curr.x] = '#'
                    curr.y += 1
                while curr.y > end.y:
                    self.mat[curr.y][curr.x] = '#'
                    curr.y -= 1
            else:  # start.y == end.y
                while curr.x < end.x:
                    self.mat[curr.y][curr.x] = '#'
                    curr.x += 1
                while curr.x > end.x:
                    self.mat[curr.y][curr.x] = '#'
                    curr.x -= 1
            self.mat[curr.y][curr.x] = '#'

    def drop_sand(self) -> bool:
        s = Point(500, 0, scaling=True)
        if self.mat[s.y][s.x] == 'o':
            return False
        try:
            while True:
                if self.mat[s.y+1][s.x] == '.':
                    s.y = s.y+1
                    continue
                if self.mat[s.y+1][s.x-1] == '.':
                    s.y = s.y+1
                    s.x = s.x-1
                    continue
                if self.mat[s.y+1][s.x+1] == '.':
                    s.y = s.y+1
                    s.x = s.x+1
                    continue
                break
            self.mat[s.y][s.x] = 'o'
            return True
        except:
            return False

    def __str__(self) -> str:
        s = ""
        for row in self.mat:
            s += "".join(row) + "\n"
        return s


def solve1() -> None:
    Point.get_minmax_from_input()
    c = Cave()
    with open('input.txt', 'r') as f:
        while line := f.readline():
            c.trace_wall(line)
    counter = 0
    while c.drop_sand():
        counter += 1

    # print(c)
    print(counter)


def solve2() -> None:
    Point.get_minmax_from_input()
    Point.min_x = min(Point.min_x, 250)
    Point.max_x = max(Point.max_x, 750)
    Point.max_y = Point.max_y + 2

    c = Cave()
    c.trace_wall(f"250,{Point.max_y} -> 750,{Point.max_y}")

    with open('input.txt', 'r') as f:
        while line := f.readline():
            c.trace_wall(line)
    counter = 0
    while c.drop_sand():
        counter += 1

    # print(c)
    print(counter)


solve1()
solve2()
