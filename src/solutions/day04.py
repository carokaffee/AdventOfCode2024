from src.tools.loader import load_data

TESTING = False


def padded_puzzle(puzzle):
    width = len(puzzle[0]) + 8
    padding_line = "." * width
    padded_puzzle = [padding_line] * 4

    for line in puzzle:
        padded_puzzle.append("...." + line + "....")
    padded_puzzle += [padding_line] * 4

    return padded_puzzle


def count_XMAS(puzzle):
    xmas_count = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for x in range(4, len(puzzle) - 3):
        for y in range(4, len(puzzle[0]) - 3):
            for dx, dy in directions:
                xmas = "".join([puzzle[x + dx * n][y + dy * n] for n in range(4)])
                if xmas == "XMAS":
                    xmas_count += 1
    return xmas_count


def count_X_MAS(puzzle):
    down_coords = set()
    up_coords = set()

    for x in range(4, len(puzzle) - 3):
        for y in range(4, len(puzzle[0]) - 3):
            for dx, dy in [(1, 1), (-1, -1)]:
                mas = "".join([puzzle[x + dx * n][y + dy * n] for n in range(3)])
                if mas == "MAS":
                    down_coords.add((x + dx, y + dy))
            for dx, dy in [(1, -1), (-1, 1)]:
                mas = "".join([puzzle[x + dx * n][y + dy * n] for n in range(3)])
                if mas == "MAS":
                    up_coords.add((x + dx, y + dy))

    return len(down_coords.intersection(up_coords))


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    puzzle = padded_puzzle(data)

    # PART 1
    # test:     18
    # answer: 2644
    print(count_XMAS(puzzle))

    # PART 2
    # test:      9
    # answer: 1952
    print(count_X_MAS(puzzle))
