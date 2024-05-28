"""Solution for kata https://www.codewars.com/kata/52ec24228a515e620b0005ef."""


def exp_sum(n):
    """
    This kata uses the dynamic programming approach
    The problem can be reduced to the problem of a backpack with an infinite number of items.
    The line indicates the number and its 'weight', the column indicates the 'backpack capacity'.

    :param n: number
    :return: explosive sum for number
    """
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    # Base case: zero can be expanded in only one way
    arr[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, n + 1):
            if i > j:
                arr[i][j] = arr[i - 1][j]
            else:
                buffer = 0
                for offset in range(0, j + 1, i):
                    buffer += arr[i - 1][j - offset]
                arr[i][j] = buffer

    return arr[-1][-1]
