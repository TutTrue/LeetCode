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