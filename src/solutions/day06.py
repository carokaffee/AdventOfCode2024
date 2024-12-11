from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    grid = [line for line in data]
    start = "".join(data).find("^") // len(data) + ("".join(data).find("^") % len(data)) * 1j
    return grid, start


def simulate_guard(rows, start):
    length = len(data)
    width = len(data[0])

    current_dir = -1 + 0j
    current_pos = start
    visited = set([current_pos])
    guard_left = False

    while not guard_left:
        new_pos = current_pos + current_dir
        new_x = int(new_pos.real)
        new_y = int(new_pos.imag)
        if new_x < 0 or new_x >= length or new_y < 0 or new_y >= width:
            guard_left = True
        elif rows[new_x][new_y] == "#":
            current_dir *= -1j
        else:
            current_pos = new_pos
            visited.add(new_pos)

    return visited


def count_loops(rows, start, guard_path):
    length = len(data)
    width = len(data[0])
    loops_found = 0

    for coord in guard_path:
        current_dir = -1 + 0j
        current_pos = start
        visited = set([current_pos, current_dir])
        guard_left = False

        while not guard_left:
            new_pos = current_pos + current_dir
            new_x = int(new_pos.real)
            new_y = int(new_pos.imag)
            if (new_pos, current_dir) in visited:
                loops_found += 1
                guard_left = True
            elif new_x < 0 or new_x >= length or new_y < 0 or new_y >= width:
                guard_left = True
            elif rows[new_x][new_y] in "#" or new_x + new_y * 1j == coord:
                current_dir *= -1j
            else:
                current_pos = new_pos
                visited.add((new_pos, current_dir))

    return loops_found


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    grid, start = parse_input(data)

    # PART 1
    # test:     41
    # answer: 5305
    guard_path = simulate_guard(grid, start)
    print(len(guard_path))

    # PART 2
    # test:      6
    # answer: 2143
    print(count_loops(grid, start, guard_path))
