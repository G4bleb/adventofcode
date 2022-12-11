

from io import TextIOWrapper
from math import floor
from dataclasses import dataclass


class Operation:
    def __init__(self, operator: str, increment: int | None) -> None:
        self.inc = increment
        self.addition = False  # Multiplication
        if operator == '+':
            self.addition = True

    def do_operation(self, old: int) -> int:
        to_add = self.inc if self.inc else old
        if self.addition:
            return old + to_add
        else:
            return old * to_add


@dataclass
class Package:
    recipient: int
    item: int


class MonkeyPartOne:
    def __init__(self, f: TextIOWrapper) -> None:
        self.inspect_counter = 0
        self.items = [int(item) for item in f.readline().split(':')[1].split(',')]
        operation_inpt = f.readline().split('old ')[1].split(' ')
        if operation_inpt[1].startswith('old'):
            self.operation = Operation(operation_inpt[0], None)
        else:
            self.operation = Operation(operation_inpt[0], int(operation_inpt[1]))
        self.test = int(f.readline().split('by ')[1])
        self.if_true = int(f.readline().split('key ')[1])
        self.if_false = int(f.readline().split('key ')[1])

    def turn(self) -> list[Package]:
        packages: list[Package] = []
        for item in self.items:
            self.inspect_counter += 1
            item = self.operation.do_operation(item)
            item = floor(item/3)
            if not (item % self.test):
                packages.append(Package(self.if_true, item))
            else:
                packages.append(Package(self.if_false, item))
        self.items = []
        return packages


def solve1():
    monkeys: list[MonkeyPartOne] = []
    with open('input.txt', 'r') as f:
        while next(f, False):
            monkeys.append(MonkeyPartOne(f))
            next(f, False)

    for _ in range(20):
        for m in monkeys:
            packages = m.turn()
            for p in packages:
                monkeys[p.recipient].items.append(p.item)

    monkeys.sort(key=lambda m: m.inspect_counter, reverse=True)
    print(monkeys[0].inspect_counter * monkeys[1].inspect_counter)


solve1()
