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


def print_grid(grid):
    for line in grid:
        for el in line:
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

    print(score)
    print_grid(grid)
