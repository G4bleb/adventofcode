#!/usr/bin/python3

import re

MANDATORY_KEYS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
ECL_POSSIBILITIES = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def passport_from_paragraph(paragraph):
    passport_lines = paragraph.split('\n')
    # print(passport_lines)
    passport_fields = []
    for line in passport_lines:
        for field in line.split(' '):
            passport_fields.append(field)
    # print(passport_fields)
    passport_dict = {}
    for field in passport_fields:
        k, v = field.split(':')
        passport_dict[k] = v
    return passport_dict


def resolvePart1():
    f = open('4', 'r')
    paragraphs = f.read().split('\n\n')
    validcount = 0
    for paragraph in paragraphs:
        passport = passport_from_paragraph(paragraph)
        if all(key in passport for key in MANDATORY_KEYS):
            validcount += 1
    return validcount


def resolvePart2():
    f = open('4', 'r')
    paragraphs = f.read().split('\n\n')
    validcount = 0
    for paragraph in paragraphs:
        passport = passport_from_paragraph(paragraph)
        try:
            if not (1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030):
                continue

            hgt_ok = False
            if passport['hgt'][-2:] == 'cm':
                if 150 <= int(passport['hgt'][:-2]) <= 193:
                    hgt_ok = True
            elif passport['hgt'][-2:] == 'in':
                if 59 <= int(passport['hgt'][:-2]) <= 76:
                    hgt_ok = True
            if not hgt_ok:
                continue

            if not re.match(r"^#[0-9a-f]{6}$", passport['hcl']):
                continue

            if not passport['ecl'] in ECL_POSSIBILITIES:
                continue

            if not (passport['pid'].isdigit() and len(passport['pid']) == 9):
                continue
            validcount += 1
        except Exception:
            pass
    return validcount


print(resolvePart1())
print(resolvePart2())
