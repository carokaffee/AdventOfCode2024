from src.tools.loader import load_data

TESTING = False
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
START_DIR = (0, 1)


def find_start_and_end(maze):
    start = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == "S"][0]
    end = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == "E"][0]
    return start, end


def get_neighbours(position, maze):
    x, y = position
    neighbours = [(x + dx, y + dy) for dx, dy in DIRECTIONS if maze[x + dx][y + dy] != "#"]
    return neighbours


def initialize(maze, start):
    paths = dict()
    previous = dict()

    for i, row in enumerate(maze):
        for j, el in enumerate(row):
            if el == "#":
                continue
            for dir in DIRECTIONS:
                paths[((i, j), dir)] = None
                previous[((i, j), dir)] = []

    paths[(start, START_DIR)] = 0

    return paths, previous


def solve_maze(maze, start, end):
    paths, previous = initialize(maze, start)
    queue = [(start, START_DIR)]

    while queue:
        queue = sorted(queue, key=paths.__getitem__)
        pos = queue.pop(0)
        (x, y), current_dir = pos
        neighbours = get_neighbours((x, y), maze)

        for nx, ny in neighbours:
            next_dir = (nx - x, ny - y)
            next_pos = ((nx, ny), next_dir)
            step_cost = 1001 if next_dir != current_dir else 1
            next_cost = paths[pos] + step_cost

            if paths[next_pos] is None or next_cost < paths[next_pos]:
                paths[next_pos] = next_cost
                queue.append(next_pos)
                previous[next_pos] = [pos]
            elif next_cost == paths[next_pos]:
                previous[next_pos] += [pos]

    shortest_path = min(paths[(end, dir)] for dir in DIRECTIONS if paths[(end, dir)] is not None)
    end_positions = [(end, dir) for dir in DIRECTIONS if paths[(end, dir)] == shortest_path]

    return shortest_path, previous, end_positions


def find_best_path_points(previous, end_positions):
    best_points = set()
    queue = end_positions

    while queue:
        current = queue.pop(0)
        best_points.add(current[0])
        for prev in previous[current]:
            queue.append(prev)

    return len(best_points)


if __name__ == "__main__":
    maze = load_data(TESTING, "\n")
    start, end = find_start_and_end(maze)
    shortest_path, previous, end_positions = solve_maze(maze, start, end)

    # PART 1
    # test:    11048
    # answer: 102504
    print(shortest_path)

    # PART 1
    # test:    64
    # answer: 535
    print(find_best_path_points(previous, end_positions))
