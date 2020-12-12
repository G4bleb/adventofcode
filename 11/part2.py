import common


def resolvePart2():
    f = open('11', 'r')
    lines = [list(line.strip()) for line in f.readlines()]
    f.close()
    tmp = iteratePart2(lines)
    while tmp != lines:
        lines = tmp
        tmp = iteratePart2(lines)
    return common.countOccupied(lines)


def iteratePart2(lines):
    nextlines = lines.copy()
    for i in range(len(lines)):
        nextlines[i] = lines[i].copy()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'L' and adjacentSeatsInSightFree(lines, i, j):
                nextlines[i][j] = '#'
            elif lines[i][j] == '#' and adjacentSeatsInSightOccupied(lines, i, j):
                nextlines[i][j] = 'L'
            else:
                nextlines[i][j] = lines[i][j]
    return nextlines


def adjacentSeatsInSightFree(lines, i, j):
    return (
        not occupiedInSight(lines, i, j, -1, -1) and
        not occupiedInSight(lines, i, j, +1, +1) and
        not occupiedInSight(lines, i, j, +1, -1) and
        not occupiedInSight(lines, i, j, -1, +1) and
        not occupiedInSight(lines, i, j, -1, 0) and
        not occupiedInSight(lines, i, j, +1, 0) and
        not occupiedInSight(lines, i, j, 0, -1) and
        not occupiedInSight(lines, i, j, 0, +1)
    )


def adjacentSeatsInSightOccupied(lines, i, j):
    return (
        occupiedInSight(lines, i, j, -1, -1) +
        occupiedInSight(lines, i, j, +1, +1) +
        occupiedInSight(lines, i, j, +1, -1) +
        occupiedInSight(lines, i, j, -1, +1) +
        occupiedInSight(lines, i, j, -1, 0) +
        occupiedInSight(lines, i, j, +1, 0) +
        occupiedInSight(lines, i, j, 0, -1) +
        occupiedInSight(lines, i, j, 0, +1) >= 5
    )


def occupiedInSight(lines, startI, startJ, dirI, dirJ):
    i, j = startI + dirI, startJ + dirJ
    while -1 < i < len(lines) and -1 < j < len(lines[i]):
        if lines[i][j] == '#':
            return True
        elif lines[i][j] == 'L':
            return False
        i += dirI
        j += dirJ
    return False


print(resolvePart2())
