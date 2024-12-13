from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    machines = []
    for machine in data:
        button_a, button_b = [
            [int(machine.split("\n")[j].split(": ")[1].split(",")[i].split("+")[1]) for i in [0, 1]] for j in [0, 1]
        ]
        prize = tuple([int(machine.split("\n")[2].split(": ")[1].split(", ")[i].split("=")[1]) for i in [0, 1]])
        machines.append((button_a, button_b, prize))
    return machines


def tokens_needed(machines, offset=0):
    score = 0
    for machine in machines:
        (Ax, Ay), (Bx, By), (X, Y) = machine
        X += offset
        Y += offset

        y = (Y - Ay / Ax * X) / (-Ay * Bx / Ax + By)
        x = (X - y * Bx) / Ax

        x = int(x + 0.1)
        y = int(y + 0.1)

        if x * Ax + y * Bx == X and x * Ay + y * By == Y:
            score += 3 * int(x + 0.1) + int(y + 0.1)

    return score


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    machines = parse_input(data)

    # PART 1
    # test:     480
    # answer: 29388
    print(tokens_needed(machines))

    # PART 2
    # test:     875318608908
    # answer: 99548032866004
    print(tokens_needed(machines, 10000000000000))
