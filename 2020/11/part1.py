import common


def resolvePart1():
    f = open('11', 'r')
    lines = [list(line.strip()) for line in f.readlines()]
    f.close()
    tmp = iteratePart1(lines)
    while tmp != lines:
        lines = tmp
        tmp = iteratePart1(lines)
    return common.countOccupied(lines)


def iteratePart1(lines):
    nextlines = lines.copy()
    for i in range(len(lines)):
        nextlines[i] = lines[i].copy()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'L' and adjacentSeatsFree(lines, i, j):
                nextlines[i][j] = '#'
            elif lines[i][j] == '#' and adjacentSeatsOccupied(lines, i, j):
                nextlines[i][j] = 'L'
            else:
                nextlines[i][j] = lines[i][j]
    return nextlines


def adjacentSeatsFree(lines, i, j):
    return (
        not occupied(lines, i-1, j-1) and
        not occupied(lines, i+1, j+1) and
        not occupied(lines, i+1, j-1) and
        not occupied(lines, i-1, j+1) and
        not occupied(lines, i-1, j) and
        not occupied(lines, i+1, j) and
        not occupied(lines, i, j-1) and
        not occupied(lines, i, j+1)
    )


def adjacentSeatsOccupied(lines, i, j):
    return (
        occupied(lines, i-1, j-1) +
        occupied(lines, i+1, j+1) +
        occupied(lines, i+1, j-1) +
        occupied(lines, i-1, j+1) +
        occupied(lines, i-1, j) +
        occupied(lines, i+1, j) +
        occupied(lines, i, j-1) +
        occupied(lines, i, j+1) >= 4
    )


def occupied(lines, i, j):
    if -1 < i < len(lines) and -1 < j < len(lines[i]):
        return lines[i][j] == '#'
    else:
        return False


print(resolvePart1())
