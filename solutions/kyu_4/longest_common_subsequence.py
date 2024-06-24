"""Solution for kata https://www.codewars.com/kata/593ff8b39e1cc4bae9000070."""


def lcs(x, y):
    array = [[''] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i_line in range(1, len(x) + 1):
        for i_column in range(1, len(y) + 1):
            # index line - 1 = letter index in x
            # index column - 1 = letter index in y
            is_equal = x[i_line - 1] if x[i_line - 1] == y[i_column - 1] else ''

            if is_equal:
                array[i_line][i_column] = array[i_line - 1][i_column - 1] + is_equal
            else:
                array[i_line][i_column] = max(array[i_line - 1][i_column],
                                              array[i_line][i_column - 1],
                                              key=len)

    return array[-1][-1]
