

def solve1():
    with open('input.txt', 'r') as f:
        setup_lines: list[str] = []
        line = f.readline()
        while line.strip():
            setup_lines.append(line)
            line = f.readline()

        stacks_count = int(setup_lines[-1].rstrip()[-1])
        stacks: list[list[str]] = [[] for _ in range(stacks_count)]

        for i in reversed(range(len(setup_lines)-1)):
            for j in range(stacks_count):
                crate = setup_lines[i][j*4+1]
                if crate != ' ':
                    stacks[j].append(crate)

        while line := f.readline().rstrip():
            move, frm, to = map(int, filter(lambda el: el.isdigit(), line.split(' ')))
            for _ in range(move):
                stacks[to-1].append(stacks[frm-1].pop())

        print("".join([s[-1] for s in stacks]))


def solve2():
    with open('input.txt', 'r') as f:
        setup_lines: list[str] = []
        line = f.readline()
        while line.strip():
            setup_lines.append(line)
            line = f.readline()

        stacks_count = int(setup_lines[-1].rstrip()[-1])
        stacks: list[list[str]] = [[] for _ in range(stacks_count)]

        for i in reversed(range(len(setup_lines)-1)):
            for j in range(stacks_count):
                crate = setup_lines[i][j*4+1]
                if crate != ' ':
                    stacks[j].append(crate)

        while line := f.readline().rstrip():
            move, frm, to = map(int, filter(lambda el: el.isdigit(), line.split(' ')))

            # buffer method
            buffer: list[str] = []
            for _ in range(move):
                buffer.append(stacks[frm-1].pop())
            for _ in range(move):
                stacks[to-1].append(buffer.pop())

            # concatenation method
            # stacks[to-1] += stacks[frm-1][-move:]
            # stacks[frm-1] = stacks[frm-1][:-move]

        print("".join([s[-1] for s in stacks]))


solve1()
solve2()
