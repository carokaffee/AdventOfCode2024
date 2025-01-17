from src.tools.loader import load_data
from math import prod

TESTING = False

# MAX_X = 11 # for test input
MAX_X = 101
# MAX_Y = 7 # for test input
MAX_Y = 103


def parse_input(data):
    robots = []
    for line in data:
        position, velocity = line.split()
        position = tuple(map(int, position.split("=")[1].split(",")))
        velocity = tuple(map(int, velocity.split("=")[1].split(",")))
        robots.append((position, velocity))
    return robots


def move_robots(robots, seconds):
    new_positions = []
    for robot in robots:
        (x, y), (dx, dy) = robot
        new_x = (x + seconds * dx) % MAX_X
        new_y = (y + seconds * dy) % MAX_Y
        new_positions.append((new_x, new_y))
    return new_positions


def calc_safety_factor(positions):
    quadrants = [0, 0, 0, 0]

    for x, y in positions:
        left = 0 <= x < MAX_X // 2
        right = MAX_X // 2 < x < MAX_X
        up = 0 <= y < MAX_Y // 2
        down = MAX_Y // 2 < y < MAX_Y
        quadrants[0] += left and up
        quadrants[1] += left and down
        quadrants[2] += right and up
        quadrants[3] += right and down

    return prod(quadrants)


def solve_part_1(robots):
    new_positions = move_robots(robots, 100)
    safety_factor = calc_safety_factor(new_positions)
    return safety_factor


def solve_part_2(robots):
    # possible_solutions = list(range(101 * 103))
    # we know that after lcm(101,103) = 101 * 103 seconds, all patterns repeat
    # I found horizontal and vertical patterns starting at 88 resp. 12 and being 103 resp. 101 seconds apart
    # so I specifically looked for a christmas tree at these values
    possible_solutions = sorted([88 + i * 103 for i in range(101)] + [12 + i * 101 for i in range(103)])

    for i in possible_solutions:
        print(i)
        new_positions = move_robots(robots, i)
        grid = [["."] * MAX_X for _ in range(MAX_Y)]
        for x, y in new_positions:
            if grid[y][x] == ".":
                grid[y][x] = 1
            else:
                grid[y][x] += 1
        for line in grid:
            for el in line:
                print(el, end="")
            print()
        input()


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    robots = parse_input(data)

    # PART 1
    # test:          12
    # answer: 229421808
    print(solve_part_1(robots))

    # PART 2
    # test:     --
    # answer: 6577
    solve_part_2(robots)
