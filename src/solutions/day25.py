from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    locks = []
    keys = []

    for grid in data:
        lines = grid.split("\n")
        width = len(lines[0])
        is_lock = True if "." not in lines[0] else False

        pins = [0 for _ in range(width)]

        for line in lines:
            for j, el in enumerate(line):
                if is_lock and el == "#" or not is_lock and el == ".":
                    pins[j] += 1

        if is_lock:
            locks.append(pins)
        else:
            keys.append(pins)

    return locks, keys


def count_fititng_keys(lock, key):
    counter = 0

    for lock in locks:
        for key in keys:
            found = True
            for i in range(len(lock)):
                if key[i] < lock[i]:
                    found = False

            if found:
                counter += 1

    return counter


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    locks, keys = parse_input(data)

    # PART 1
    # test:      3
    # answer: 2586
    print(count_fititng_keys(locks, keys))
