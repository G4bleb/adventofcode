#!/usr/bin/python3

from typing import List


def solve1():
    with open('input.txt', 'r') as f:
        heightmap: List[List[int]] = []
        risk_level_sum = 0
        for line in f:
            heightmap.append(list(map(int, list(line.rstrip()))))
        width = len(heightmap[0])
        height = len(heightmap)
        for y in range(height):
            for x, point in enumerate(heightmap[y]):
                if x > 0 and heightmap[y][x-1] <= point:
                    continue
                if x + 1 < width and heightmap[y][x+1] <= point:
                    continue
                if y > 0 and heightmap[y-1][x] <= point:
                    continue
                if y + 1 < height and heightmap[y+1][x] <= point:
                    continue
                risk_level_sum += point+1
        print(risk_level_sum)


class Point:
    def __init__(self, height: int) -> None:
        self.height = height
        self.inBasin = False


class Basin:
    def __init__(self, start_x: int, start_y: int, pointmap: List[List[Point]]) -> None:
        self.value: List[Point] = []
        self.findBasin(start_x, start_y, pointmap)

    def findBasin(self, x: int, y: int, pointmap: List[List[Point]]) -> int:
        if pointmap[y][x].inBasin:
            return
        pointmap[y][x].inBasin = True
        self.value.append(pointmap[y][x])
        if x > 0 and pointmap[y][x-1].height < 9:
            self.findBasin(x-1, y, pointmap)
        if x + 1 < len(pointmap[y]) and pointmap[y][x+1].height < 9:
            self.findBasin(x+1, y, pointmap)
        if y > 0 and pointmap[y-1][x].height < 9:
            self.findBasin(x, y-1, pointmap)
        if y + 1 < len(pointmap) and pointmap[y+1][x].height < 9:
            self.findBasin(x, y+1, pointmap)


def solve2():
    with open('input.txt', 'r') as f:
        pointmap: List[List[Point]] = []
        basins_sizes: List[int] = []
        for line in f:
            heightmapline = map(int, list(line.rstrip()))
            pointmap.append([Point(h) for h in heightmapline])
        width = len(pointmap[0])
        height = len(pointmap)
        for y in range(height):
            for x, point in enumerate(pointmap[y]):
                if x > 0 and pointmap[y][x-1].height <= point.height:
                    continue
                if x + 1 < width and pointmap[y][x+1].height <= point.height:
                    continue
                if y > 0 and pointmap[y-1][x].height <= point.height:
                    continue
                if y + 1 < height and pointmap[y+1][x].height <= point.height:
                    continue
                if not point.inBasin:
                    found = Basin(x, y, pointmap)
                    basins_sizes.append(len(found.value))
        top3_basins = ((sorted(basins_sizes, reverse=True)[:3]))
        answer = 1
        for b in top3_basins:
            answer *= b
        print(answer)


solve1()
solve2()
