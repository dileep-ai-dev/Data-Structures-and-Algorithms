class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isvalid(row, col, num):

            # Check row
            for i in range(len(board[0])):
                if board[row][i] == num:
                    return False

            # Check column
            for j in range(len(board)):
                if board[j][col] == num:
                    return False

            # Find the starting position of the 3x3 box
            start_row=(row//3)*3
            start_col=(col//3)*3

            # Check 3x3 box
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack(r, c):

            # Move to the next row
            if c == 9:
                return backtrack(r + 1, 0)

            # Entire board solved
            if r == 9:
                return True

            # Skip already filled cells
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            # Try numbers 1 to 9
            for val in range(1, 10):

                num = str(val)

                if isvalid(r, c, num):

                    # Choose
                    board[r][c] = num

                    # Explore
                    if backtrack(r, c + 1):
                        return True

                    # Undo
                    board[r][c] = "."

            return False

        backtrack(0, 0)