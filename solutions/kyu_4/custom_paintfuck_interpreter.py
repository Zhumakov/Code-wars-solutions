"""Solution for kata https://www.codewars.com/kata/5868a68ba44cfc763e00008d."""
COMMAND = ('n', 'e', 's', 'w', '*', '[', ']')


def proc_comm(comm, array, width, height, cursor):
    match comm:
        case 'n': cursor[0] = (cursor[0] - 1) % height
        case 's': cursor[0] = (cursor[0] + 1) % height
        case 'e': cursor[1] = (cursor[1] + 1) % width
        case 'w': cursor[1] = (cursor[1] - 1) % width
        case '*': array[cursor[0]][cursor[1]] = (array[cursor[0]][cursor[1]] + 1) % 2


def interpreter(code, iterations, width, height):
    code = [i for i in code if i in COMMAND]

    array = [[0] * width for _ in range(0, height)]

    cursor = [0, 0]
    it = 0
    i = 0
    while it < iterations:
        if i >= len(code):
            break

        comm = code[i]

        if comm == '[' and array[cursor[0]][cursor[1]] == 0:
            i = code.index(']', i, len(code)) + 1
            it += 1
            continue

        elif comm == ']' and array[cursor[0]][cursor[1]] == 1:
            i = code.index('[', 0, i) + 1
            it += 1
            continue

        proc_comm(comm, array, width, height, cursor)

        i += 1
        it += 1

    output = ''
    for lines in array:
        line = ''

        for column in lines:
            line += str(column)

        line += '\r\n'
        output += line

    return output.rstrip('\r\n')
