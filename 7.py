#!/usr/bin/python3

import re


def bagAndItsContainersTypes(bags_containers, contained_name, bag_types):
    for container in bags_containers.setdefault(contained_name, []):
        bagAndItsContainersTypes(bags_containers, container, bag_types)
    bag_types.append(contained_name)


def resolvePart1():
    f = open('7', 'r')
    lines = [line.strip() for line in f.readlines()]
    bags_containers = {}
    for line in lines:
        matches = re.findall(r"(?:^|\d+)([a-z ]+?)bag", line)
        for contained in matches[1:]:
            name = contained[contained.index(' '):].strip()
            bags_containers.setdefault(name, []).append(matches[0].strip())
    # Input : clear purple bags contain 5 faded indigo bags, 3 muted purple bags.
    # Becomes : bags_containers = {'faded indigo': ['clear purple'], 'muted purple': ['clear purple']}
    print(bags_containers['shiny gold'])
    total_containers = []
    bagAndItsContainersTypes(bags_containers, 'shiny gold', total_containers)
    return len(dict.fromkeys(total_containers))-1


def countContainedBagsIncludingThisOne(container_name, bags_contents):
    count = 1
    for contained in bags_contents.setdefault(container_name, []):
        count += contained[0] * \
            countContainedBagsIncludingThisOne(contained[1], bags_contents)
    return count


def resolvePart2():
    f = open('7', 'r')
    lines = [line.strip() for line in f.readlines()]
    bags_contents = {}
    for line in lines:
        matches = re.findall(r"(^|\d+)([a-z ]+?)bag", line)
        container_name = matches[0][1].strip()
        for contained in matches[1:]:
            n = int(contained[0])
            name = contained[1].strip()
            bags_contents.setdefault(container_name, []).append((n, name))
        # Input : clear purple bags contain 5 faded indigo bags, 3 muted purple bags.
        # Becomes : bags_contents = {'clear purple': [(5, 'faded indigo'), (3, 'muted purple')]}
    return countContainedBagsIncludingThisOne('shiny gold', bags_contents)-1


print(resolvePart2())
