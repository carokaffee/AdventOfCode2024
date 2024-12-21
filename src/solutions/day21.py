from src.tools.loader import load_data
from itertools import combinations, product
from tqdm import tqdm

TESTING = False


if __name__ == "__main__":
    seq_last_robot = load_data(TESTING, "\n")

    coords_num = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
        "gap": (3, 0),
    }

    coords_dirs = {
        "gap": (0, 0),
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
    }

    shortest_overall = []

    for keypad_seq in seq_last_robot:
        pos2 = (3, 2)
        shortest_moves2 = []
        for el in keypad_seq:
            shortest_moves2.append([])
            new_pos = coords_num[el]
            dx, dy = new_pos[0] - pos2[0], new_pos[1] - pos2[1]
            adx, ady = abs(dx), abs(dy)
            for subset in list(combinations(range(adx + ady), adx)):
                current_path = ""
                current_pos = [pos2]
                for i in range(adx + ady):
                    if i in subset:
                        current_path = current_path + "v" if dx > 0 else current_path + "^"
                        new_current_pos = (
                            (current_pos[-1][0] - 1, current_pos[-1][1])
                            if dx < 0
                            else (current_pos[-1][0] + 1, current_pos[-1][1])
                        )
                        current_pos.append(new_current_pos)
                    else:
                        current_path = current_path + ">" if dy > 0 else current_path + "<"
                        new_current_pos = (
                            (current_pos[-1][0], current_pos[-1][1] - 1)
                            if dy < 0
                            else (current_pos[-1][0], current_pos[-1][1] + 1)
                        )
                        current_pos.append(new_current_pos)
                current_path = current_path + "A"
                if coords_num["gap"] not in current_pos:
                    shortest_moves2[-1].append(current_path)
            pos2 = new_pos

        moves_last_robot = ["".join(seq) for seq in list(product(*shortest_moves2))]
        min_length_2 = min(map(len, moves_last_robot))
        moves_last_robot = [move for move in moves_last_robot if len(move) == min_length_2]
        print("moves last robot for sequence", keypad_seq, moves_last_robot)

        moves_middle_robot = []

        for move_last_robot in moves_last_robot:
            print("move", move_last_robot)
            pos1 = (0, 2)
            shortest_moves1 = []
            for el in move_last_robot:
                shortest_moves1.append([])
                new_pos = coords_dirs[el]
                dx, dy = new_pos[0] - pos1[0], new_pos[1] - pos1[1]
                adx, ady = abs(dx), abs(dy)
                for subset in list(combinations(range(adx + ady), adx)):
                    current_path = ""
                    current_pos = [pos1]
                    for i in range(adx + ady):
                        if i in subset:
                            current_path = current_path + "v" if dx > 0 else current_path + "^"
                            new_current_pos = (
                                (current_pos[-1][0] - 1, current_pos[-1][1])
                                if dx < 0
                                else (current_pos[-1][0] + 1, current_pos[-1][1])
                            )
                            current_pos.append(new_current_pos)
                        else:
                            current_path = current_path + ">" if dy > 0 else current_path + "<"
                            new_current_pos = (
                                (current_pos[-1][0], current_pos[-1][1] - 1)
                                if dy < 0
                                else (current_pos[-1][0], current_pos[-1][1] + 1)
                            )
                            current_pos.append(new_current_pos)
                    current_path = current_path + "A"
                    if coords_num["gap"] not in current_pos:
                        shortest_moves1[-1].append(current_path)
                pos1 = new_pos
            moves_middle_robot += ["".join(seq) for seq in list(product(*shortest_moves1))]

        # moves_middle_robot = list(set(moves_middle_robot))
        print("len of moves middle robot for sequence", len(moves_middle_robot))
        min_length_1 = min(map(len, moves_middle_robot))
        moves_middle_robot = [move for move in moves_middle_robot if len(move) == min_length_1]

        moves_first_robot = []

        for move_middle_robot in tqdm(moves_middle_robot):
            # print("move", move_middle_robot)
            pos0 = (0, 2)
            shortest_moves0 = []
            for el in move_middle_robot:
                shortest_moves0.append([])
                new_pos = coords_dirs[el]
                dx, dy = new_pos[0] - pos0[0], new_pos[1] - pos0[1]
                adx, ady = abs(dx), abs(dy)
                for subset in list(combinations(range(adx + ady), adx)):
                    current_path = ""
                    current_pos = [pos0]
                    for i in range(adx + ady):
                        if i in subset:
                            current_path = current_path + "v" if dx > 0 else current_path + "^"
                            new_current_pos = (
                                (current_pos[-1][0] - 1, current_pos[-1][1])
                                if dx < 0
                                else (current_pos[-1][0] + 1, current_pos[-1][1])
                            )
                            current_pos.append(new_current_pos)
                        else:
                            current_path = current_path + ">" if dy > 0 else current_path + "<"
                            new_current_pos = (
                                (current_pos[-1][0], current_pos[-1][1] - 1)
                                if dy < 0
                                else (current_pos[-1][0], current_pos[-1][1] + 1)
                            )
                            current_pos.append(new_current_pos)
                    current_path = current_path + "A"
                    if coords_num["gap"] not in current_pos:
                        shortest_moves0[-1].append(current_path)
                pos0 = new_pos
            moves_first_robot += ["".join(seq) for seq in list(product(*shortest_moves0))]

        # moves_middle_robot = list(set(moves_middle_robot))
        print("len of moves middle robot for sequence", len(moves_first_robot))
        min_length_0 = min(map(len, moves_first_robot))
        moves_first_robot = [move for move in moves_first_robot if len(move) == min_length_0]

        # print(len(moves_first_robot[0]))
        shortest_overall.append(min(map(len, moves_first_robot)))

    print(shortest_overall)
    score = 0
    for j, keypad_seq in enumerate(seq_last_robot):
        numeric = int("".join(keypad_seq[i] for i in range(len(keypad_seq)) if keypad_seq[i].isdigit()))
        score += numeric * shortest_overall[j]
        print(numeric * shortest_overall[j])

    print(score)
