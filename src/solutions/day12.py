from src.tools.loader import load_data

TESTING = False


def get_neighbours(current, max_x, max_y):
    i, j = current
    neighbours = []
    if i + 1 < max_x:
        neighbours.append((i + 1, j))
    if i - 1 >= 0:
        neighbours.append((i - 1, j))
    if j + 1 < max_y:
        neighbours.append((i, j + 1))
    if j - 1 >= 0:
        neighbours.append((i, j - 1))

    return neighbours


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    max_x = len(data)
    max_y = len(data[0])

    visited = set()
    regions = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in visited:
                current_region = {(i, j)}
                queue = [(i, j)]
                visited.add((i, j))
                current = (i, j)
                while queue:
                    u, v = queue[0]
                    for x, y in get_neighbours(queue[0], max_x, max_y):
                        if data[x][y] == data[u][v] and (x, y) not in visited:
                            current_region.add((x, y))
                            visited.add((x, y))
                            queue.append((x, y))
                    queue = queue[1:]
                regions.append(current_region)

    score = 0
    score_part2 = 0

    for region in regions:
        circum = 0
        border = set()
        for i, j in region:
            for x, y in get_neighbours((i, j), max_x, max_y):
                if data[x][y] != data[i][j]:
                    circum += 1
                    if x == i:
                        if y < j:
                            border.add(((i, j), (i + 1, j), "e"))
                        else:
                            border.add(((i, j + 1), (i + 1, j + 1), "w"))
                    if y == j:
                        if x < i:
                            border.add(((i, j), (i, j + 1), "s"))
                        else:
                            border.add(((i + 1, j), (i + 1, j + 1), "n"))
            if i == 0:
                circum += 1
                border.add(((i, j), (i, j + 1), "s"))
            if i == max_x - 1:
                circum += 1
                border.add(((i + 1, j), (i + 1, j + 1), "n"))
            if j == 0:
                circum += 1
                border.add(((i, j), (i + 1, j), "e"))
            if j == max_y - 1:
                circum += 1
                border.add(((i, j + 1), (i + 1, j + 1), "w"))
        score += circum * len(region)

        visited_borders = set()
        border_count = 0
        for bord in border:
            if bord not in visited_borders:
                current_border = [bord]
                border_count += 1
                while current_border:
                    (a, b), (c, d), direction = current_border[0]
                    visited_borders.add(bord)
                    if a == c:
                        left = ((a, b - 1), (c, d - 1), direction)
                        right = ((a, b + 1), (c, d + 1), direction)
                        if left in border and left not in visited_borders:
                            visited_borders.add(left)
                            current_border.append(left)
                        if right in border:
                            visited_borders.add(right)
                            current_border.append(right)
                    else:
                        up = ((a + 1, b), (c + 1, d), direction)
                        down = ((a - 1, b), (c - 1, d), direction)
                        if up in border and up not in visited_borders:
                            visited_borders.add(up)
                            current_border.append(up)
                        if down in border:
                            visited_borders.add(down)
                            current_border.append(down)
                    current_border = current_border[1:]
        score_part2 += border_count * len(region)

    print(score)
    print(score_part2)
