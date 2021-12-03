#!/usr/bin/python3
from typing import List
from functools import reduce


def binary_to_int(binary: List[int]) -> int:
    return int(''.join(map(str, binary)), 2)


def solve1():
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        number_of_bits = len(lines[0])
        bits_counts = [0]*number_of_bits
        for line in lines:
            line_bits = list(map(int, list(line)))
            for i in range(number_of_bits):
                bits_counts[i] += line_bits[i]

        gamma_rate_binary = [int(bcount > len(lines)/2) for bcount in bits_counts]
        epsilon_rate_binary = [int(not gr) for gr in gamma_rate_binary]

        gamma_rate = binary_to_int(gamma_rate_binary)
        epsilon_rate = binary_to_int(epsilon_rate_binary)

        print(gamma_rate*epsilon_rate)


def solve2():
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

        # Initial criterias
        o2_criteria = oxygen_generator_criteria(lines)
        co2_criteria = int(not o2_criteria)

        # Compute o2 rating
        o2_rating_list = list(filter(lambda x: int(x[0]) == o2_criteria, lines))
        i = 0
        while len(o2_rating_list) > 1:
            i += 1
            o2_criteria = oxygen_generator_criteria(o2_rating_list, i)
            o2_rating_list = list(filter(lambda x: int(x[i]) == o2_criteria, o2_rating_list))
        o2_rating_binary = list(map(int, o2_rating_list[0]))
        o2_rating = binary_to_int(o2_rating_binary)

        # Compute co2 rating
        co2_rating_list = list(filter(lambda x: int(x[0]) == co2_criteria, lines))
        i = 0
        while len(co2_rating_list) > 1:
            i += 1
            co2_criteria = int(not oxygen_generator_criteria(co2_rating_list, i))
            co2_rating_list = list(filter(lambda x: int(x[i]) == co2_criteria, co2_rating_list))
        co2_rating_binary = list(map(int, co2_rating_list[0]))
        co2_rating = binary_to_int(co2_rating_binary)

        print(o2_rating*co2_rating)


def oxygen_generator_criteria(lines: List[str], i=0) -> int:  # Could have used regex '^1' instead
    first_bits = [int(l[i]) for l in lines]
    first_bits_count = reduce(lambda x, y: x+y, first_bits)
    return int(first_bits_count >= len(lines)/2)


solve1()
solve2()
