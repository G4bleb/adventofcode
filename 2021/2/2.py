#!/usr/bin/python3


from typing import List, Tuple


def solve1():
    with open('input.txt', 'r') as f:
        splitted_lines = [l.split() for l in list(f.readlines())]
        instructions: List[Tuple[str, int]] = [(i[0], int(i[1])) for i in splitted_lines]
        depth = 0
        hposition = 0
        for command, units in instructions:
            if command == 'forward':
                hposition += units
            elif command == 'down':
                depth += units
            elif command == 'up':
                depth -= units
        print(hposition*depth)


def solve2():
    with open('input.txt', 'r') as f:
        splitted_lines = [l.split() for l in list(f.readlines())]
        instructions: List[Tuple[str, int]] = [(i[0], int(i[1])) for i in splitted_lines]
        depth = 0
        hposition = 0
        aim = 0
        for command, units in instructions:
            if command == 'forward':
                hposition += units
                depth += aim * units
            elif command == 'down':
                aim += units
            elif command == 'up':
                aim -= units
        print(hposition*depth)


solve1()
solve2()
