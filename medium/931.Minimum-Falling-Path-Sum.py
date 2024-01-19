# 931. Minimum Falling Path Sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                left = matrix[row-1][col-1] if col > 0 else float('inf')
                up = matrix[row-1][col]
                right = matrix[row-1][col +
                                      1] if col < len(matrix)-1 else float('inf')

                matrix[row][col] = matrix[row][col] + min(left, right, up)

        return min(matrix[-1])

# -------------------------------------------------------------

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dp(row, col):
            if col < 0 or col == len(matrix):
                return float('inf')
            if row == len(matrix):
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            memo[(row, col)] = matrix[row][col] + min(
                dp(row+1, col-1),
                dp(row+1, col),
                dp(row+1, col+1),
            )
            return memo[(row, col)]
        return min(dp(0, i) for i in range(len(matrix)))
