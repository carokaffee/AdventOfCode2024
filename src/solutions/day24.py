from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    values = dict()
    connections = []
    raw_vals, raw_conns = data

    for line in raw_vals.split("\n"):
        key, val = line.split(": ")
        values[key] = int(val)
    for line in raw_conns.split("\n"):
        before, goal = line.split(" -> ")
        start, instr, end = before.split(" ")
        connections.append(((start, instr, end), goal))

    return values, connections


def run_system(data):
    values, connections = parse_input(data)
    for _ in range(100):
        for (start, instr, end), goal in connections:
            if start in values.keys() and end in values.keys() and goal not in values.keys():
                if instr == "AND":
                    values[goal] = int(values[start] and values[end])
                elif instr == "OR":
                    values[goal] = int(values[start] or values[end])
                elif instr == "XOR":
                    values[goal] = int(values[start] != values[end])
    return values, connections


def identify_wrong_wires(connections):
    swapped_wires = []

    for (start, instr, end), goal in connections:
        # Condition 1: XOR instruction and no wires start with "x", "y", or "z"
        if instr == "XOR" and all(not wire.startswith(("x", "y", "z")) for wire in (start, end, goal)):
            swapped_wires.append(goal)

        # Condition 2: AND instruction, a related XOR connection, and no "x00" in start/end
        elif (
            instr == "AND"
            and any(i == "XOR" and goal in (s, e) for (s, i, e), _ in connections)
            and not "x00" in (start, end)
        ):
            swapped_wires.append(goal)

        # Condition 3: XOR instruction, a related OR connection, and no "x00" in start/end
        elif (
            instr == "XOR"
            and any(i == "OR" and goal in (s, e) for (s, i, e), _ in connections)
            and not "x00" in (start, end)
        ):
            swapped_wires.append(goal)

        # Condition 4: Non-XOR instruction, goal starts with "z", and goal is not "z45"
        elif instr != "XOR" and goal.startswith("z") and goal != "z45":
            swapped_wires.append(goal)

    return sorted(swapped_wires)


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    values, connections = run_system(data)
    z_wires = sorted((z for z in values.keys() if z.startswith("z")), reverse=True)

    # PART 1
    # test:             2024
    # answer: 36902370467952
    print(int("".join(str(values[z]) for z in z_wires), 2))

    # PART 2
    # test:                   z00,z01,z02,z05
    # answer: cvp,mkk,qbw,wcb,wjb,z10,z14,z34
    print(",".join(identify_wrong_wires(connections)))
