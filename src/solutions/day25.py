from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    locks = []
    keys = []

    for grid in data:
        is_lock = True if "." not in grid.split("\n")[0] else False

        if is_lock:
            locks.append([0 for _ in range(len(grid.split("\n")[0]))])
            for line in grid.split("\n")[1:]:
                for i, el in enumerate(line):
                    if el == "#":
                        locks[-1][i] += 1
        else:
            keys.append([0 for _ in range(len(grid.split("\n")[0]))])
            for line in list(reversed(grid.split("\n")))[1:]:
                for i, el in enumerate(line):
                    if el == "#":
                        keys[-1][i] += 1

    height = len(data[0].split("\n"))

    return locks, keys, height


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    locks, keys, height = parse_input(data)

    count = 0

    for lock in locks:
        for key in keys:
            comb = [0 for _ in range(len(key))]
            found = True
            for i in range(len(lock)):
                comb[i] = lock[i] + key[i]
            for i in range(len(comb)):
                if comb[i] >= height - 1:
                    found = False
            if found:
                count += 1

    print(count)
