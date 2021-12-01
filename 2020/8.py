def resolvePart1():
    f = open('8', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    executed = {}
    i, acc = 0, 0
    while i < len(lines) and not executed.setdefault(i, False):
        executed[i] = True
        cmd, val = lines[i].split(' ')
        if cmd == 'nop':
            i += 1
        elif cmd == 'acc':
            acc += int(val)
            i += 1
        else:
            i += int(val)
    return acc


def tryProg(lines):
    executed = {}
    i, acc = 0, 0
    while i < len(lines):
        if executed.setdefault(i, False):
            return None
        executed[i] = True
        cmd, val = lines[i].split(' ')
        if cmd == 'nop':
            i += 1
        elif cmd == 'acc':
            acc += int(val)
            i += 1
        else:
            i += int(val)
    return acc


def replaceElem(input_list, index, elem):
    ret = input_list.copy()
    ret[index] = elem
    return ret


def resolvePart2():
    f = open('8', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    i = 0
    while i < len(lines):
        cmd, val = lines[i].split(' ')
        if cmd == 'nop':
            ret = tryProg(replaceElem(lines, i, "jmp "+val))
            if ret:
                return ret
        elif cmd == 'jmp':
            ret = tryProg(replaceElem(lines, i, "nop "+val))
            if ret:
                return ret
        i += 1
    return("Failed")


print(resolvePart1())
print(resolvePart2())
