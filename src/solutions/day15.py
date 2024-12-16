from src.tools.loader import load_data

TESTING = False
DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(data):
    grid = []
    moves = []
    for i, line in enumerate(data[0].split("\n")):
        grid_line = []
        for j, el in enumerate(line):
            if el == "@":
                position = (i, j)
                grid_line.append(".")
            else:
                grid_line.append(el)
        grid.append(grid_line)

    for line in data[1].split("\n"):
        for el in line:
            moves.append(DIRECTIONS[el])

    return grid, moves, position


def print_grid(grid, position):
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if (i, j) == position:
                print("@", end="")
            else:
                print(el, end="")
        print()


def solve_part_1(grid, moves, position):
    for move in moves:
        x, y = position
        dx, dy = move
        new_x, new_y = x + dx, y + dy

        if grid[new_x][new_y] == ".":
            position = (new_x, new_y)

        if grid[new_x][new_y] == "O":
            next_elements = ["."]
            counter = 1

            while next_elements[-1] != "#":
                next_elements.append(grid[x + counter * dx][y + counter * dy])
                counter += 1

            box_counter = 1
            boxes_there = True

            while boxes_there:
                if next_elements[box_counter] == "O":
                    box_counter += 1
                else:
                    boxes_there = False

            if next_elements[box_counter] == ".":
                position = (new_x, new_y)
                grid[new_x][new_y] = "."
                grid[x + box_counter * dx][y + box_counter * dy] = "O"
        else:
            pass

    return grid


def enlarge_grid(grid):
    large_grid = []
    for line in grid:
        grid_line = []
        for el in line:
            if el in "#.":
                grid_line += [el] * 2
            else:
                grid_line.append("[")
                grid_line.append("]")
        large_grid.append(grid_line)
    return large_grid


def solve_part_2(grid, moves, position):
    grid = enlarge_grid(grid)
    position = (position[0], position[1] * 2)

    for move in moves:
        x, y = position
        dx, dy = move
        new_x, new_y = x + dx, y + dy

        if grid[new_x][new_y] == ".":
            position = (new_x, new_y)

        elif grid[new_x][new_y] in "[]":
            if dx == 0:
                next_elements = ["."]
                counter = 1

                while next_elements[-1] != "#":
                    next_elements.append(grid[x + counter * dx][y + counter * dy])
                    counter += 1

                box_counter = 1
                boxes_there = True

                while boxes_there:
                    if next_elements[box_counter] in ["[", "]"]:
                        box_counter += 1
                    else:
                        boxes_there = False

                if next_elements[box_counter] == ".":
                    position = (new_x, new_y)
                    grid[new_x][new_y] = "."
                    for i in range(2, box_counter + 1):
                        if dy > 0:
                            grid[x + i * dx][y + i * dy] = "[" if i % 2 == 0 else "]"
                        else:
                            grid[x + i * dx][y + i * dy] = "]" if i % 2 == 0 else "["

            else:
                boxes_touched = []
                queue = []
                no_wall = True

                if grid[new_x][new_y] == "[":
                    next_box = ((new_x, new_y), (new_x, new_y + 1))
                    boxes_touched.append(next_box)
                    queue.append(next_box)
                elif grid[new_x][new_y] == "]":
                    next_box = ((new_x, new_y - 1), (new_x, new_y))
                    boxes_touched.append(next_box)
                    queue.append(next_box)

                while queue:
                    (x1, y1), (x2, y2) = queue[0]

                    if grid[x1 + dx][y1] == "#" or grid[x2 + dx][y2] == "#":
                        queue = []
                        boxes_touched = []
                        no_wall = False

                    else:
                        if grid[x1 + dx][y1] == "[":
                            next_box = ((x1 + dx, y1), (x1 + dx, y1 + 1))
                            queue.append(next_box)
                            boxes_touched.append(next_box)
                        elif grid[x1 + dx][y1] == "]":
                            next_box = ((x1 + dx, y1 - 1), (x1 + dx, y1))
                            queue.append(next_box)
                            boxes_touched.append(next_box)

                        if grid[x2 + dx][y2] == "[":
                            next_box = ((x2 + dx, y2), (x2 + dx, y2 + 1))
                            queue.append(next_box)
                            boxes_touched.append(next_box)
                        queue = queue[1:]

                for (x1, y1), (x2, y2) in reversed(boxes_touched):
                    grid[x1 + dx][y1] = "["
                    grid[x2 + dx][y2] = "]"
                    grid[x1][y1] = "."
                    grid[x2][y2] = "."
                if no_wall:
                    position = (new_x, new_y)

        else:
            pass

    return grid


def calculate_score(grid):
    score = 0
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el in "O[":
                score += 100 * i + j
    return score


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")

    # PART 1
    # test:     10092
    # answer: 1442192
    grid, moves, position = parse_input(data)
    grid = solve_part_1(grid, moves, position)
    print(calculate_score(grid))

    # PART 2
    # test:      9021
    # answer: 1448458
    grid, moves, position = parse_input(data)
    grid = solve_part_2(grid, moves, position)
    print(calculate_score(grid))
