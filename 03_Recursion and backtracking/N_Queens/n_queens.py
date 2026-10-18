class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        matrix = [["."] * n for _ in range(n)]
        result = []

        def issafe(row, col):

            min_idx = min(row, col)
            start_r, start_col = row - min_idx, col - min_idx
            max_length = min(n - start_r, n - start_col)

            # Check main diagonal \
            for k in range(max_length):
                if (start_r + k) != row and matrix[start_r + k][start_col + k] == 'Q':
                    return False

            # Check anti-diagonal /
            for i in range(n):
                if 0 <= (row + col - i) < n and row != i and matrix[i][(row + col) - i] == 'Q':
                    return False

            # Check column
            for r in range(n):
                if matrix[r][col] == 'Q':
                    return False

            return True

        def backtrack(row):

            if row == n:
                result.append(["".join(row) for row in matrix])
                return

            for col in range(n):

                if issafe(row, col):

                    matrix[row][col] = 'Q'

                    backtrack(row + 1)

                    matrix[row][col] = "."

        backtrack(0)

        return result