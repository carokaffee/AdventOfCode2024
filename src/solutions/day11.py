from src.tools.loader import load_data
from collections import defaultdict

TESTING = False


def parse_input(data):
    raw_stones = list(map(int, data[0].split()))
    stones = defaultdict(int)
    
    for stone in raw_stones:
        stones[stone] += 1
    
    return stones


def do_iteration(stones):
    new_stones = defaultdict(int)

    for stone in stones.keys():
        num_stones = stones[stone]
        if stone == 0:
            new_stones[1] += num_stones
        elif len(str(stone)) % 2 == 0:
            new_stones[int(str(stone)[:len(str(stone)) // 2])] += num_stones
            new_stones[int(str(stone)[len(str(stone))//2:])] += num_stones
        else:
            new_stones[stone * 2024] += num_stones

    return new_stones


def blink_and_count(stones, times):
    for _ in range(times):
        stones = do_iteration(stones)

    result = sum(stones.values())
    return result


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    stones = parse_input(data)

    # PART 1
    # test:    55312
    # answer: 200446
    print(blink_and_count(stones, 25))

    # PART 2
    # test:    65601038650482
    # answer: 238317474993392
    print(blink_and_count(stones, 75))
