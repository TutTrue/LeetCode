class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        s = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    s.add((i, j))
        for x, y in s:
            for i in range(len(matrix[x])):
                matrix[x][i] = 0
            for i in range(len(matrix)):
                matrix[i][y] = 0

