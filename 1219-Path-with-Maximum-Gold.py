class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = float('-inf')
        def rec(i, j, cur=0):
            nonlocal m
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                m = max(m, cur)
                return
            temp = grid[i][j]
            grid[i][j] = 0
            rec(i, j+1, cur+temp)
            rec(i, j-1, cur+temp)
            rec(i+1, j, cur+temp)
            rec(i-1, j, cur+temp)
            grid[i][j] = temp
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    rec(i, j)
        return m if m != float('-inf') else 0