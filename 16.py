import re
import collections

range_pattern = re.compile(r'\d+-\d+')


def solve():
    f = open('16', 'r')
    lines = f.readlines()
    ranges = []
    start = 0
    for i in range(len(lines)):
        if lines[i] == '\n':
            print(i)
            start = i+1
            break
        matches = re.findall(range_pattern, lines[i])
        for match in matches:
            ranges.append(list(map(int, match.split('-'))))
    print(ranges)

    checker = collections.defaultdict(bool)
    for r in ranges:
        for i in range(r[0], r[1]+1):
            checker[i] = True
    print(start)
    for i in range(start+1, len(lines)):
        if lines[i] == '\n':
            start = i+1
            break
        pass

    total = 0
    for i in range(start+1, len(lines)):
        numbers = map(int, lines[i].split(','))
        for n in numbers:
            if not checker[n]:
                total += n

    print(total)


print(solve())
