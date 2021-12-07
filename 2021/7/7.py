#!/usr/bin/python3

from typing import List


def solve1():
    with open('input.txt', 'r') as f:
        content = f.readline()
        crabs = [int(c) for c in content.split(',')]
        crab_counts = [0]*(max(crabs)+1)
        for crab in crabs:
            crab_counts[crab] += 1

        fuel_needs: List[int] = []
        for i in range(len(crab_counts)):
            fuel_need = 0
            for j in range(len(crab_counts)):
                if j == i:
                    continue
                fuel_need += abs(i-j)*crab_counts[j]
            fuel_needs.append(fuel_need)

        print(min(fuel_needs))


def solve2():
    with open('input.txt', 'r') as f:
        content = f.readline()
        crabs = [int(c) for c in content.split(',')]
        crab_counts = [0]*(max(crabs)+1)
        for crab in crabs:
            crab_counts[crab] += 1

        fuel_needs: List[int] = []
        for i in range(len(crab_counts)):
            fuel_need = 0
            for j in range(len(crab_counts)):
                if j == i:
                    continue
                dist = abs(i-j)
                fuel_need += int(dist*(dist+1)/2*crab_counts[j])
            fuel_needs.append(fuel_need)

        print(min(fuel_needs))


solve1()
solve2()
