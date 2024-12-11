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


def hike(grid):
    max_x = len(grid)
    max_y = len(grid[0])
    entry_points = ((i, j) for i in range(max_x) for j in range(max_y) if grid[i][j] == 0)
    scores = 0
    ratings = 0

    for entry_point in entry_points:
        end_points = set()
        path_counter = 0
        current = [entry_point]

        while current:
            x, y = current[0]
            current_height = grid[x][y]
            neighbours = get_neighbours((x, y), max_x, max_y)

            for nx, ny in neighbours:
                neighbour_height = grid[nx][ny]
                if neighbour_height == 9 and current_height == 8:
                    end_points.add((nx, ny))
                    path_counter += 1
                elif neighbour_height == current_height + 1:
                    current.append((nx, ny))
            current = current[1:]

        scores += len(end_points)
        ratings += path_counter

    return scores, ratings


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)

    scores, ratings = hike(grid)

    # PART 1
    # test:    36
    # answer: 776
    print(scores)

    # PART 2
    # test:     81
    # answer: 1657
    print(ratings)
