#!/usr/bin/python3

from typing import List


def solve1():
    with open('input.txt', 'r') as f:
        lines = list(f.readlines())

        count = 0
        last = lines[0]
        for i in range(1, len(lines)):
            if int(last) < int(lines[i]):
                count += 1
            last = lines[i]
    print(count)


def get_window_sum(start: int, end: int, lines: List[str]) -> int:
    window_sum = 0
    for i in range(start, end+1):
        window_sum += int(lines[i])
    return window_sum


def solve2():
    with open('input.txt', 'r') as f:
        lines = list(f.readlines())

        last_window_sum = get_window_sum(0, 2, lines)
        count = 0
        for i in range(1, len(lines)-2):
            current_window_sum = get_window_sum(i, i+2, lines)
            if last_window_sum < current_window_sum:
                count += 1
            last_window_sum = current_window_sum
    print(count)


solve1()
solve2()
