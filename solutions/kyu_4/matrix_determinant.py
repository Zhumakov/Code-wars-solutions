"""Solution for kata https://www.codewars.com/kata/52a382ee44408cea2500074c"""


def reduce_matrix(array, i_column):
    res = []
    size = len(array)
    for i in range(1, size):
        res.append([])
        for j in range(size):
            if j != i_column:
                res[i - 1].append(array[i][j])

    return res


def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]

    else:
        res = []
        for i in range(size):
            reduced_array = reduce_matrix(matrix, i)
            res.append(determinant(reduced_array))

    d = 0
    for i, num in enumerate(res):
        if i % 2 == 0:
            d += matrix[0][i] * num
        else:
            d -= matrix[0][i] * num

    return d
