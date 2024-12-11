from src.tools.loader import load_data

TESTING = False


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    stones = list(map(int, data[0].split()))

    for i in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:len(str(stone)) // 2]))
                new_stones.append(int(str(stone)[len(str(stone))//2:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))