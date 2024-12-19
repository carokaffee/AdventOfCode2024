from src.tools.loader import load_data

TESTING = False

MAX_X = 71 if not TESTING else 7
MAX_Y = 71 if not TESTING else 7

BYTE_LENGTH = 1024 if not TESTING else 12


def parse_input(data):
    bytes = []
    for line in data:
        bytes.append(tuple(map(int, line.split(","))))
    return bytes


def create_grid(bytes):
    bytes_set = set(bytes)
    grid = []

    for i in range(MAX_X):
        line = "".join("#" if (i, j) in bytes_set else "." for j in range(MAX_Y))
        grid.append(line)

    return grid


def get_neighbours(position, grid):
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
    x, y = position
    neighbours = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < MAX_X and 0 <= ny < MAX_Y and grid[nx][ny] != "#":
            neighbours.append((nx, ny))

    return neighbours


def do_dijkstra(grid):
    start = (0, 0)
    end = (MAX_X - 1, MAX_Y - 1)
    queue = [start]
    distances = {(i, j): -1 for i in range(MAX_X) for j in range(MAX_Y)}
    distances[start] = 0

    while queue:
        queue = sorted(queue, key=distances.__getitem__)
        next = queue.pop(0)
        neighbours = get_neighbours(next, grid)

        for nx, ny in neighbours:
            dist_neighbour = distances[(nx, ny)]
            dist_next = distances[(next[0], next[1])]

            if dist_next + 1 < dist_neighbour or dist_neighbour < 0:
                distances[(nx, ny)] = dist_next + 1
                queue.append((nx, ny))

    return distances[end]


def find_shortest_path(bytes):
    grid = create_grid(bytes[:BYTE_LENGTH])
    shortest_path = do_dijkstra(grid)

    return shortest_path


def find_blocking_byte(bytes):
    min_counter = 0
    max_counter = len(bytes)

    while max_counter - min_counter > 1:
        counter = (max_counter + min_counter) // 2
        new_bytes = tuple(bytes[: counter + 1])

        grid = create_grid(new_bytes)
        result = do_dijkstra(grid)

        if result == -1:
            max_counter = counter
        else:
            min_counter = counter

    return bytes[max_counter]


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    bytes = parse_input(data)

    # PART 1
    # test:    22
    # answer: 312
    print(find_shortest_path(bytes))

    # PART 2
    # test:     6,1
    # answer: 28,26
    print(find_blocking_byte(bytes))
