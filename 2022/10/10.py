
class CPU:
    part_1_cycles = {20, 60, 100, 140, 180, 220}

    def __init__(self, crt=False) -> None:
        self.crt = crt
        self.cycles = 0
        self.x = 1
        self.part_1_answer = 0
        pass

    def cycle(self) -> None:
        self.cycles += 1
        if self.cycles in self.part_1_cycles:
            self.part_1_answer += self.cycles * self.x

        if self.crt:
            if self.cycles % 40 == 1:
                print()
            if self.x <= self.cycles % 40 <= self.x+2:
                print('#', end='')
            else:
                print('.', end='')

    def interpret_instruction(self, instruction: str) -> None:
        if instruction.startswith('noop'):
            self.cycle()
            return
        # addx
        amount = int(instruction.split(' ')[1])
        self.cycle()
        self.cycle()
        self.x += amount


def solve1():
    cpu = CPU()
    with open('input.txt', 'r') as f:
        while line := f.readline():
            cpu.interpret_instruction(line)
    print(cpu.part_1_answer)


def solve2():
    cpu = CPU(crt=True)
    with open('input.txt', 'r') as f:
        while line := f.readline():
            cpu.interpret_instruction(line)
    print()


solve1()
solve2()
