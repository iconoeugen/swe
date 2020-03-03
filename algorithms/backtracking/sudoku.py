#!/usr/bin/python

def sudoku_next_cell(row, col):
    next_row = row + 1
    next_col = col
    if next_row == 9:
        next_row = 0
        next_col += 1
    return next_row, next_col

def sudoku_valid_cell(row, col, solution):
    for i in range(0, 9):
        # check row
        if i != col and solution[row][i] == solution[row][col]:
            return False
        # check column
        if i != row and solution[i][col] == solution[row][col]:
            return False

        # check table sub-partition
        partition_start_row = row - (row % 3)
        partition_start_col = col - (col % 3)
        partition_row = partition_start_row + i % 3
        partition_col = partition_start_col + i // 3

        if partition_row != row and partition_col != col and \
           solution[partition_row][partition_col] == solution[row][col]:
           return False

    return True

def sudoku_print(solution):
    for row in solution:
        for cell in row:
            print("{:^3}".format(cell), end='')
        print('')

def sudoku(solution, row = 0, col = 0):
    if col == 9:
        # just filled a full sudoku
        sudoku_print(solution)
        return

    # where do we move next
    next_row, next_col = sudoku_next_cell(row, col)

    # cell is already populated and skip choice space
    if solution[row][col] != None:
        sudoku(solution, next_row, next_col)
        return

    for i in range(1, 10):
        solution[row][col] = i

        if sudoku_valid_cell(row, col, solution):
            sudoku(solution, next_row, next_col)

        # revert change
        solution[row][col] = None

if __name__ == "__main__":
    unsolved = [
        [None, None,    4, None,    5,    2, None, None,    1],
        [None,    6, None,    8,    1, None,    2,    5,    4],
        [None, None,    5, None,    7, None, None,    8,    3],
        [None, None, None, None, None,    5, None, None, None],
        [   7, None, None, None,    6, None, None, None,    8],
        [None, None, None,    7, None, None, None, None, None],
        [   1,    9, None, None,    2, None,    3, None, None],
        [   6,    7,    2, None,    3,    4, None,    1, None],
        [   5, None, None,    9,    8, None,    7, None,    2],
    ]

    #solved = 
    sudoku(unsolved)

    expected = [
        [   9,    8,    4,    3,    5,    2,    6,    7,    1],
        [   3,    6,    7,    8,    1,    9,    2,    5,    4],
        [   2,    1,    5,    4,    7,    6,    9,    8,    3],
        [   8,    3,    6,    2,    4,    5,    1,    9,    7],
        [   7,    5,    9,    1,    6,    3,    4,    2,    8],
        [   4,    2,    1,    7,    9,    8,    5,    3,    6],
        [   1,    9,    8,    6,    2,    7,    3,    4,    5],
        [   6,    7,    2,    5,    3,    4,    8,    1,    9],
        [   5,    4,    3,    9,    8,    1,    7,    6,    2],
    ]


    #assert(solved == expected)