
def resolvePart1():
    f = open('9', 'r')
    lines = list(map(int, f.readlines()))
    f.close()
    ok = True
    i = 24
    while i < len(lines) and ok:
        i += 1
        ok = testSum(lines, i)
    return lines[i]


def testSum(lines, i):
    for j in range(i-25, i):
        for k in range(i-25, i):
            if k != j:
                if lines[j] + lines[k] == lines[i]:
                    return True
    return False


def resolvePart2():
    f = open('9', 'r')
    lines = list(map(int, f.readlines()))
    toFind = resolvePart1()
    i = 0
    while i < len(lines):
        total = 0
        j = i - 1
        while total < toFind:
            j += 1
            total += lines[j]
        if total == toFind:
            return min(lines[i:j]) + max(lines[i:j])
        i += 1
    return "Failed"


print(resolvePart1())
print(resolvePart2())
