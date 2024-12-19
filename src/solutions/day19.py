from src.tools.loader import load_data
from collections import defaultdict

TESTING = False


def parse_input(data):
    patterns = set(tuple(data[0].split(", ")))
    designs = tuple(data[1].split("\n"))

    return patterns, designs


def count_possibilities(patterns, designs):
    possible_count = 0
    total_arrangements = 0

    for design in designs:
        is_possible = False
        valid_prefixes = set([p for p in patterns if design.startswith(p)])
        arrangements = defaultdict(int, {p: 1 for p in valid_prefixes})

        while valid_prefixes:
            prefix = min(valid_prefixes, key=len)
            valid_prefixes.remove(prefix)

            if prefix == design:
                is_possible = True
                break

            for pattern in patterns:
                next_prefix = prefix + pattern
                if design.startswith(next_prefix):
                    valid_prefixes.add(next_prefix)
                    arrangements[next_prefix] += arrangements[prefix]

        if is_possible:
            possible_count += 1
            total_arrangements += arrangements[design]

    return possible_count, total_arrangements


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    patterns, designs = parse_input(data)
    possible_count, total_arrangements = count_possibilities(patterns, designs)

    # PART 1
    # test:     6
    # answer: 367
    print(possible_count)

    # PART 2
    # test:                16
    # answer: 724388733465031
    print(total_arrangements)
