from src.tools.loader import load_data
from collections import defaultdict

TESTING = False


def get_next(position, grid, max_x, max_y):
    i, j = position
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < max_x and 0 <= ny < max_y and grid[nx][ny] == ".":
            return (nx, ny), False
        if grid[nx][ny] == "E":
            return (nx, ny), True


def solve_part_1(grid, max_x, max_y):
    done = False
    current = [(i, j) for i in range(max_x) for j in range(max_y) if grid[i][j] == "S"][0]
    counter = 0

    while not done:
        grid[current[0]][current[1]] = counter
        current, done = get_next(current, grid, max_x, max_y)
        if done:
            grid[current[0]][current[1]] = counter + 1
        counter += 1

    count_diffs = defaultdict(int)

    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if type(el) != int:
                continue
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x = i + 2 * dx
                new_y = j + 2 * dy
                if 0 <= new_x < max_x and 0 <= new_y < max_y and type(grid[new_x][new_y]) == int:
                    difference = grid[new_x][new_y] - grid[i][j]
                    if difference > 0:
                        count_diffs[difference - 2] += 1

    counter = 0
    for key, val in count_diffs.items():
        threshold = 1 if TESTING else 100
        if key >= threshold:
            counter += val

    return counter


def solve_part_2(grid, max_x, max_y):
    feasible_pairs = set()
    new_diffs = defaultdict(int)

    for i in range(max_x):
        for j in range(max_y):
            if type(grid[i][j]) != int:
                continue
            for n in range(-20, 21):
                for m in range(-20 + abs(n), 21 - abs(n)):
                    assert abs(n) + abs(m) <= 20
                    if i + n >= max_x or j + m >= max_y or i + n < 0 or j + m < 0:
                        continue
                    if type(grid[i + n][j + m]) != int:
                        continue
                    if grid[i + n][j + m] - grid[i][j] < 0:
                        continue
                    if ((i + n, j + m), (i, j), n + m) not in feasible_pairs:
                        feasible_pairs.add(((i + n, j + m), (i, j), abs(n) + abs(m)))
                        new_diffs[grid[i + n][j + m] - grid[i][j] - abs(n) - abs(m)] += 1

    counter = 0
    for key, val in new_diffs.items():
        threshold = 50 if TESTING else 100
        if key >= threshold:
            counter += val

    return counter


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = [[el for el in line] for line in data]
    max_x = len(grid)
    max_y = len(grid[0])

    # PART 1
    # test:     44
    # answer: 1369
    print(solve_part_1(grid, max_x, max_y))

    # PART 2
    # test:      285
    # answer: 979012
    print(solve_part_2(grid, max_x, max_y))
