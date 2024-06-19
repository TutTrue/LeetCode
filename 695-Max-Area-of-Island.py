class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= N or c >= M or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            area = 1
            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)
            return area

        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        return max_area
