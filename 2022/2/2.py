def solve1():
    OUTCOMES = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    my_score = 0
    for line in lines:
        my_score += OUTCOMES[line]
    print(my_score)


def solve2():
    OUTCOMES = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }

    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    my_score = 0
    for line in lines:
        my_score += OUTCOMES[line]
    print(my_score)


solve1()
solve2()
