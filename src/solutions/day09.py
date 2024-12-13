from src.tools.loader import load_data
from collections import defaultdict

TESTING = True


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    print(len(data[0]))

    files = []
    free_space = []
    for i, el in enumerate(data[0]):
        if i % 2 == 0:
            files.append(int(el))
        else:
            free_space.append(int(el))
    print(data)
    print("files", files)
    print("free space", free_space)

    compressed_file = defaultdict(list)

    for i, el in enumerate(data[0]):
        if i % 2 == 0:
            compressed_file[i].append((int(el), i // 2))
        else:
            compressed_file[i].append((int(el), None))

    print(compressed_file)

    current_last_idx = ((len(data[0]) - 1) // 2) * 2
    print(current_last_idx)

    for i, el in enumerate(data[0]):
        while compressed_file[i][-1][1] is None and current_last_idx > i:
            new_ith_element = []
            number, element = compressed_file[i][-1]
            if element is None and current_last_idx > i:
                print(compressed_file[current_last_idx], current_last_idx)
                last_num, last_el = compressed_file[current_last_idx][0]
                if last_el is not None:
                    if last_num < number:
                        new_ith_element = compressed_file[i][:-1] + [(last_num, last_el)] + [(number - last_num, None)]
                        compressed_file[i] = new_ith_element
                        compressed_file[current_last_idx] = [(last_num, None)]
                        current_last_idx -= 2
                    elif last_num == number:
                        new_ith_element = compressed_file[i][:-1] + [(last_num, last_el)]
                        compressed_file[i] = new_ith_element
                        compressed_file[current_last_idx] = [(last_num, None)]
                        current_last_idx -= 2
                    else:
                        new_ith_element = compressed_file[i][:-1] + [(last_num, last_el)]
                        compressed_file[i] = new_ith_element
                        compressed_file[current_last_idx] = [(last_num, None)]
                        current_last_idx -= 2

    print(compressed_file)
