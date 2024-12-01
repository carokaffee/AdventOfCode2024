from src.tools.loader import load_data

TESTING = False

if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    left_list = []
    right_list = []
    for line in data:
        a, b = list(map(int, line.split()))
        left_list.append(a)
        right_list.append(b)

    left_list.sort()
    right_list.sort()

    # print(left_list, right_list)

    sum = 0

    for i in range(len(left_list)):
        sum += abs(left_list[i]-right_list[i])

    print(sum)

    similar = 0

    for el in left_list:
        similar += right_list.count(el)*el

    print(similar)