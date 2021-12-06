#!/usr/bin/python3

from typing import List


def iterateFlock(flock: List[int]):
    newborns = flock[0]
    for i in range(1, 9):
        flock[i-1] = flock[i]
    flock[8] = newborns
    flock[6] += newborns
    return flock


def solve1():
    with open('input.txt', 'r') as f:
        content = f.readline()
        flock = [0]*9
        for s in content.split(','):
            flock[int(s)] += 1

        for _ in range(80):
            flock = iterateFlock(flock)
        print(sum(flock))


def solve2():
    with open('input.txt', 'r') as f:
        content = f.readline()
        flock = [0]*9
        for s in content.split(','):
            flock[int(s)] += 1

        for _ in range(256):
            flock = iterateFlock(flock)
        print(sum(flock))


solve1()
solve2()
