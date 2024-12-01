from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    left = []
    right = []
    for line in data:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    return left, right


def get_total_distance(left, right):
    diff_sum = 0
    for i in range(len(left)):
        diff_sum += abs(sorted(left)[i] - sorted(right)[i])
    return diff_sum


def get_sim_score(left, right):
    sim_sum = 0
    for el in left:
        sim_sum += right.count(el) * el
    return sim_sum


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    left, right = parse_input(data)

    # PART 1
    # test:        11
    # answer: 1579939
    print(get_total_distance(left, right))

    # PART 2
    # test:         31
    # answer: 20351745
    print(get_sim_score(left, right))
