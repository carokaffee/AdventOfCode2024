from src.tools.loader import load_data

TESTING = True


def get_neighbours(position, maze):
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbours = [(x + dx, y + dy) for dx, dy in directions if maze[x + dx][y + dy] != "#"]
    return neighbours


if __name__ == "__main__":
    maze = load_data(TESTING, "\n")
    print(maze)

    for i, row in enumerate(maze):
        for j, el in enumerate(maze):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "E":
                end = (i, j)

    print(start, end)
    current_direction = (0, 1)

    shortest_paths = dict()
    previous = dict()
    for i, row in enumerate(maze):
        for j, el in enumerate(row):
            if el != "#":
                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    shortest_paths[((i, j), dir)] = None
                    previous[((i, j), dir)] = []
    shortest_paths[(start, current_direction)] = 0
    # previous[(start, current_direction)] = 1

    # print(shortest_paths)

    queue = [(start, current_direction)]
    found = False

    while queue:
        queue = sorted(queue, key=shortest_paths.__getitem__)
        (x, y), current_direction = queue.pop(0)
        dx, dy = current_direction
        neighbours = get_neighbours((x, y), maze)
        for nx, ny in neighbours:
            next_direction = (nx - x, ny - y)
            rotation = next_direction != current_direction

            if shortest_paths[((nx, ny), next_direction)] is None:
                if not rotation:
                    shortest_paths[((nx, ny), next_direction)] = shortest_paths[((x, y), current_direction)] + 1
                    queue.append(((nx, ny), next_direction))
                else:
                    shortest_paths[((nx, ny), next_direction)] = shortest_paths[((x, y), current_direction)] + 1001
                    queue.append(((nx, ny), next_direction))
                previous[((nx, ny), next_direction)] = [((x, y), current_direction)]
            else:
                if not rotation:
                    if shortest_paths[((x, y), current_direction)] + 1 < shortest_paths[((nx, ny), current_direction)]:
                        shortest_paths[((nx, ny), current_direction)] = shortest_paths[((x, y), current_direction)] + 1
                        queue.append(((nx, ny), current_direction))
                        previous[((nx, ny), current_direction)] = [((x, y), current_direction)]
                    elif (
                        shortest_paths[((x, y), current_direction)] + 1 == shortest_paths[((nx, ny), current_direction)]
                    ):
                        previous[((nx, ny), current_direction)] += [((x, y), current_direction)]
                else:
                    if shortest_paths[((x, y), current_direction)] + 1001 < shortest_paths[((nx, ny), next_direction)]:
                        shortest_paths[((nx, ny), next_direction)] = shortest_paths[((x, y), current_direction)] + 1001
                        queue.append(((nx, ny), (nx - x, ny - y)))
                        previous[((nx, ny), next_direction)] = [((x, y), current_direction)]
                    elif (
                        shortest_paths[((x, y), current_direction)] + 1001 == shortest_paths[((nx, ny), next_direction)]
                    ):
                        previous[((nx, ny), next_direction)] += [((x, y), current_direction)]

    shortest = 2**1000
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (end, dir) in shortest_paths.keys():
            print("end, dir", shortest_paths[(end, dir)])
            if shortest_paths[(end, dir)] is not None:
                if shortest_paths[(end, dir)] < shortest:
                    shortest = shortest_paths[(end, dir)]
                    shortest_coord = (end, dir)

    print("Sol Part 1: ", shortest)

    involved_points = set([end])
    queue = [(end, dir)]

    while queue:
        current = queue.pop(0)
        (x, y), dir = current
        involved_points.add((x, y))
        for prev in previous[current]:
            queue.append(prev)

    print("Sol Part 2: ", len(involved_points))

    # 535
