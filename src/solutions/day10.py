from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    grid = [[int(el) for el in line] for line in data]
    return grid


def get_neighbours(coord):
    x, y = coord
    neighbours = []
    if 0 <= x-1 < GRID_LENGTH:
        neighbours.append((x-1,y))
    if 0 <= x+1 < GRID_LENGTH:
        neighbours.append((x+1,y))
    if 0 <= y-1 < GRID_WIDTH:
        neighbours.append((x,y-1))
    if 0 <= y+1 < GRID_WIDTH:
        neighbours.append((x,y+1))
    return(neighbours)


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid = parse_input(data)

    GRID_LENGTH = len(grid)
    GRID_WIDTH = len(grid[0])

    scores = 0
    ratings = 0

    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == 0:
                nine_pos = set()
                counter = 0
                current_pos = [(i,j)]
                while current_pos:
                    u,v = current_pos[0]
                    neighbours = get_neighbours((u,v))
                    for x,y in neighbours:
                        if grid[x][y] == 9 and grid[x][y] == grid[u][v] + 1:
                            nine_pos.add((x,y))
                            counter += 1
                        elif grid[x][y] == grid[u][v] + 1:
                            current_pos.append((x,y))
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