"""Solution for kata https://www.codewars.com/kata/5bc6f9110ca59325c1000254."""


def count(chess_board):
    size = len(chess_board)

    # The index in the array is the dimension of the cells
    # the index value is the number of these cells
    counter = [0] * (size + 1)

    for i_line in range(1, size):
        for i_column in range(1, size):

            if chess_board[i_line][i_column] == 0:
                continue

            cell = min(
                chess_board[i_line - 1][i_column - 1],
                chess_board[i_line - 1][i_column],
                chess_board[i_line][i_column - 1],
            )
            chess_board[i_line][i_column] = cell + 1
            counter[cell + 1] += 1

    # The number of cells for the current dimension
    # will be the sum of the number of cells
    # of all dimensions greater than or equal to the current one
    res = {}
    for i in range(2, size + 1):
        num_of_ceils = sum(counter[i:])
        if num_of_ceils:
            res[i] = num_of_ceils

    return res
