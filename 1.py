#!/usr/bin/python3

def resolve():
    f = open('1', 'r')
    lines = f.readlines()
    lines = list(map(int, lines))
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                if i != j != k:
                    if lines[i] + lines[j] + lines[k] == 2020:
                        return lines[i] * lines[j] * lines[k]


print(resolve())
