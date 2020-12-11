def resolvePart1():
    f = open('10', 'r')
    lines = list(map(int, f.readlines()))
    f.close()
    joltage = 0
    diff_cnt = [0, 0, 0]
    lines.sort()
    for adapter in lines:
        diff = adapter - joltage
        diff_cnt[diff-1] += 1
        joltage += diff
    diff_cnt[2] += 1
    return diff_cnt[0]*diff_cnt[2]


print(resolvePart1())
