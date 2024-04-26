class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for r in range(1, len(grid)):
            for c in range(len(grid[r])):
                m = float('inf')
                for i in range(len(grid[r])):
                    if i != c:
                        m = min(m, grid[r-1][i])
                grid[r][c] += m
        return min(grid[-1])
        # m = float('inf')
        # memo = {}
        # def rec(path=0, prev=(-1, 0)):
        #     nonlocal m
        #     if prev in memo:
        #         return
        #     if prev[1] == len(grid):
        #         m = min(m, path)
        #         memo[prev] = m
        #         return

        #     for i in range(len(grid[prev[1]])):
        #         if i != prev[0]:
        #             rec(path+grid[prev[1]][i], (i, prev[1]+1))
        # rec()
        # return m