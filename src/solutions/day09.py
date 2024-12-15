from src.tools.loader import load_data

TESTING = False


def parse_filesystem(data):
    filesystem = []
    for i, num in enumerate(data[0]):
        num = int(num)
        if i % 2 == 0:
            filesystem.append([(num, i // 2)])
        else:
            filesystem.append([(num, None)])
    return filesystem


def solve_part_1(filesystem):
    length = len(filesystem)
    start_ptr = 1
    end_ptr = length - 1 if (length - 1) % 2 == 0 else length - 2

    while start_ptr < end_ptr:
        available_space, is_filled = filesystem[start_ptr][-1]
        needed_space, id = filesystem[end_ptr][-1]
        if is_filled is None:
            if available_space > needed_space:
                filesystem[start_ptr] = (
                    filesystem[start_ptr][:-1] + [(needed_space, id)] + [(available_space - needed_space, None)]
                )
                filesystem[end_ptr] = [(needed_space, None)]
                end_ptr -= 2
            elif available_space < needed_space:
                filesystem[start_ptr] = filesystem[start_ptr][:-1] + [(available_space, id)]
                filesystem[end_ptr] = [(needed_space - available_space, id)]
                start_ptr += 2
            else:
                filesystem[start_ptr] = filesystem[start_ptr][:-1] + [(available_space, id)]
                filesystem[end_ptr] = [(needed_space, None)]
                start_ptr += 2
                end_ptr -= 2
        else:
            start_ptr += 2

    return filesystem


def solve_part_2(filesystem):
    length = len(filesystem)
    end_ptr = length - 1 if (length - 1) % 2 == 0 else length - 2

    while end_ptr > 0:
        start_ptr = 1
        needed_space, id = filesystem[end_ptr][-1]

        while start_ptr < end_ptr:
            available_space, is_filled = filesystem[start_ptr][-1]
            if is_filled is None:
                if available_space > needed_space:
                    filesystem[start_ptr] = (
                        filesystem[start_ptr][:-1] + [(needed_space, id)] + [(available_space - needed_space, None)]
                    )
                    filesystem[end_ptr] = [(needed_space, None)]
                    start_ptr = end_ptr
                elif available_space < needed_space:
                    start_ptr += 2
                else:
                    filesystem[start_ptr] = filesystem[start_ptr][:-1] + [(available_space, id)]
                    filesystem[end_ptr] = [(needed_space, None)]
                    start_ptr = end_ptr
            else:
                start_ptr += 2

        end_ptr -= 2

    return filesystem


def calculate_checksum(filesystem):
    current_id = 0
    checksum = 0

    for register in filesystem:
        for space, id in register:
            for _ in range(space):
                checksum += sum([current_id * id if id is not None else 0])
                current_id += 1

    return checksum


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    # PART 1
    # test:            1928
    # answer: 6337367222422
    filesystem = parse_filesystem(data)
    filesystem_part1 = solve_part_1(filesystem)
    print(calculate_checksum(filesystem_part1))

    # PART 2
    # test:            2858
    # answer: 6361380647183
    filesystem = parse_filesystem(data)
    filesystem_part2 = solve_part_2(filesystem)
    print(calculate_checksum(filesystem_part2))
