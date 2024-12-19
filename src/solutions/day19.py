from src.tools.loader import load_data
from collections import defaultdict

TESTING = False


def parse_input(data):
    patterns = set(tuple(data[0].split(", ")))
    goals = tuple(data[1].split("\n"))

    return patterns, goals


def count_possibilities(patterns, towels):
    count_if_possible = 0
    count_number_of_ways = 0

    for towel in towels:
        is_doable = False
        part_of_towels = set([pattern for pattern in patterns if towel.startswith(pattern)])
        number_of_ways = defaultdict(int)
        number_of_ways.update({pattern: 1 for pattern in part_of_towels})

        while part_of_towels:
            part_of_towel = min(part_of_towels, key=len)
            part_of_towels.remove(part_of_towel)

            for pattern in patterns:
                index = len(part_of_towel)
                if towel[index:].startswith(pattern):
                    part_of_towels.add(part_of_towel + pattern)
                    number_of_ways[part_of_towel + pattern] += number_of_ways[part_of_towel]
                if part_of_towel == towel:
                    is_doable = True

        if is_doable:
            count_if_possible += 1
            count_number_of_ways += number_of_ways[towel]

    return count_if_possible, count_number_of_ways


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    patterns, towels = parse_input(data)
    count_if_possible, count_number_of_ways = count_possibilities(patterns, towels)

    # PART 1
    # test:     6
    # answer: 367
    print(count_if_possible)

    # PART 2
    # test:                16
    # answer: 724388733465031
    print(count_number_of_ways)
