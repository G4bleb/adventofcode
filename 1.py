#!/usr/bin/python3
def resolvePart1():
    f = open('1', 'r')
    lines = f.readlines()
    f.close()
    lines = list(map(int, lines))
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                if lines[i] + lines[j] == 2020:
                    return lines[i] * lines[j]


def resolvePart2():
    f = open('1', 'r')
    lines = f.readlines()
    f.close()
    lines = list(map(int, lines))
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                if i != j != k:
                    if lines[i] + lines[j] + lines[k] == 2020:
                        return lines[i] * lines[j] * lines[k]


print(resolvePart1())
print(resolvePart2())
