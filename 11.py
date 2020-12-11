def resolvePart1():
    f = open('11', 'r')
    lines = [list(line.strip()) for line in f.readlines()]
    f.close()

    tmp = iterate(lines)
    while tmp != lines:
        lines = tmp
        tmp = iterate(lines)
    return countOccupied(lines)


def iterate(lines):
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


def printLines(lines):
    print('\n'.join([''.join(line) for line in lines]), end='\n\n')


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


def countOccupied(lines):
    count = 0
    for line in lines:
        count += line.count('#')
    return count


print(resolvePart1())
