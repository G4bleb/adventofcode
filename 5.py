def splitListInHalf(to_split, keep_lower_half):
    middle = len(to_split)//2
    if(keep_lower_half):
        return to_split[:middle]
    else:
        return to_split[middle:]


def getSeatId(seat_str):
    possible_rows = list(range(128))
    for rowchar in seat_str[:7]:
        possible_rows = splitListInHalf(possible_rows, rowchar == 'F')
    row = possible_rows[0]
    possible_cols = list(range(8))
    for colchar in seat_str[7:]:
        possible_cols = splitListInHalf(possible_cols, colchar == 'L')
    col = possible_cols[0]
    return row*8+col


def resolvePart1():
    f = open('5', 'r')
    lines = [line.strip() for line in f.readlines()]
    highest = 0
    for line in lines:
        highest = max(highest, getSeatId(line))
    return highest


def resolvePart2():
    f = open('5', 'r')
    lines = [line.strip() for line in f.readlines()]
    seat_ids = []
    for line in lines:
        seat_ids.append(getSeatId(line))

    for seat_id in seat_ids:
        if seat_id-2 in seat_ids and seat_id-1 not in seat_ids:
            return seat_id-1
        elif seat_id+2 in seat_ids and seat_id+1 not in seat_ids:
            return seat_id+1


print(resolvePart1())
print(resolvePart2())
