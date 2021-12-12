#!/usr/bin/python3

from typing import List


class Octopus:
    flash_counter = 0

    def __init__(self, value: int) -> None:
        self.has_flashed = False
        self.value = value


def flash(x: int, y: int, octopuses: List[List[Octopus]]):
    octopuses[y][x].has_flashed = True
    Octopus.flash_counter += 1
    if x > 0 and y > 0 and not octopuses[y-1][x-1].has_flashed:
        octopuses[y-1][x-1].value += 1
        if octopuses[y-1][x-1].value > 9:
            flash(x-1, y-1, octopuses)
    if x > 0 and not octopuses[y][x-1].has_flashed:
        octopuses[y][x-1].value += 1
        if octopuses[y][x-1].value > 9:
            flash(x-1, y, octopuses)
    if x > 0 and y + 1 < len(octopuses) and not octopuses[y+1][x-1].has_flashed:
        octopuses[y+1][x-1].value += 1
        if octopuses[y+1][x-1].value > 9:
            flash(x-1, y+1, octopuses)
    if y + 1 < len(octopuses) and not octopuses[y+1][x].has_flashed:
        octopuses[y+1][x].value += 1
        if octopuses[y+1][x].value > 9:
            flash(x, y+1, octopuses)
    if y + 1 < len(octopuses) and x + 1 < len(octopuses[0]) and not octopuses[y+1][x+1].has_flashed:
        octopuses[y+1][x+1].value += 1
        if octopuses[y+1][x+1].value > 9:
            flash(x+1, y+1, octopuses)
    if x + 1 < len(octopuses[0]) and not octopuses[y][x+1].has_flashed:
        octopuses[y][x+1].value += 1
        if octopuses[y][x+1].value > 9:
            flash(x+1, y, octopuses)
    if y > 0 and x + 1 < len(octopuses[0]) and not octopuses[y-1][x+1].has_flashed:
        octopuses[y-1][x+1].value += 1
        if octopuses[y-1][x+1].value > 9:
            flash(x+1, y-1, octopuses)
    if y > 0 and not octopuses[y-1][x].has_flashed:
        octopuses[y-1][x].value += 1
        if octopuses[y-1][x].value > 9:
            flash(x, y-1, octopuses)


def solve1():
    with open('input.txt', 'r') as f:
        inputgrid: List[List[int]] = []
        octopuses: List[List[Octopus]] = []

        for line in f:
            inputgrid = map(int, list(line.rstrip()))
            octopuses.append([Octopus(o) for o in inputgrid])
        width = len(octopuses[0])
        height = len(octopuses)

        for _ in range(100):
            for y in range(height):
                for x in range(width):
                    octopuses[y][x].value += 1
            for y in range(height):
                for x, octo in enumerate(octopuses[y]):
                    if octo.value > 9 and not octo.has_flashed:
                        flash(x, y, octopuses)
            for y in range(height):
                for x, octo in enumerate(octopuses[y]):
                    if octo.has_flashed:
                        octo.value = 0
                        octo.has_flashed = False

        print(Octopus.flash_counter)


def solve2():
    with open('input.txt', 'r') as f:
        inputgrid: List[List[int]] = []
        octopuses: List[List[Octopus]] = []

        for line in f:
            inputgrid = map(int, list(line.rstrip()))
            octopuses.append([Octopus(o) for o in inputgrid])
        width = len(octopuses[0])
        height = len(octopuses)

        step_counter = 0
        while True:
            step_counter += 1
            for y in range(height):
                for x in range(width):
                    octopuses[y][x].value += 1
            for y in range(height):
                for x, octo in enumerate(octopuses[y]):
                    if octo.value > 9 and not octo.has_flashed:
                        flash(x, y, octopuses)
            for y in range(height):
                for x, octo in enumerate(octopuses[y]):
                    if octo.has_flashed:
                        octo.value = 0
                        octo.has_flashed = False
            all_flashed = True
            for y in range(height):
                for x, octo in enumerate(octopuses[y]):
                    if octo.value != 0:
                        all_flashed = False
            if all_flashed:
                break
        print(step_counter)


solve1()
solve2()
