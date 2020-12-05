#!/usr/bin/python3

def resolvePart1():
    f = open('2', 'r')
    lines = f.readlines()
    rightcount = 0
    for line in lines:
        numbers, chkletter, pw = line.split(' ')
        bot, top = map(int, numbers.split('-'))
        chkletter = chkletter[0]
        lettercount = 0
        for pwletter in pw:
            if chkletter == pwletter:
                lettercount += 1
        if bot <= lettercount <= top:
            rightcount += 1
    return rightcount


def resolvePart2():
    f = open('2', 'r')
    lines = f.readlines()
    rightcount = 0
    for line in lines:
        numbers, chkletter, pw = line.strip().split(' ')
        bot, top = map(int, numbers.split('-'))
        chkletter = chkletter[0]
        if (chkletter == pw[bot-1] and chkletter != pw[top-1]) or (chkletter == pw[top-1] and chkletter != pw[bot-1]):
            rightcount += 1
    return rightcount


print(resolvePart2())
