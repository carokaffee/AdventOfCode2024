from src.tools.loader import load_data

TESTING = False

INSTRUCTIONS = {
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv",
}


def parse_input(data):
    registers = [int(data[0].split("\n")[i].split(": ")[-1]) for i in range(3)]
    program = tuple(map(int, data[1].split(": ")[1].split(",")))

    return registers, program


def perform_instruction(registers, opcode, operand, instruction_pointer):
    reg_a, reg_b, reg_c = registers
    instruction = INSTRUCTIONS[opcode]
    new_instruction_pointer = instruction_pointer
    literal_operand = operand
    combo_operand = [0, 1, 2, 3, reg_a, reg_b, reg_c][operand] if operand != 7 else None
    output = ""

    match instruction:
        case "adv":
            reg_a = reg_a // (2**combo_operand)
        case "bxl":
            reg_b = reg_b ^ literal_operand
        case "bst":
            reg_b = combo_operand % 8
        case "jnz":
            if reg_a != 0:
                new_instruction_pointer = literal_operand
            else:
                new_instruction_pointer += 2
        case "bxc":
            reg_b = reg_b ^ reg_c
        case "out":
            output += str(combo_operand % 8) + ","
        case "bdv":
            reg_b = reg_a // (2**combo_operand)
        case "cdv":
            reg_c = reg_a // (2**combo_operand)

    if instruction != "jnz":
        new_instruction_pointer += 2

    return output, new_instruction_pointer, [reg_a, reg_b, reg_c]


def run_program(registers, program):
    instruction_pointer = 0
    overall_output = ""
    current_register = registers

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        output, instruction_pointer, current_register = perform_instruction(
            current_register, opcode, operand, instruction_pointer
        )
        overall_output += output

    return overall_output[:-1]


def find_A_for_part_2(program):
    program_string = ",".join(map(str, program))
    reg_a_candidates = [i for i in range(1, 8)]
    counter = -1

    while abs(counter) < len(program):
        counter -= 1
        next_goal = program[counter]
        new_possible_reg_a = []
        for candidate in reg_a_candidates:
            for new_candidate in [candidate * 8 + i for i in range(8)]:
                # after one program step with X being the number in register A, for our input we get
                # Register A : X // 8
                # Register B : (((X % 8) ^ 7) ^ (X // 2**((X % 8) ^ 7))) ^ 7
                # Register C : X // 2**((X % 8) ^ 7)
                # Added Output: '((((X % 8) ^ 7) ^ (X // 2**((X % 8) ^ 7))) ^ 7) % 8'
                result_input = ((((new_candidate % 8) ^ 7) ^ (new_candidate // 2 ** ((new_candidate % 8) ^ 7))) ^ 7) % 8
                result_testing = new_candidate % 8
                result = result_testing if TESTING else result_input
                if result == next_goal:
                    new_possible_reg_a.append(new_candidate)

        reg_a_candidates = new_possible_reg_a

    # test if we found correct solutions
    reg_a_candidates = [reg_a for reg_a in reg_a_candidates if run_program([reg_a, 0, 0], program) == program_string]

    return min(reg_a_candidates)


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    registers, program = parse_input(data)

    # PART 1
    # test:   4,6,3,5,6,3,5,2,1,0
    # answer:   2,1,0,1,7,2,5,0,3
    print(run_program(registers, program))

    # PART 2
    # test:
    # answer: 267265166222235
    print(find_A_for_part_2(program))
