def printLines(lines):
    print('\n'.join([''.join(line) for line in lines]), end='\n\n')


def countOccupied(lines):
    count = 0
    for line in lines:
        count += line.count('#')
    return count
