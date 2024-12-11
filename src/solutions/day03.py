from src.tools.loader import load_data
import re

TESTING = False


def find_instruction_sum(instruction, do_dont):
    if do_dont:
        instruction = enabled_instruction(instruction)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, instruction)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])

    return result


def enabled_instruction(instruction):
    enabled_instruction = ""
    current_index = 0

    while True:
        start_index = instruction.find("don't()", current_index)
        if start_index == -1:
            enabled_instruction += instruction[current_index:]
            break

        enabled_instruction += instruction[current_index:start_index]
        end_index = instruction.find("do()", start_index)
        if end_index == -1:
            break

        current_index = end_index

    return enabled_instruction


if __name__ == "__main__":
    instruction = load_data(TESTING, "\n\n")[0]

    # PART 1
    # test:         161
    # answer: 174561379
    print(find_instruction_sum(instruction, False))

    # PART 2
    # test:          48
    # answer: 106921067
    print(find_instruction_sum(instruction, True))
