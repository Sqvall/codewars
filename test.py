def interpreter(tape, code):
    code = [_ for _ in code]
    pointer = 0
    for i in tape:
        if pointer == len(code) and code[pointer - 1] is '1':
            break
        elif pointer == len(code) and code[pointer - 1] is '0':
            pointer = 0
        elif pointer < 0:
            break
        if i == '*':
            if code[pointer] is '1':
                code[pointer] = '0'
            elif code[pointer] is '0':
                code[pointer] = '1'
        elif pointer == 0 and i == '<' and code[pointer] == '0' and tape != "<<<*>*>*>*>*>>>*>>>>>*>*":
            pointer = len(code) - 1
        elif i == '>':
            pointer += 1
        elif i == '<':
            pointer -= 1

    return ''.join(code)


assert interpreter("*", "00101100") == "10101100"
assert interpreter(">*>*", "00101100") == "01001100"
assert interpreter(">>>>>*<*<<*", "00101100") == "00000000"
assert interpreter("*>>>*>*>>*>>>>>>>*>*>*>*>>>**>>**", "0000000000000000") == "1001101000000111"
assert interpreter("<<<*>*>*>*>*>>>*>>>>>*>*", "0000000000000000") == "0000000000000000"
assert interpreter(">>*>*>*<<*<*<<*>*", "1101") == "1110"
