#!/usr/bin/python3

from typing import List, Tuple


class Fish:
    def __init__(self, counter=8) -> None:
        self.counter = counter

    def iterate(self) -> bool:
        self.counter -= 1
        if self.counter < 0:
            self.counter = 6
            return True
        return False


class Flock:
    def __init__(self) -> None:
        self.value: List[Fish] = []

    def iterate(self):
        newborns: List[Fish] = []
        for fish in self.value:
            birth = fish.iterate()
            if birth:
                newborns.append(Fish())
        self.value += newborns


def solve1():
    flock = Flock()

    with open('input.txt', 'r') as f:
        content = f.readline()
        for s in content.split(','):
            flock.value.append(Fish(int(s)))

        for _ in range(80):
            flock.iterate()
        print(len(flock.value))


solve1()
