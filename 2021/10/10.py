#!/usr/bin/python3

from typing import List

BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}


def is_bracket_opening(bracket: str) -> bool:
    return bracket in BRACKETS


def is_bracket_matching(to_match: str, to_test: str) -> bool:
    return to_test == BRACKETS.get(to_match, None)


def syntax_error_score(illegal_chars: List[str]) -> int:
    CHARS_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for char in illegal_chars:
        score += CHARS_SCORES[char]
    return score


def solve1():
    with open('input.txt', 'r') as f:
        illegal_chars: List[str] = []
        for line in f:
            buffer: List[str] = []
            for char in line.rstrip():
                if is_bracket_opening(char):
                    buffer.append(char)
                elif is_bracket_matching(buffer[-1], char):
                    buffer.pop()
                else:
                    illegal_chars.append(char)
                    break
        print(syntax_error_score(illegal_chars))


def get_closing_bracket(opening_bracket: str) -> str:
    return BRACKETS[opening_bracket]


def get_completion_score(completion_chars: List[str]) -> int:
    CHARS_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for char in completion_chars:
        score *= 5
        score += CHARS_SCORES[char]
    return score


def solve2():
    with open('input.txt', 'r') as f:
        completions_scores: List[int] = []
        for line in f:
            discard = False
            buffer: List[str] = []
            for char in line.rstrip():
                if is_bracket_opening(char):
                    buffer.append(char)
                elif is_bracket_matching(buffer[-1], char):
                    buffer.pop()
                else:
                    discard = True
                    break

            if discard:
                continue

            completion_chars: List[str] = []
            for char in reversed(buffer):
                completion_chars.append(get_closing_bracket(char))
            completions_scores.append(get_completion_score(completion_chars))

        print(sorted(completions_scores)[int(len(completions_scores)/2)])


solve1()
solve2()
