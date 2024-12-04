from src.tools.loader import load_data

TESTING = False


if __name__ == "__main__":
    data = load_data(TESTING, "'nothing")
    sequence = data[0]

    next_mul = 0
    prev_next_mul = 0
    done = False
    add_up = 0

    while not done:
        prev_next_mul = next_mul
        next_mul = sequence.find('mul', next_mul)
        next_dont = sequence.find("don't()", prev_next_mul)
        next_do = sequence.find("do()", prev_next_mul)
        if next_dont != -1 and next_mul != -1 and next_dont < next_mul:
            next_do = sequence.find("do()", next_dont)
            if next_do != -1:
                next_mul = next_do
            else:
                next_mul = 2**100
        else:

            if next_mul == -1:
                done = True
                continue
            else:
                if sequence[next_mul+3] == '(':
                    len_dig1 = 0
                    if sequence[next_mul+4].isdigit():
                        len_dig1 += 1
                        if sequence[next_mul+5].isdigit():
                            len_dig1 += 1
                            if sequence[next_mul+6].isdigit():
                                len_dig1 += 1
                        if sequence[next_mul+3+len_dig1+1] == ',':
                            len_dig2 = 0
                            if sequence[next_mul+3+len_dig1+2].isdigit():
                                len_dig2 += 1
                                if sequence[next_mul+3+len_dig1+3].isdigit():
                                    len_dig2 += 1
                                    if sequence[next_mul+3+len_dig1+4].isdigit():
                                        len_dig2 += 1
                                if sequence[next_mul+3+len_dig1+len_dig2+2] == ")":
                                    add_up += int(sequence[next_mul+3+1:next_mul+3+1+len_dig1]) * int(sequence[next_mul+3+1+len_dig1+1:next_mul+3+1+len_dig1+len_dig2+1])
            next_mul += 1


    print(add_up)

