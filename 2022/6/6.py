from collections import defaultdict


def solve(marker_length):
    offset = marker_length-1
    with open('input.txt', 'r') as f:
        inpt = f.readline().rstrip()

    checker = defaultdict(int)

    for i in range(offset):
        checker[inpt[i]] += 1

    for i in range(offset, len(inpt)):
        checker[inpt[i]] += 1

        if len(checker) == marker_length:
            print(i+1)
            return

        checker[inpt[i-offset]] -= 1
        if not checker[inpt[i-offset]]:
            del checker[inpt[i-offset]]


solve(4)
solve(14)
