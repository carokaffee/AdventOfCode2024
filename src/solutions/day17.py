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
    reg_a = int(data[0].split("\n")[0].split(": ")[-1])
    reg_b = int(data[0].split("\n")[1].split(": ")[-1])
    reg_c = int(data[0].split("\n")[2].split(": ")[-1])
    program = tuple(map(int, data[1].split(": ")[1].split(",")))

    return [reg_a, reg_b, reg_c], program


def perform_instruction(registers, opcode, operand, instruction_pointer):
    reg_a, reg_b, reg_c = registers
    literal_operand = operand
    instruction = INSTRUCTIONS[opcode]
    compop = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg_a, 5: reg_b, 6: reg_c, 7: 1}
    combo_operand = compop[operand]
    output = ""
    new_instruction_pointer = instruction_pointer

    if instruction == "adv":
        reg_a = reg_a // (2**combo_operand)
    elif instruction == "bxl":
        reg_b = reg_b ^ literal_operand
    elif instruction == "bst":
        reg_b = combo_operand % 8
    elif instruction == "jnz":
        if reg_a != 0:
            new_instruction_pointer = literal_operand
        else:
            new_instruction_pointer += 2
    elif instruction == "bxc":
        reg_b = reg_b ^ reg_c
    elif instruction == "out":
        output += str(combo_operand % 8) + ","
    elif instruction == "bdv":
        reg_b = reg_a // (2**combo_operand)
    elif instruction == "cdv":
        reg_c = reg_a // (2**combo_operand)

    if instruction != "jnz":
        new_instruction_pointer += 2

    return output, new_instruction_pointer, [reg_a, reg_b, reg_c]


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    registers, program = parse_input(data)
    print(registers, program)
    program_string = ",".join(map(str, program))
    done = True
    counter = 0

    while not done:
        if counter % 1000 == 0:
            print(counter)
        registers = [counter, 0, 0]
        instruction_pointer = 0
        overall_output = ""

        while instruction_pointer < len(program):
            opcode = program[instruction_pointer]
            operand = int(program[instruction_pointer + 1])
            output, instruction_pointer, registers = perform_instruction(
                registers, opcode, operand, instruction_pointer
            )
            overall_output += output

        if overall_output == program_string + ",":
            done = True
            print("FOUND SOLUTION", registers, counter)

        counter += 1

    if True:
        # registers = [counter, 0, 0]
        instruction_pointer = 0
        overall_output = ""

        while registers[0] != 0:
            reg_a = registers[0]
            overall_output += str(((((reg_a % 8) ^ 7) ^ (reg_a // 2 ** ((reg_a % 8) ^ 7))) ^ 7) % 8) + ","
            registers[0] = registers[0] // 8

    print("registers", registers)
    print("program", program_string)
    print("output ", overall_output[:-1])
    print()

    for i in [7 * 8 + i for i in range(8)]:
        reg_a = i
        result = str(((((reg_a % 8) ^ 7) ^ (reg_a // 2 ** ((reg_a % 8) ^ 7))) ^ 7) % 8)
        if False:  # result == "0":
            print(i, result)

    possible_reg_a = [i for i in range(1, 8)]
    counter = -1

    while abs(counter) < len(program):
        counter -= 1
        next_goal = program[counter]
        new_possible_reg_a = []
        for possibility in possible_reg_a:
            for trial_reg_a in [possibility * 8 + i for i in range(8)]:
                result = ((((trial_reg_a % 8) ^ 7) ^ (trial_reg_a // 2 ** ((trial_reg_a % 8) ^ 7))) ^ 7) % 8
                if result == next_goal:
                    new_possible_reg_a.append(trial_reg_a)

        possible_reg_a = new_possible_reg_a

    for possible in possible_reg_a:
        registers = [possible, 0, 0]
        instruction_pointer = 0
        overall_output = ""

        while registers[0] != 0:
            reg_a = registers[0]
            overall_output += str(((((reg_a % 8) ^ 7) ^ (reg_a // 2 ** ((reg_a % 8) ^ 7))) ^ 7) % 8) + ","
            registers[0] = registers[0] // 8

        print("possible", possible)
        print("output  ", overall_output[:-1])
        print("program ", program_string)
        print()

        if overall_output[:-1] == program_string:
            print("FOUND SOLUTION PART 2", possible, overall_output)

    print(min(possible_reg_a))

# Register A : X // 8
# Register B : (((X % 8) ^ 7) ^ (X // 2**((X % 8) ^ 7))) ^ 7
# Register C : X // 2**((X % 8) ^ 7)

# Added Output: '((((X % 8) ^ 7) ^ (X // 2**((X % 8) ^ 7))) ^ 7) % 8'
