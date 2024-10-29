class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}
        def dfs(r, c, last):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] <= last:
                return -1
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = 1 + max(
                dfs(r-1, c+1, grid[r][c]),
                dfs(r, c+1, grid[r][c]),
                dfs(r+1, c+1, grid[r][c]),
            )
            return memo[(r, c)]

        res = 0
        for i in range(ROWS):
            res = max(res, dfs(i, 0, float('-inf')))

        return res