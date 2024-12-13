from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    padding_line = "." * (len(data[0]) + 2)
    padded_data = [padding_line]

    for line in data:
        padded_data.append("." + line + ".")
    padded_data += [padding_line]

    return padded_data


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
    flowers = parse_input(data)

    max_x = len(data)
    max_y = len(data[0])

    visited = set()
    regions = []
    borders2 = []
    scores_new = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in visited:
                current_region = {(i, j)}
                current_border = set()
                queue = [(i, j)]
                visited.add((i, j))

                while queue:
                    x, y = queue[0]
                    for nx, ny in get_neighbours((x, y), max_x, max_y):
                        if data[nx][ny] == data[x][y] and (nx, ny) not in visited:
                            current_region.add((nx, ny))
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                        elif data[nx][ny] != data[x][y]:
                            current_border.add(((x, y), (nx - x, ny - y)))
                    queue = queue[1:]

                regions.append(current_region)
                borders2.append(current_border)
                scores_new += len(current_region) * len(current_border)

    score = 0
    score_part2 = 0

    for region in regions:
        circum = 0
        border = set()
        for i, j in region:
            for nx, ny in get_neighbours((i, j), max_x, max_y):
                if data[nx][ny] != data[i][j]:
                    circum += 1
                    if nx == i:
                        if ny < j:
                            border.add(((i, j), (i + 1, j), "e"))
                        else:
                            border.add(((i, j + 1), (i + 1, j + 1), "w"))
                    if ny == j:
                        if nx < i:
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

    print("old part 1", score)
    print("new part 1", scores_new)
    print("old part2", score_part2)
