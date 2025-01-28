class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r == M or c < 0 or c == N or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0
            res = fish
            res+= dfs(r+1, c)
            res+= dfs(r-1, c)
            res+= dfs(r, c+1)
            res+= dfs(r, c-1)
            return res

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                res = max(res, dfs(r, c))
        return res
            