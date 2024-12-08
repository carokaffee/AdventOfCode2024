from src.tools.loader import load_data
from collections import defaultdict
from itertools import permutations

TESTING = False


def parse_input(data):
    antennas = defaultdict(list)
    for i, line in enumerate(data):
        for j, el in enumerate(line):
            if el.isalnum():
                antennas[el].append((i,j))
    return antennas


def count_locations(antennas, *, repeat):
    locations = set()

    for el in antennas.keys():
        for (x1,y1), (x2,y2) in permutations(antennas[el], 2):
            dx, dy = x1 - x2, y1 - y2
            if not repeat:
                if x1 + dx in range(len(data)) and y1 + dy in range(len(data[0])):
                    locations.add((x1 + dx, y1 + dy))
            else:
                for n in range(max(len(data), len(data[0]))):
                    if x1 + n * dx in range(len(data)) and y1 + n * dy in range(len(data[0])):
                        locations.add((x1 + n * dx, y1 + n * dy))

    return len(locations)


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    antennas = parse_input(data)
    
    # PART 1
    # test:    14
    # answer: 327
    print(count_locations(antennas, repeat=False))

    # PART 2
    # test:     34
    # answer: 1233
    print(count_locations(antennas, repeat=True))