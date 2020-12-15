def solve(playing, end):
    memory = {}
    i = 1
    for n in playing:
        memory[n] = (0, i)
        i += 1

    consider = playing[-1]
    turn = len(playing) + 1
    while turn <= end:
        # print("Turn", turn, "considering", consider)
        # print(memory[consider])

        if memory[consider][0] == 0:
            consider = 0
        else:
            consider = memory[consider][1]-memory[consider][0]
        try:
            memory[consider] = (memory[consider][1], turn)
        except KeyError:
            memory[consider] = (0, turn)

        # print("Saying", consider)
        turn += 1
    return consider


print(solve([11, 18, 0, 20, 1, 7, 16], 2020))
print(solve([11, 18, 0, 20, 1, 7, 16], 30000000))
