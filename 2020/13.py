import math


def resolvePart1():
    f = open('13', 'r')
    ready, timetable_line = f.readlines()
    ready = int(ready)
    timetable = []

    for time_line in timetable_line.split(','):
        if time_line.isdigit():
            timetable.append(int(time_line))

    wait, i = math.inf, 0
    wait_index = -1
    while i < len(timetable):
        tmp = -1 * (ready % timetable[i] - timetable[i])
        # print(timetable[i], '-->', tmp)
        if tmp < wait:
            wait = tmp
            wait_index = i
        i += 1

    return timetable[wait_index] * (-1 * (ready % timetable[wait_index] - timetable[wait_index]))


print(resolvePart1())
