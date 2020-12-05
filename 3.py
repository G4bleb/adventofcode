#!/usr/bin/python3

def resolvePart1():
    f = open('3', 'r')
    lines = [line.strip() for line in f.readlines()]
    return checkSlope(lines, 3)


def resolvePart2():
    f = open('3', 'r')
    lines = [line.strip() for line in f.readlines()]
    result = checkSlope(lines, 1)
    result *= checkSlope(lines, 3)
    result *= checkSlope(lines, 5)
    result *= checkSlope(lines, 7)
    result *= checkSlope(lines, 1, 2)
    return result


def checkSlope(lines, right, down=1):
    treecount = 0
    i = 0
    for line in lines[down::down]:
        i += right
        if line[i % len(line)] == '#':
            treecount += 1
    return treecount


print(resolvePart2())
