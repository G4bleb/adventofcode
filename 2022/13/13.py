import json
from functools import cmp_to_key


def compare(l: int | list, r: int | list) -> 1 | -1 | str:
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return 'continue'
        return -1 if l < r else 1
    if isinstance(l, list) and isinstance(r, list):
        for lv, rv in zip(l, r):
            comparison = compare(lv, rv)
            if comparison != 'continue':
                return comparison
        if len(r) != len(l):
            return -1 if len(r) > len(l) else 1
        return 'continue'
    # One of them is an integer, the other is a list
    if isinstance(l, int):
        l = [l]
    else:
        r = [r]
    return compare(l, r)


def solve1() -> None:
    packet_pair: list[list] = [[],  []]
    i = 0
    res = 0
    with open('input.txt', 'r') as f:
        while line := f.readline():
            i += 1
            packet_pair[0] = json.loads(line)
            packet_pair[1] = json.loads(f.readline())
            left = packet_pair[0]
            right = packet_pair[1]
            next(f, False)
            if compare(left, right) == -1:
                res += i
    print(res)


def solve2() -> None:
    packets = []
    with open('input.txt', 'r') as f:
        while line := f.readline():
            line = line.rstrip()
            if line:
                packets.append(json.loads(line))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    res = 1
    i = 0
    for p in packets:
        i += 1
        if p == [[2]] or p == [[6]]:
            res *= i
    print(res)


solve1()
solve2()
