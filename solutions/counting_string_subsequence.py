"""Solution for kata https://www.codewars.com/kata/52f7892a747862fc9a0009a6."""


def count_subsequences(needle, haystack):
    len_x = len(haystack) + 1
    len_y = len(needle) + 1

    array = [[0] * len_x for _ in range(len_y)]

    # base cases
    for i in range(len_x):
        array[0][i] = 1

    # filling the array
    for index_y in range(1, len_y):
        for index_x in range(1, len_x):

            if needle[index_y - 1] == haystack[index_x - 1]:
                array[index_y][index_x] = array[index_y - 1][index_x - 1] + array[index_y][index_x - 1]

            else:
                array[index_y][index_x] = array[index_y][index_x - 1]

    return array[-1][-1]
