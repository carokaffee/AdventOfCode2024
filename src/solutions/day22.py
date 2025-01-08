from src.tools.loader import load_data

TESTING = False
PRUNE = 16777216


def get_next_secret_number(a):
    start = a
    a *= 64
    a ^= start
    a %= PRUNE
    start = a
    a //= 32
    a ^= start
    a %= PRUNE
    start = a
    a *= 2048
    a ^= start
    a %= PRUNE
    return a


def solve_part_1(initial_secret_numbers):
    score = 0

    for num in initial_secret_numbers:
        current = num
        for _ in range(2000):
            current = get_next_secret_number(current)
        score += current

    return score


def solve_part_2(initial_secret_numbers):
    best_score = 0
    evolving_total = []
    diffs_total = []
    dicts = []

    for num in initial_secret_numbers:
        evolving_secret_numbers = [num % 10]
        current = num
        for _ in range(2000):
            current = get_next_secret_number(current)
            evolving_secret_numbers.append(current % 10)
        diffs_total.append([evolving_secret_numbers[i + 1] - evolving_secret_numbers[i] for i in range(2000)])
        seq = ()
        seq_to_val = {}

        for diff, val in zip(diffs_total[-1], evolving_secret_numbers[1:]):
            seq = seq + (diff,)
            if len(seq) > 4:
                seq = seq[-4:]
            if seq in seq_to_val:
                continue
            seq_to_val[seq] = val
        evolving_total.append(evolving_secret_numbers)
        dicts.append(seq_to_val)

    possible_four_diffs = {tuple(diffs_total[i][j : j + 4]) for i in range(len(diffs_total)) for j in range(2000 - 4)}

    for four_price_changes in possible_four_diffs:
        score = 0
        for seq_to_val in dicts:
            score += seq_to_val.get(four_price_changes, 0)

        if best_score < score:
            best_score = score

    return best_score


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    initial_secret_numbers = list(map(int, data))

    # PART 1
    # test:      37327623 # different test input
    # answer: 18694566361
    print(solve_part_1(initial_secret_numbers))

    # PART 2
    # test:     23
    # answer: 2100
    print(solve_part_2(initial_secret_numbers))
