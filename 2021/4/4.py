#!/usr/bin/python3


from typing import List


class BingoNumber:
    def __init__(self, value: int) -> None:
        self.value = value
        self.checked = False

    def check(self) -> None:
        self.checked = True


class BingoBoard:
    def __init__(self) -> None:
        self.value: List[List[BingoNumber]] = []

    def add_line(self, line: List[BingoNumber]) -> None:
        self.value.append(line)

    def winner(self) -> bool:
        size = len(self.value)

        for i in range(size):
            checked_streak = 0
            for j in range(size):
                if self.value[i][j].checked:
                    checked_streak += 1
            if checked_streak == size:
                return True
        for j in range(size):
            checked_streak = 0
            for i in range(size):
                if self.value[i][j].checked:
                    checked_streak += 1
            if checked_streak == size:
                return True
        return False

    def get_sum_of_unchecked_numbers(self) -> int:
        total = 0
        for line in self.value:
            for number in line:
                if not number.checked:
                    total += number.value
        return total


def solve1():
    with open('input.txt', 'r') as f:
        drawn_numbers: List[int] = [int(n) for n in f.readline().split(',')]
        boards: List[BingoBoard] = []

        for _ in f:
            boards.append(BingoBoard())
            for _ in range(5):
                board_line = [BingoNumber(int(n)) for n in f.readline().split()]
                boards[-1].add_line(board_line)

        for drawn in drawn_numbers:

            for board in boards:
                for board_line in board.value:
                    for checkable_number in board_line:
                        if checkable_number.value == drawn:
                            checkable_number.check()
            for board in boards:
                if board.winner():
                    print(board.get_sum_of_unchecked_numbers() * drawn)
                    return


def solve2():
    with open('input.txt', 'r') as f:
        drawn_numbers: List[int] = [int(n) for n in f.readline().split(',')]
        boards: List[BingoBoard] = []

        for _ in f:
            boards.append(BingoBoard())
            for _ in range(5):
                board_line = [BingoNumber(int(n)) for n in f.readline().split()]
                boards[-1].add_line(board_line)

        for drawn in drawn_numbers:
            for board in boards:
                for board_line in board.value:
                    for checkable_number in board_line:
                        if checkable_number.value == drawn:
                            checkable_number.check()
            for board in boards:
                if board.winner():
                    if len(boards) > 1:
                        boards.remove(board)
                    else:
                        print(board.get_sum_of_unchecked_numbers() * drawn)
                        return


solve1()
solve2()
