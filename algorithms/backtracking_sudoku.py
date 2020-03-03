#!/usr/bin/python

class Solution:
    def next_free_spot(self, A, x, y):
        next_y = y + 1
        next_x = x + next_y // 9
        next_y = next_y % 9
        return next_x, next_y

    def is_valid_sudoku_position(self, A, x, y):
        v = A[x][y]

        for i in range(9):
            if i != x and A[i][y] == v:
                return False
            if i != y and A[x][i] == v:
                return False

            ix = i // 3
            iy = i % 3

            ux = (x // 3) * 3
            uy = (y // 3) * 3

            cx = ux + ix
            cy = uy + iy

            if cx != x and cy != y and A[cx][cy] == v:
                return False

        return True

    def solveSudokuRec(self, A, x = 0, y = 0):
        # we reached end of board
        if x >= 9:
            return A

        next_x, next_y = self.next_free_spot(A, x, y)

        solution = []
        # position is already taken
        if A[x][y] != '.':
            return self.solveSudokuRec(A, next_x, next_y)

        for i in range(1,10):
            A[x][y] = str(i)

            if self.is_valid_sudoku_position(A, x, y):
                solution = self.solveSudokuRec(A, next_x, next_y)
                # break the backtracking if solution found
                if len(solution) > 0:
                    return solution

            A[x][y] = '.'
        return solution

    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        return self.solveSudokuRec(A)


if __name__ == "__main__":
    solution = Solution()
    A = [list("53..7...."), list("6..195..."), list(".98....6."), list("8...6...3"), list("4..8.3..1"), list("7...2...6"), list(".6....28."), list("...419..5"), list("....8..79")]
    print(solution.solveSudoku(A))
