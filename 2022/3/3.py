def letter_to_priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter)-38
    else:
        return ord(letter)-96


def solve1():
    with open('input.txt', 'r') as f:
        total = 0
        while line := f.readline().rstrip():

            half_index = int(len(line)/2)
            first_pouch = set(line[:half_index])
            second_pouch = set(line[half_index:])

            for obj in first_pouch:
                if obj in second_pouch:
                    total += letter_to_priority(obj)
                    break
    print(total)


def solve2():
    with open('input.txt', 'r') as f:
        bags = [set(line.rstrip()) for line in f.readlines()]

    total = 0
    for i in range(0, len(bags), 3):
        group = bags[i:i+3]

        for obj in group[0]:
            if obj in group[1]:
                if obj in group[2]:
                    total += letter_to_priority(obj)
                    break

    print(total)


solve1()
solve2()
