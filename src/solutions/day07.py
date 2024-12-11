from src.tools.loader import load_data
import itertools

TESTING = False


def parse_input(data):
    calibrations = []
    equations = []
    for line in data:
        cal, numbers = line.split(": ")
        calibrations.append(int(cal))
        equations.append(tuple(map(int, numbers.split())))
    return calibrations, equations


def find_calibration_sum(calibrations, equations, concat):
    total = 0

    for j, equation in enumerate(equations):
        operators = list(itertools.product([0, 1, 2] if concat else [0, 1], repeat=len(equation) - 1))
        found = False
        for operator in operators:
            if not found:
                res = equation[0]
                for i in range(len(equation) - 1):
                    if operator[i] == 0:
                        res += equation[i + 1]
                    elif operator[i] == 1:
                        res *= equation[i + 1]
                    else:
                        res *= 10 ** (len(str(equation[i + 1])))
                        res += equation[i + 1]
                if res == calibrations[j]:
                    found = True
        if found:
            total += calibrations[j]

    return total


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    calibrations, equations = parse_input(data)

    # PART 1
    # test:            3749
    # answer: 1620690235709
    print(find_calibration_sum(calibrations, equations, concat=False))

    # PART 2
    # test:             11387
    # answer: 145397611075341
    print(find_calibration_sum(calibrations, equations, concat=True))
