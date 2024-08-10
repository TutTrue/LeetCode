class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        res = 0
        my_grid = [[0 for i in range(n*3)] for j in range(n*3)]

        def dfs(r, c):
            if r < 0 or r >= len(my_grid) or c < 0 or c >= len(my_grid[0]) or my_grid[r][c] != 0:
                return

            my_grid[r][c] = 1

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(n):
            for j in range(n):
                if grid[i][j]=="/":
                    my_grid[i*3+0][j*3+2] = -1
                    my_grid[i*3+1][j*3+1] = -1
                    my_grid[i*3+2][j*3+0] = -1
                elif grid[i][j]=="\\":
                    my_grid[i*3+0][j*3+0] = -1
                    my_grid[i*3+1][j*3+1] = -1
                    my_grid[i*3+2][j*3+2] = -1
                    

        for i in range(n*3):
            for j in range(n*3):
                if my_grid[i][j]==0:
                    res += 1
                    dfs(i, j)
                

        return res
