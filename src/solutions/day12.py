from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    padding_line = "." * (len(data[0]) + 2)
    padded_data = [padding_line]

    for line in data:
        padded_data.append("." + line + ".")
    padded_data += [padding_line]

    return padded_data


def get_neighbours(position):
    x, y = position
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    neighbours = [(x + dx, y + dy) for dx, dy in directions]

    return neighbours


def solve_part_1(flowers):
    flowers = parse_input(data)
    visited = set()
    regions = []
    borders = []
    score = 0

    for i in range(len(flowers)):
        for j in range(len(flowers[0])):
            if flowers[i][j].isalpha() and (i, j) not in visited:
                current_region = {(i, j)}
                current_border = set()
                queue = [(i, j)]
                visited.add((i, j))

                while queue:
                    x, y = queue[0]
                    for nx, ny in get_neighbours((x, y)):
                        if flowers[nx][ny] == flowers[x][y] and (nx, ny) not in visited:
                            current_region.add((nx, ny))
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                        elif flowers[nx][ny] != flowers[x][y]:
                            current_border.add(((x, y), (nx - x, ny - y)))
                    queue = queue[1:]

                regions.append(current_region)
                borders.append(current_border)
                score += len(current_region) * len(current_border)

    return regions, borders, score


def solve_part_2(regions, borders):
    score = 0

    for n in range(len(regions)):
        region = regions[n]
        fences = borders[n]
        visited_fences = set()
        fence_count = 0

        for fence in fences:
            if fence not in visited_fences:
                queue = [fence]
                fence_count += 1

                while queue:
                    (x, y), direction = queue[0]
                    dx, dy = direction
                    visited_fences.add(fence)
                    prev_fence = ((x - dy, y - dx), direction)
                    next_fence = ((x + dy, y + dx), direction)
                    possible_neighbours = [prev_fence, next_fence]

                    for pn in possible_neighbours:
                        if pn in fences and pn not in visited_fences:
                            visited_fences.add(pn)
                            queue.append(pn)

                    queue = queue[1:]

        score += fence_count * len(region)

    return score


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    flowers = parse_input(data)

    # PART 1
    # test:      1930
    # answer: 1488414
    regions, borders, score_1 = solve_part_1(flowers)
    print(score_1)

    # PART 2
    # test:     1206
    # answer: 911750
    score_2 = solve_part_2(regions, borders)
    print(score_2)
