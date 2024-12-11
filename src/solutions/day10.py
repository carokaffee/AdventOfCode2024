from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    grid = [[int(el) for el in line] for line in data]
    return grid


def get_neighbours(coord, max_x, max_y):
    x, y = coord
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    neighbours = [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < max_x and 0 <= y + dy < max_y]
    return neighbours


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)

    max_x = len(grid)
    max_y = len(grid[0])

    scores = 0
    ratings = 0

    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == 0:
                nine_pos = set()
                counter = 0
                current_pos = [(i, j)]
                while current_pos:
                    u, v = current_pos[0]
                    neighbours = get_neighbours((u, v), max_x, max_y)
                    for x, y in neighbours:
                        if grid[x][y] == 9 and grid[x][y] == grid[u][v] + 1:
                            nine_pos.add((x, y))
                            counter += 1
                        elif grid[x][y] == grid[u][v] + 1:
                            current_pos.append((x, y))
                    current_pos = current_pos[1:]
                scores += len(nine_pos)
                ratings += counter

    # PART 1
    # test:    36
    # answer: 776
    print(scores)

    # PART 2
    # test:     81
    # answer: 1657
    print(ratings)
