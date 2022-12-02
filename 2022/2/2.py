def solve1():
    outcomes = {
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
        my_score = 0
        while line := f.readline():
            game = line.rstrip()
            my_score += outcomes[game]
    print(my_score)


def solve2():
    outcomes = {
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
        my_score = 0
        while line := f.readline():
            game = line.rstrip()
            my_score += outcomes[game]
    print(my_score)


solve1()
solve2()
