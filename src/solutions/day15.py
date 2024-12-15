from src.tools.loader import load_data

TESTING = False

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(data):
    grid = []
    moves = []
    for i, line in enumerate(data[0].split("\n")):
        grid.append([])
        for j, el in enumerate(line):
            if el == "@":
                position = (i, j)
                grid[-1].append(".")
            else:
                grid[-1].append(el)

    for line in data[1].split("\n"):
        for el in line:
            moves.append(DIRECTIONS[el])

    return grid, moves, position


def enlarge_grid(grid):
    large_grid = []
    for i, line in enumerate(grid):
        large_grid.append([])
        for j, el in enumerate(line):
            if el == "#":
                large_grid[-1].append("#")
                large_grid[-1].append("#")
            elif el == "O":
                large_grid[-1].append("[")
                large_grid[-1].append("]")
            elif el == ".":
                large_grid[-1].append(".")
                large_grid[-1].append(".")
            else:
                large_grid[-1].append(".")
                large_grid[-1].append(".")
    return large_grid


def print_grid(grid, position):
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if i == position[0] and j == position[1]:
                print("@", end="")
            else:
                print(el, end="")
        print()


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    grid, moves, position = parse_input(data)

    # print(position)
    # print_grid(grid)
    # print(moves)

    for move in moves:
        x, y = position
        dx, dy = move

        # print(position)
        # print_grid(grid)
        # input()

        new_x, new_y = x + dx, y + dy
        if grid[new_x][new_y] == ".":
            position = (new_x, new_y)
        elif grid[new_x][new_y] == "#":
            pass
        else:
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
            if next_elements[box_counter] == "#":
                pass
            elif next_elements[box_counter] == ".":
                position = (new_x, new_y)
                grid[new_x][new_y] = "."
                grid[x + box_counter * dx][y + box_counter * dy] = "O"
            else:
                raise ValueError("something is wrong")

    score = 0
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "O":
                score += 100 * i + j

    print("Score Part 1:", score)
    # print()
    # print_grid(grid)

    grid, moves, position = parse_input(data)
    grid = enlarge_grid(grid)
    position = (position[0], position[1] * 2)

    # print(position)
    # print_grid(grid, position)

    for move in moves:
        x, y = position
        dx, dy = move

        new_x, new_y = x + dx, y + dy
        if grid[new_x][new_y] == ".":
            position = (new_x, new_y)
        elif grid[new_x][new_y] == "#":
            pass
        else:
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
                if next_elements[box_counter] == "#":
                    pass
                elif next_elements[box_counter] == ".":
                    position = (new_x, new_y)
                    grid[new_x][new_y] = "."
                    for i in range(2, box_counter + 1):
                        if dy > 0:
                            grid[x + i * dx][y + i * dy] = "[" if i % 2 == 0 else "]"
                        else:
                            grid[x + i * dx][y + i * dy] = "]" if i % 2 == 0 else "["
                else:
                    raise ValueError("something is wrong")
            else:
                boxes_touched = []
                queue = []
                done = False
                no_wall = True
                if grid[new_x][new_y] == "[":
                    if (((new_x, new_y), (new_x, new_y + 1))) not in boxes_touched:
                        boxes_touched.append((((new_x, new_y), (new_x, new_y + 1))))
                        queue.append((((new_x, new_y), (new_x, new_y + 1))))
                elif grid[new_x][new_y] == "]":
                    if (((new_x, new_y - 1), (new_x, new_y))) not in boxes_touched:
                        boxes_touched.append((((new_x, new_y - 1), (new_x, new_y))))
                        queue.append((((new_x, new_y - 1), (new_x, new_y))))
                else:
                    raise ValueError("not a correct box")

                while queue:
                    (bx, by), (cx, cy) = queue[0]
                    if queue[0] == ((1, 13), (1, 14)):
                        print("HERE WE ARE")
                    if grid[bx + dx][by] == "#" or grid[cx + dx][cy] == "#":
                        queue = []
                        boxes_touched = []
                        no_wall = False
                    else:
                        if grid[bx + dx][by] == "[":
                            if ((bx + dx, by), (bx + dx, by + 1)) not in boxes_touched:
                                queue.append(((bx + dx, by), (bx + dx, by + 1)))
                                boxes_touched.append(((bx + dx, by), (bx + dx, by + 1)))
                            # queue = queue[1:]
                        elif grid[bx + dx][by] == "]":
                            if ((bx + dx, by - 1), (bx + dx, by)) not in boxes_touched:
                                queue.append(((bx + dx, by - 1), (bx + dx, by)))
                                boxes_touched.append(((bx + dx, by - 1), (bx + dx, by)))
                            # queue = queue[1:]
                        elif grid[bx + dx][by] == ".":
                            pass
                            # queue = queue[1:]
                        else:
                            raise ValueError("problem with left box")

                        if grid[cx + dx][cy] == "[":
                            if ((cx + dx, cy), (cx + dx, cy + 1)) not in boxes_touched:
                                queue.append(((cx + dx, cy), (cx + dx, cy + 1)))
                                boxes_touched.append(((cx + dx, cy), (cx + dx, cy + 1)))
                            # queue = queue[1:]
                        elif grid[cx + dx][cy] == "]":
                            pass
                        elif grid[cx + dx][cy] == ".":
                            pass
                            # queue = queue[1:]
                        else:
                            raise ValueError("problem with right box")
                        queue = queue[1:]

                for (bx, by), (cx, cy) in reversed(boxes_touched):
                    if grid[bx + dx][by] == "#" or grid[cx + dx][cy] == "#":
                        # print(bx, dx, by)
                        # print("queue", queue)
                        # print("boxes touched", boxes_touched)
                        # print_grid(grid, position)
                        raise ValueError("what happens here?")
                    grid[bx + dx][by] = "["
                    grid[cx + dx][cy] = "]"
                    grid[bx][by] = "."
                    grid[cx][cy] = "."
                if no_wall:
                    position = (new_x, new_y)

        # print(position)
        # print_grid(grid, position)
        # input()

    score = 0
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == "[":
                score += 100 * i + j

    print("Score Part 2:", score)
