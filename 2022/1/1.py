#!/usr/bin/python3

import bisect


def solve1():
    with open('input.txt', 'r') as f:
        lines = list(f.readlines())

    maxelf = 0
    tmp = 0
    for line in lines:
        if line == '\n':
            maxelf = max(tmp, maxelf)
            tmp = 0
        else:
            tmp += int(line)
    maxelf = max(tmp, maxelf)

    print(maxelf)


def solve2():
    with open('input.txt', 'r') as f:
        lines = list(f.readlines())

    elves: list[int] = []
    curr_elf = 0
    for line in lines:
        if line == '\n':
            bisect.insort(elves, curr_elf)
            curr_elf = 0
        else:
            curr_elf += int(line)
    bisect.insort(elves, curr_elf)

    print(sum(elves[-3:]))


solve1()
solve2()
