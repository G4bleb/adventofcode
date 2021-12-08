#!/usr/bin/python3

from typing import List


def number_from_letters(word: str) -> int:
    if len(word) == 2:
        return 1
    if len(word) == 3:
        return 7
    if len(word) == 4:
        return 4
    if len(word) == 7:
        return 8
    return 0


def solve1():
    with open('input.txt', 'r') as f:
        counts = [0]*10
        for line in f:
            left, right = line.split('|')
            numbers = right.split()
            for word in numbers:
                counts[number_from_letters(word)] += 1
        print(counts[1]+counts[4]+counts[7]+counts[8])


def find_top_segment_letter(one: str, seven: str) -> str:
    sev_list = list(seven)
    for letter in list(one):
        sev_list.remove(letter)
    return sev_list[0]


def substract_numbers_one_segment(bigger: str, smaller: str) -> str:
    word_list = list(bigger)
    for letter in list(smaller):
        if letter in word_list:
            word_list.remove(letter)
        else:
            break
    if len(word_list) == 1:
        return word_list[0]
    return None


def substract_numbers_list(bigger: str, smaller: str) -> List[str]:
    word_list = list(bigger)
    for letter in list(smaller):
        if letter in word_list:
            word_list.remove(letter)
    return word_list


def match_found_list_with_right_number(found_lists: List[List[str]], right_number: List[str]) -> int:
    for (k, found) in enumerate(found_lists):
        if found == right_number:
            return k


def solve2():

    with open('input.txt', 'r') as f:

        outputs: List[int] = []
        for line in f:
            found = ['']*10
            segments = {'a': '', 'b': '', 'c': '',  'd': '', 'e': '',  'f': '', 'g': ''}
            left, right = line.split('|')
            left_numbers = left.split()
            numbers: List[str] = []

            # find obvious numbers 1,4,7,8
            for word in left_numbers:
                number_found = number_from_letters(word)
                if number_found != 0:
                    found[number_from_letters(word)] = word
                else:
                    numbers.append(word)

            # find top segment
            segments['a'] = find_top_segment_letter(found[1], found[7])

            # find bottom segment and 9
            one_segment_missing_from_nine = found[4]+segments['a']
            for word in numbers:
                remain = substract_numbers_one_segment(word, one_segment_missing_from_nine)
                if remain:
                    segments['g'] = remain
                    found[9] = word
            numbers.remove(found[9])

            # find bottom left segment
            segments['e'] = substract_numbers_one_segment(found[8], found[9])

            # find 3, 5 and top right segment
            three_and_five: List[str] = []
            for word in numbers:
                if not segments['e'] in word:
                    remain = substract_numbers_one_segment(found[9], word)
                    if remain:
                        three_and_five.append(word)
            for i in range(2):
                remain = substract_numbers_list(found[1], three_and_five[i])
                if len(remain) == 1:
                    segments['c'] = remain[0]
                    found[5] = three_and_five[i]
                    found[3] = three_and_five[int(not i)]
                    break
            numbers.remove(found[5])
            numbers.remove(found[3])

            # find top right segment
            segments['b'] = substract_numbers_list(found[5], found[3])[0]

            # find middle segment
            segments['d'] = substract_numbers_one_segment(found[8], found[7]+segments['b']+segments['e']+segments['g'])

            # find last segment : bottom left
            for k in segments.keys():
                if k not in segments.values():
                    segments['f'] = k
                    break

            # find 0
            sorted_0 = substract_numbers_list(found[8], segments['d'])
            sorted_0.sort()
            for word in numbers:
                word_list = list(word)
                word_list.sort()

                if word_list == sorted_0:
                    found[0] = word
                    break
            numbers.remove(found[0])
            del sorted_0

            # find 6
            sorted_6 = substract_numbers_list(found[8], segments['c'])
            sorted_6.sort()
            for word in numbers:
                word_list = list(word)
                word_list.sort()

                if word_list == sorted_6:
                    found[6] = word
                    break
            numbers.remove(found[6])
            del sorted_6

            # find 2
            found[2] = numbers[0]
            del numbers

            # everything found
            right_numbers = right.split()
            found_lists = [list(f) for f in found]
            right_numbers_lists = [list(n) for n in right_numbers]

            [l.sort() for l in found_lists]
            [l.sort() for l in right_numbers_lists]

            # compute output
            output = 0
            output += match_found_list_with_right_number(found_lists, right_numbers_lists[0])*1000
            output += match_found_list_with_right_number(found_lists, right_numbers_lists[1])*100
            output += match_found_list_with_right_number(found_lists, right_numbers_lists[2])*10
            output += match_found_list_with_right_number(found_lists, right_numbers_lists[3])

            outputs.append(output)
        print(sum(outputs))


solve1()
solve2()
