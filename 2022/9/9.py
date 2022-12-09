import math


def distance(p: tuple[int, int], q: tuple[int, int]):
    return math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)


def step(point: tuple[int, int], direction: str) -> tuple[int, int]:
    match direction:
        case 'R':
            return (point[0]+1, point[1])
        case 'U':
            return (point[0], point[1]+1)
        case 'L':
            return (point[0]-1, point[1])
        case 'D':
            return (point[0], point[1]-1)
        case _:
            return point


def solve1() -> None:
    with open('input.txt', 'r') as f:
        H = (0, 0)
        T = (0, 0)
        visited: set[tuple] = {(0, 0)}
        while line := f.readline():
            move = line.rstrip().split(' ')
            direction = move[0]
            steps = int(move[1])
            for _ in range(steps):
                if distance(T, step(H, direction)) >= 2:
                    T = H
                    visited.add(T)
                H = step(H, direction)
        print(len(visited))


def get_new_tail_spot(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    if distance(tail, head) > 1.5:
        if head[0] == tail[0]:
            return (tail[0], tail[1]+1) if head[1] > tail[1] else (tail[0], tail[1]-1)
        if head[1] == tail[1]:
            return (tail[0]+1, tail[1]) if head[0] > tail[0] else (tail[0]-1, tail[1])
        if head[0] > tail[0] and head[1] > tail[1]:
            return (tail[0]+1, tail[1]+1)
        if head[0] > tail[0] and head[1] < tail[1]:
            return (tail[0]+1, tail[1]-1)
        if head[0] < tail[0] and head[1] > tail[1]:
            return (tail[0]-1, tail[1]+1)
        if head[0] < tail[0] and head[1] < tail[1]:
            return (tail[0]-1, tail[1]-1)
    return tail


def print_rope(rope: list[tuple[int, int]]) -> None:
    # Works as long as coordinates are not negative (ok for debugging purposes)
    max_x = max(rope, key=lambda s: s[0])[0]
    max_y = max(rope, key=lambda s: s[1])[1]
    for y in range(-1, max_y + 2):
        for x in range(-1, max_x + 2):
            if (x, y) in rope:
                print('x', end="")
            else:
                print('.', end="")
        print()
    print()


def solve2() -> None:
    with open('input.txt', 'r') as f:
        rope = [(0, 0)]*10
        tail_visited: set[tuple] = {(0, 0)}
        while line := f.readline():
            move = line.rstrip().split(' ')
            direction = move[0]
            steps = int(move[1])
            for _ in range(steps):
                rope[0] = step(rope[0], direction)
                for i in range(1, len(rope)):
                    new_spot = get_new_tail_spot(rope[i-1], rope[i])
                    if rope[i] == new_spot:
                        break
                    rope[i] = new_spot
                    if i == len(rope)-1:
                        tail_visited.add(rope[i])

        print(len(tail_visited))


solve1()
solve2()
