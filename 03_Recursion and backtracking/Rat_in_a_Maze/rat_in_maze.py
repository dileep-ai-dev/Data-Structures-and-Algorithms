def rat(matrix):

    if not matrix or matrix[0][0] == 0 or matrix[-1][-1] == 0:
        return []

    result = []

    directions = [
        (-1, 0, "up"),
        (0, -1, "left"),
        (1, 0, "down"),
        (0, 1, "right")
    ]

    def backtrack(current, row, col):

        # Base case: destination reached
        if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
            result.append(current.copy())
            return

        # Mark current cell as visited
        original_value = matrix[row][col]
        matrix[row][col] = 0

        # Try all four directions
        for dr, dc, direction_name in directions:

            next_row = row + dr
            next_col = col + dc

            if (
                0 <= next_row < len(matrix)
                and 0 <= next_col < len(matrix[0])
                and matrix[next_row][next_col] == 1
            ):
                current.append(direction_name)

                backtrack(current, next_row, next_col)

                # Backtrack
                current.pop()

        # Restore the cell
        matrix[row][col] = original_value

    # Start from the top-left cell
    backtrack([], 0, 0)

    return result


# Test case
print(
    rat([
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ])
)