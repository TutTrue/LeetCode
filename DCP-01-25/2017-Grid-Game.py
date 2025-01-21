class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        l, r = 1, len(grid[0]) - 2
        while l < len(grid[0]):
            grid[1][l] += grid[1][l-1]
            grid[0][r] += grid[0][r+1]
            l+=1;r-=1
        res = max(grid[0][0], grid[1][-1])
        for i in range(len(grid[0])):
            res = min(
                res,
                max(
                    grid[0][i+1] if i < len(grid[0]) - 1 else 0,
                    grid[1][i-1] if i > 0 else 0
                )
            )
        return res